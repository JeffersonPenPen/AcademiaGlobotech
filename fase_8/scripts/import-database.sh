#!/bin/bash

# Check for required tools
if ! command -v pg_dump &> /dev/null || ! command -v mysql &> /dev/null; then
    echo "pg_dump and mysql client tools are required but not installed."
    exit 1
fi

# Get RDS endpoint from CloudFormation stack
RDS_ENDPOINT=$(aws cloudformation describe-stacks --stack-name HoloTaskerHub --query "Stacks[0].Outputs[?OutputKey=='RdsEndpoint'].OutputValue" --output text)
if [ -z "$RDS_ENDPOINT" ]; then
    echo "Failed to retrieve RDS endpoint."
    exit 1
fi

# Prompt for Supabase credentials and RDS password
read -p "Enter your Supabase URL: " SUPABASE_URL
read -p "Enter your Supabase database name: " SUPABASE_DB
read -p "Enter your Supabase user: " SUPABASE_USER
read -sp "Enter your Supabase password: " SUPABASE_PASSWORD
echo
read -sp "Enter your RDS MySQL password: " RDS_PASSWORD
echo

# Export data from Supabase using pg_dump
DUMP_FILE="supabase_dump.sql"
pg_dump -h "$SUPABASE_URL" -U "$SUPABASE_USER" -d "$SUPABASE_DB" --no-owner --no-acl -F c -f "$DUMP_FILE" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "Failed to export data from Supabase."
    exit 1
fi

# Convert PostgreSQL syntax to MySQL syntax using sed
MYSQL_DUMP_FILE="mysql_dump.sql"
sed -e 's/\"//g' -e 's/::/ /g' "$DUMP_FILE" > "$MYSQL_DUMP_FILE"

# Import data to RDS MySQL
mysql -h "$RDS_ENDPOINT" -u "$SUPABASE_USER" -p"$RDS_PASSWORD" < "$MYSQL_DUMP_FILE"
if [ $? -ne 0 ]; then
    echo "Failed to import data to RDS MySQL."
    exit 1
fi

# Clean up temporary files
rm "$DUMP_FILE" "$MYSQL_DUMP_FILE"
echo "Data imported successfully to RDS MySQL."
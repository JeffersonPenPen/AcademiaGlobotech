#!/bin/bash

# Check if AWS CLI is installed
if ! command -v aws &> /dev/null; then
    echo "AWS CLI could not be found. Please install it."
    exit 1
fi

# Verify AWS credentials
if ! aws sts get-caller-identity &> /dev/null; then
    echo "AWS credentials are not configured correctly."
    exit 1
fi

# Create or update the CloudFormation stack
STACK_NAME="HoloTaskerHub"
TEMPLATE_FILE="path/to/your/template.yaml" # Update this with the actual path to your CloudFormation template

aws cloudformation deploy \
    --template-file "$TEMPLATE_FILE" \
    --stack-name "$STACK_NAME" \
    --capabilities CAPABILITY_NAMED_IAM

# Get Load Balancer DNS
LOAD_BALANCER_DNS=$(aws cloudformation describe-stacks --stack-name "$STACK_NAME" --query "Stacks[0].Outputs[?OutputKey=='LoadBalancerDNS'].OutputValue" --output text)

if [ -n "$LOAD_BALANCER_DNS" ]; then
    echo "Load Balancer DNS: $LOAD_BALANCER_DNS"
else
    echo "Load Balancer DNS not found."
fi

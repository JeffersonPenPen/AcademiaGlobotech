# Arquitetura AWS - Holo Tasker Hub

## Visão Geral

Este documento descreve a arquitetura completa da infraestrutura AWS para o projeto Holo Tasker Hub, implementada usando AWS CloudFormation.

## Componentes da Arquitetura

### 1. Network Layer
- VPC CIDR: 10.0.0.0/16
- Public Subnets: 10.0.1.0/24, 10.0.2.0/24
- Private Subnets: 10.0.10.0/24, 10.0.11.0/24

### 2. Compute Layer
- EC2 t2.micro instances
- Auto Scaling Group (min 2, max 4)
- Target Tracking Scaling (CPU 70%)

### 3. Load Balancing
- Application Load Balancer
- Health checks every 30 seconds

### 4. Database
- RDS MySQL 8.0 db.t3.micro
- 20 GB storage
- 7 days backup retention

### 5. Storage
- Amazon EFS encrypted
- General Purpose performance mode

### 6. Security
- Security Groups with least privilege
- RDS in private subnet
- Encryption at rest enabled

## Custos
- Free Tier: ~$18/mês
- Pós Free Tier: ~$50-60/mês

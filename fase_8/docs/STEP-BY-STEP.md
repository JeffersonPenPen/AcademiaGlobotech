# Guia Passo a Passo - Deploy do Holo Tasker Hub na AWS

Este guia detalha todos os passos necessários para fazer o deploy do projeto na AWS usando CloudFormation.

## Pré-requisitos

### 1. Conta AWS
- Criar conta AWS (Free Tier): https://aws.amazon.com/free/
- Verificar email
- Adicionar método de pagamento

### 2. AWS CLI Instalado

**Linux/Mac:**
```bash
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
```

**Windows:**
- Baixar: https://awscli.amazonaws.com/AWSCLIV2.msi

**Verificar:**
```bash
aws --version
```

### 3. Configurar AWS CLI

```bash
aws configure
# AWS Access Key ID: AKIA...
# AWS Secret Access Key: wJalr...
# Default region name: us-east-1
# Default output format: json
```

### 4. Criar Key Pair EC2

```bash
aws ec2 create-key-pair --key-name holotasker-key --query 'KeyMaterial' --output text > holotasker-key.pem
chmod 400 holotasker-key.pem
```

## Deploy da Stack

### Script Automatizado

```bash
chmod +x scripts/deploy.sh
./scripts/deploy.sh
```

### Manual

```bash
aws cloudformation create-stack --stack-name HoloTaskerHub --template-body file://cloudformation/template.yaml --parameters file://cloudformation/parameters.json --capabilities CAPABILITY_NAMED_IAM --region us-east-1
aws cloudformation wait stack-create-complete --stack-name HoloTaskerHub
```

## Verificação

```bash
aws cloudformation describe-stacks --stack-name HoloTaskerHub --query 'Stacks[0].Outputs[?OutputKey==`LoadBalancerDNS`].OutputValue' --output text
```

## Destruir Stack

```bash
./scripts/destroy.sh
```

---
**Autor**: Jefferson Ramos de Melo
**Data**: 2025-10-24
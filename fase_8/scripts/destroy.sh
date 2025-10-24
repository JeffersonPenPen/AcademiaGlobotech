#!/bin/bash

# Script para destruir a stack após apresentação
# CUIDADO: Isso deletará TODOS os recursos!

set -e

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

STACK_NAME="HoloTaskerHub"

echo ""
echo -e "${RED}⚠️  ATENÇÃO: Isso irá DELETAR toda a infraestrutura!${NC}"
echo ""
read -p "Tem certeza? Digite 'DELETAR' para confirmar: " CONFIRM

if [ "$CONFIRM" != "DELETAR" ]; then
    echo "Operação cancelada."
    exit 0
fi

echo ""
echo -e "${YELLOW}🗑️  Deletando stack $STACK_NAME...${NC}"

aws cloudformation delete-stack --stack-name $STACK_NAME
echo ""
echo -e "${YELLOW}⏳ Aguardando exclusão...${NC}"
aws cloudformation wait stack-delete-complete --stack-name $STACK_NAME
echo ""
echo -e "${GREEN}✅ Stack deletada com sucesso!${NC}"
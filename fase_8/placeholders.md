# Placeholders e Configurações do Projeto

Este documento lista todos os valores que precisam ser fornecidos ou ajustados no arquivo `template.yaml` antes de implantar a infraestrutura na AWS.

---

### 1. Parâmetros do Template (`Parameters`)

Estes valores são solicitados quando você cria a stack do CloudFormation.

-   **`DbPassword`**
    -   **Localização:** `template.yaml`, seção `Parameters`.
    -   **Descrição:** A senha para o usuário master do banco de dados RDS. Por segurança, o campo `NoEcho` está ativado, então a senha não será visível no console.
    -   **Ação:** Forneça uma senha segura com no mínimo 8 caracteres ao criar a stack.

-   **`MyIP`**
    -   **Localização:** `template.yaml`, seção `Parameters`.
    -   **Descrição:** Seu endereço IP público, usado para permitir o acesso SSH ao Bastion Host. O valor padrão `0.0.0.0/0` permite o acesso de qualquer lugar, o que **não é seguro para produção**.
    -   **Ação:** Substitua o valor padrão pelo seu IP público no formato CIDR (ex: `123.45.67.89/32`). Você pode descobrir seu IP pesquisando "what is my ip" no Google.

---

### 2. Valores Codificados no Template (`UserData`)

Estes valores estão dentro do script de inicialização das instâncias EC2 (`AppLaunchTemplate`). Para máxima segurança em um ambiente de produção, eles devem ser gerenciados através do **AWS Secrets Manager** em vez de estarem no template.

-   **`ImageId`**
    -   **Localização:** `template.yaml`, recurso `AppLaunchTemplate`.
    -   **Valor Atual:** `ami-0c55b159cbfafe1f0`
    -   **Descrição:** ID da Amazon Machine Image (AMI) para o Amazon Linux 2. Este ID é específico para a região `us-east-1` (N. Virginia).
    -   **Ação:** Se você for implantar em uma região diferente, precisará encontrar o ID da AMI do Amazon Linux 2 correspondente para aquela região.

-   **`JWT_SECRET`**
    -   **Localização:** `template.yaml`, recurso `AppLaunchTemplate`, dentro do script `UserData`.
    -   **Valor Atual:** `your-super-secret-jwt-key-that-should-be-in-secrets-manager`
    -   **Descrição:** A chave secreta usada para assinar os JSON Web Tokens (JWT) para autenticação de usuários.
    -   **Ação:** Substitua o valor por uma string longa, complexa e aleatória.

-   **`GEMINI_API_KEY`**
    -   **Localização:** `template.yaml`, recurso `AppLaunchTemplate`, dentro do script `UserData`.
    -   **Valor Atual:** `your-gemini-api-key-that-should-be-in-secrets-manager`
    -   **Descrição:** Sua chave de API para o serviço Google Gemini.
    -   **Ação:** Substitua o valor pela sua chave de API real do Gemini.

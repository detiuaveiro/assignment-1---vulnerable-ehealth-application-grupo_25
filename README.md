## SQL INJECTION (CWE-89) (Butuc)
- Versão Insegura:
    - Desparametrizar as queries **DONE**
    - Login a partir de método GET em vez de POST? **DONE**

## XSS (CWE-79) (Artur)
### Stored XSS
-**DONE**

### Reflected XSS
-**DONE**

## Improper Input Validation (CWE-20) (Daniel)
- Versão Segura: **DONE** 
    - Verificar que código de Exam é do Utilizador Logged In

## Missing Encryption of Sensitive Data (CWE-311) (Butuc)
- Versão Segura
    - Encriptar password na BD

## CWE-598: Use of GET Request Method With Sensitive Query Strings + CWE-200: Exposure of Sensitive Information to an Unauthorized Actor (Artur)
-**DONE**

## CWE-307: Improper Restriction of Excessive Authentication Attempts (Daniel)
- Versão Segura
    - Bloquear login após 5 tentativas de password erradas 

## CWE-552: Files or Directories Accessible to External Parties (Artur)
- Ambas
    - Botão HTML para fazer download de Exames
    - Função para criar .txt (num caminho separado)

- Versão Segura:
    - Verificar que o código do Exame pertence ao utilizador que está a fazer download

## CWE-522 + CWE-434 (Artur + Daniel)
- Ambas (Butuc)
    - Criar um ficheiro HTML para editar informações do perfil
    - Página deve ter opção para mudar pass e foto de perfil

- Versão Insegura:
    - No caminho URL, apresentar o ID do utilizador
    - Não verificar que a conta logged in é a conta da pessoa que está a editar o perfil

- Versão Segura:
    - Verificar terminação do ficheiro da foto (deve ser .png)
    -  Fazer verificações anteriores
    - Não apresentar ID no URL


## Relatório
    - Listar vulnerabilidades
    - Explicar o que elas são
    - Pensar nos ataques para cada uma

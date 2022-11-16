## SQL INJECTION (CWE-89) (Butuc)

- Versão Insegura:
    - Desparametrizar as queries
    - Login a partir de método GET em vez de POST?

## XSS (CWE-79) (Artur)
### Stored XSS
-DONE

### Reflected XSS
- Versão Insegura:
    - HTML das páginas Appointments/Patients/Prescriptions do Doctor dashboard, adicionar uma tag com "Foram encontrados x resultados para a sua pesquisa"

- Versão Segura:
    - HTML das páginas Appointments/Patients/Prescriptions do Doctor dashboard, adicionar uma tag com "Foram encontrados x resultados para a sua pesquisa"
    - Fazer escape de caracteres perigosos (<, >, &, etc)

## Improper Input Validation (CWE-20) (Daniel)
- Versão Segura:
    - Verificar que código de Exam é do Utilizador Logged In

### Missing Encryption of Sensitive Data (CWE-311) (Butuc)
- Versão Segura
    - Encriptar password na BD

### CWE-598: Use of GET Request Method With Sensitive Query Strings + CWE-200: Exposure of Sensitive Information to an Unauthorized Actor (Artur)
- Versão Segura
    - Aceder às páginas de patients/appointments/prescriptions/exams details na Doctor Dashboard com um POST em vez de GET na lupa

### CWE-307: Improper Restriction of Excessive Authentication Attempts (Daniel)
- Versão Segura
    - Bloquear login após 3 tentativas de password erradas (Procurar qual a CWE)

### CWE-552: Files or Directories Accessible to External Parties (Artur)
- Ambas
    - Botão HTML para fazer download de Exames
    - Função para criar .txt (num caminho separado)

- Versão Segura:
    - Verificar que o código do Exame pertence ao utilizador que está a fazer download

### CWE-522 + CWE-434 (Artur + Daniel)
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


### Relatório
    - Listar vulnerabilidades
    - Explicar o que elas são
    - Pensar nos ataques para cada uma

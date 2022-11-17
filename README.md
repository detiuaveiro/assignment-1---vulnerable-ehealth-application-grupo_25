Neste trabalho foi proposta a exploração de várias vulnerabilidades num website de uma empresa de gerenciamento de pacientes e médicos, ehealthCorp, com o objetivo de explorar as causas e os efeitos que estas inseguranças têm no bom funcionamento e desenvolvimento de uma aplicação, bem como as metodologias e as boas práticas que devem ser aplicadas para evitar a sua ocorrência. 

Com estes objetivos em mente, foram exploradas 10 vulnerabilidades diferentes numa versão insegura do website, sendo essas mesmo corrigidas numa versão semelhante, mas mais segura, do projeto. Ambas as aplicações foram desenvolvidas com recurso à framework web Flask, escrita em Python, utilizada tanto para a implementação do frontend como backend, com a base de dados relacional a ser implementada com recurso ao MySQL.

## Autores

- Artur Correia (nº mec 102477)
- André Butuc (nº mec 103530)
- Bruna Simões (nº mec 103453)
- Daniel Carvalho (nº mec 77036)

## Lista de Vulnerabilidades (CWE's) Implementadas

- CWE-89: Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') 
- CWE-79: Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting')
- CWE-20: Improper Input Validation
- CWE-311: Missing Encryption of Sensitive Data
- CWE-598: Use of GET Request Method With Sensitive Query Strings 
- CWE-200: Exposure of Sensitive Information to an Unauthorized Actor
- CWE-307: Improper Restriction of Excessive Authentication Attempts 
- CWE-522: Insufficiently Protected Credentials 
- CWE-434: Unrestricted Upload of File with Dangerous Type
- CWE-552: Files or Directories Accessible to External Parties

## Como Correr o Projeto

1. Instalar o docker-compose:
https://docs.docker.com/compose/

2. Abrir um terminal na pasta da versão do site que se pretende correr e executar o comando:

```
docker compose up
```

3. Aceder ao site pelo link:
http://localhost:5000/

## Credenciais de Acesso para Testar as Aplicações

- Conta do Paciente:
    - E-Mail: art.afo@ua.pt / Pass: 1904
    - Códigos de Prescrição a Testar: AXF03, AXF05, 0QAT8
    - Códigos de Levantamento de Exames a Testar: HGK10
    
- Conta do Médico:
    - E-Mail: afgomes@mail.pt / Pass: 1234

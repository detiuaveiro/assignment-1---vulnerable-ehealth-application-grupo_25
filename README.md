**Funcionalidades/Páginas do site**

- Homepage
- Login/Registo
- Form para contactar empresa

Utilizador:
- Marcar consultas/histórico de consultas
- Download de análises com código
- ...

Administrador:
- Backend c/ info do sistema

Médico:
- Dashboard com funcionalidades


**Vulnerabilidades**

- [SQL Injection - CWE 89](https://cwe.mitre.org/data/definitions/89.html)
  - Form para login
  - Tabelas do histórico de consultas 
  
  - Versão segura: Métodos de sanitização/Parametrização de queries (Verificar se não tem caracteres ilegais, fazer escape de caracteres ilegais), SP's para fazer verificações
  
- [XSS - CWE 79](https://cwe.mitre.org/data/definitions/79.html) 
  - Search Bar algures (p ex na lista de consultas?)
  - Página p/ noticias sobre saúde com comentários?
  
  - Versão segura: Content Security Protocol

- [Improper input Validation - CWE 20](https://cwe.mitre.org/data/definitions/20.html)
  - Página p/ levantar prescrições de medicamentos (não verificar o código passado)
  
  - Versão segura: Verificar input do utilizador 
  
- [Unrestricted Upload of File with Dangerous Type - CWE 434](https://cwe.mitre.org/data/definitions/434.html)
  - Inserção de fotografias/documentos (ex receitas, CC, etc)
  
  - Versão segura: Fazer verificação do formato do ficheiro

- [Improper authentication - CWE 287](https://cwe.mitre.org/data/definitions/287.html)
 
- [Unchecked return value - CWE 252](https://cwe.mitre.org/data/definitions/252.html)
 
- [Out of bound reads - CWE 175](https://cwe.mitre.org/data/definitions/125.html)


**Deteção de Vulnerabilidades**

- SQLMap
- Nikto

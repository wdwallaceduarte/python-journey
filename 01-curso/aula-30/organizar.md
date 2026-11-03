## Organização futura
### Arquitetura MVC
Como você deixou anotado no código que pretende estudar MVC, já vale começar a organizar as responsabilidades:

**`Camada ->`** Responsabilidade  
**`Model  ->`** Conectar e manipular o banco SQLite  
**`View   ->`** Criar janelas, campos e botões Tkinter  
**`Controller ->`** Receber ações do usuário e chamar o Model  

```plaintext
projeto/
│
├── model.py
│   ├── conectar_bd()
│   ├── consultar_bd()
│   ├── consultar_usuario_bd()
│   ├── inserir_usuario_bd()
│   ├── atualizar_usuario_bd()
│   └── deletar_usuario_bd()
│
├── view.py
│   ├── abrir_janela_principal()
│   └── abrir_tela_interna()
│
└── controller.py
    ├── realizar_login()
    ├── realizar_cadastro()
    └── realizar_logout()
```
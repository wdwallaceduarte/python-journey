# 🐍 Python Journey

Repositório com meus estudos e práticas em Python.

## 📂 Estrutura

- **01-curso/** — Exercícios das aulas do curso
- **02-pratica-casa/** — Práticas pessoais
- **03-coddy/** — Desafios do Coddy
- **04-projetos/** — Projetos maiores

```plaintext
python-journey/
│
├── README.md
├── .gitignore
├── LICENSE
│
├── 01-curso/                      # Exercícios do curso
│   ├── aula-01-introducao/
│   │   ├── README.md
│   │   └── exercicio_01.py
│   ├── aula-02-variaveis/
│   │   ├── README.md
│   │   └── exercicio_01.py
│   └── aula-03-condicionais/
│       └── ...
│
├── 02-pratica-casa/               # Exercícios próprios
│   ├── 01-basico/
│   │   ├── hello_world.py
│   │   └── calculadora.py
│   ├── 02-intermediario/
│   │   └── ...
│   └── 03-desafios/
│       └── ...
│
├── 03-coddy/                      # Exercícios do Coddy
│   ├── nivel-01-fundamentos/
│   ├── nivel-02-estruturas/
│   └── nivel-03-funcoes/
│
└── 04-projetos/                   # Projetos maiores (futuro)
    └── ...
``` 

## 🚀 Progresso

- [x] Variáveis e tipos
- [x] Condicionais
- [ ] Laços de repetição
- [ ] Funções


# Padrão de Mensagens de Commit (Conventional Commits)

- `feat:` - Movo exercício/projeto  
- `fix:` - Correção de código  
- `docs:`- Aleteração em README  
- `refactor:` - Melhora código sem mudar comportamento  
- `chore:` - Tarefas de organização (criar pasta, etc...)  

## Exemplos
```
git commit -m "feat(curso): aula 05 - funções"
git commit -m "feat(coddy): nível 02 - listas"
git commit -m "docs: atualiza progresso no README"
git commit -m "refactor(pratica): simplifica calculadora"
```
`git commit --amend --no-edit` - Comando para adcionar arquivo no ultimo commit  
`git push -u origin main` - comando usado para o primeiro push 

## Comandos de Remoção
• Remover o nome de usuário global:  
`git config --global --unset user.name`  
• Remover o e-mail global:  
`git config --global --unset user.email`  

### Configurações Locais (Apenas para o repositório atual)
Se você quiser remover as configurações apenas do projeto em que está trabalhando no momento, remova a flag --global:  
• `git config --unset user.name`  
• `git config --unset user.email`  
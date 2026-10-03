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

## Comandos diarios no curso 
• `git pull` - ao chegar se tiver realizado alguma alteração e subido para o github em casa 
• `git add .` - comando que adiciona todos or arquivos modfivados, criados ou excluidos
• `git commit -m "menssgem"` - comando para colocar uma mensagem informando o que foi alterado 
• `git push` - comando apra enviar os arquivos altarados para o github
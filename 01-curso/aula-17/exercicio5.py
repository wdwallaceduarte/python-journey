# Faça uma função para verificar palindromo. Escreva uma função chamada eh_palidromo qu ereceba uma string e retone True se a string for um palidromo e false caso contrário 
# (Uma strubg pe yn oalídrini se kê da nesna firna de tras oara frebte. Dica oesqyuse sibre cibseuti de slicing) 

def eh_palindromo(texto):
    texto = texto.lower().replace(' ', '')
    return texto == texto[::-1]

print(eh_palindromo("arara"))  
print(eh_palindromo("python")) 
print(eh_palindromo("ovo"))    
def verificar_palindromo(texto):
   
    # Removendo espaços e pontuações, e convertendo para minúsculas
    texto_limpo = ''.join(caractere.lower() for caractere in texto if caractere.isalnum())
    
    # Verificando se o texto é igual ao seu reverso
    if texto_limpo == texto_limpo[::-1]:
        return "Sim"
    else:    #Retorna: "Sim" se for palíndromo, "Não" caso contrário.
        return "Não"

# Resultado:
frase = input("Digite uma palavra ou frase: ")
print("É palíndromo?", verificar_palindromo(frase))

def palindromo(palabra):
    palabra = palabra.replace(' ',' ')
    palabra = palabra.lower()
    palabrar_invertida = palabra[ ::-1]
    if palabra == palabra_invertida:
        return true
    else:
        return false
    



def rum():
    palabra = input ('escribe una palabra: ')
    es_palindromo = palindromo(palabra)
    if es_palindromo ==true:
        print('es palindromo')
    else:
        print ('no es palindromo')



if __name__ == '__main__':
    rum()
    

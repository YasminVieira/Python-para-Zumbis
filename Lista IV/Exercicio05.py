# Seja o mesmo texto acima “splitado”. Calcule quantas palavras possuem uma das letras “python” e que tenham mais de 4 caracteres.
# Não se esqueça de transformar maiúsculas para minúsculas e de remover antes os caracteres especiais:

texto = '''The Python Software Foundation and the global Python
community welcome and encourage participation by everyone. Our community is based on
mutual respect, tolerance, and encouragement, and we are working to help each other live up
to these principles. We want our community to be more diverse: whoever you are, and
whatever your background, we welcome you.'''.lower()
texto = texto.replace(',', ' ').replace('.', ' ').replace(':', ' ')
texto = texto.split()

def é_pythonica(p):
    if len(p) <= 4:
        return False
    
    for c in p:
        if c in 'python':
            return True

    return False

lista = []
for p in texto:
    if é_pythonica(p):
        lista.append(p)

print(lista)
print(len(lista))

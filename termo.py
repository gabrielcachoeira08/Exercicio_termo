with open('todas_palavras.txt', 'r', encoding='utf-8') as entrada, \
    open('palavras_validas.txt', 'w', encoding='utf-8') as saida:

    for linha in entrada:
        palavra = linha.strip()

        if len(palavra) == 5:
            saida.write(palavra + '\n')

with open('palavras_validas.txt', 'r', encoding='utf-8') as arquivo:
    palavras = arquivo.read()
    print(palavras)



#sem usar o documento ainda
palavra_secreta = "lapis"
chute = ""
tentativa = 1

acertos = ""
while acertos != "🟩🟩🟩🟩🟩":
    acertos = ""
    tentativa = input("Digite uma palavra:")
    for i in range (5):
        if tentativa[i] == palavra_secreta[i]:
            acertos += "🟩"
        elif tentativa[i] in palavra_secreta:
            acertos += "🟨"
        else:
            acertos += "⬛️"
    print(acertos)
# Mini Bot de Perguntas sobre Python

print("Olá, eu sou o GenshinBot!")
print("Digite 'sair' para encerrar a conversa.\n")

while True:
    pergunta = input("Você: ").strip().lower()

    if pergunta == "sair":
        print("PyBot: Até mais! Bons estudos! 👋")
        break

    # Respostas pré-definidas
    elif "banners" in pergunta:
        print("Os banners da 6.0 são: Lauma e Nahida na primeira fase e Flins e Yelan na segunda fase.")

    elif "condicional" in pergunta or "if" in pergunta:
        print("🤖: Condicionais permitem executar código baseado em condições. Exemplo:\nif x > 10:\n    print('Maior que 10')")

    elif "laço" in pergunta or "loop" in pergunta or "for" in pergunta:
        print("🤖: Laços repetem código várias vezes. Exemplo:\nfor i in range(5):\n    print(i)")

    elif "while" in pergunta:
        print("🤖: O laço while repete enquanto a condição for verdadeira. Exemplo:\nwhile x < 5:\n    x += 1")

    elif "randint" in pergunta or "aleatório" in pergunta:
        print("🤖: Você pode gerar números aleatórios com a biblioteca random.\nExemplo:\nfrom random import randint\nnumero = randint(1, 10)")

    else:
        print("🤖: Hmmm... não entendi. Pergunte sobre variáveis, condicionais, laços ou randint.")

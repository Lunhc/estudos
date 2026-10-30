# ----------------------------------------------------------------
#                        CHAT BOT PYTHON 
# ----------------------------------------------------------------

# COMO RODAR: PYTHON CHATBOT.PY
# PARA SAIR: Digite 'Sair'

def responder(mensagem):
    mensagem = mensagem.lower().strip()

    if mensagem in ('oi', 'ola', 'ola', 'e ai', 'eai'):
        return 'Olá! Tudo bem com voce?'

    elif'tudo bem' in mensagem or 'como vai' in mensagem:
        return 'Tudo Otimo por aqui! Estou aprendendo a conversa'

    elif'seu nome'in mensagem or 'quem e voce' in mensagem:
        return 'Eu sou o Sidney, um chatbot feito em Python pela Luh'

    elif 'ajuda' in mensagem:
        return 'Tente dizer: oi, tudo bem?, qual seu nome? ou sair'

    else:
        return 'Hm, ainda nao sei responder isso. tente *ajuda* .'

def main():
    print('==== Chatbot Sideny ====')
    print("Digite 'Sair' para encerrar.\n")

    while True:
        entrada = input('Voce: ')

        if entrada.lower().strip() == "sair":
            print("Sidney: Até mais! 👋")
            break

        resposta = responder(entrada)
        print(f'Sidney: {resposta}')


if __name__ == '__main__':
    main()
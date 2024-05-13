def process_input(user_input):
    # Dividir a entrada do usuário em palavras
    words = user_input.split()

    # Lógica para verificar cada palavra
    for word in words:
        # Aqui você pode adicionar suas próprias condições para cada palavra
        if word == 'ajuda':
            return "Posso ajudar você com alguma coisa?"
        elif word == 'informação':
            return "Que tipo de informação você está procurando?"
        # Adicione mais condições conforme necessário

    # Se nenhuma condição for correspondida, retornar uma resposta padrão
    return "Desculpe, não entendi o que você quis dizer."

# Função principal do chatbot
def chat(cursor):
    print("Olá! Eu sou um chatbot. Como posso te ajudar hoje?")
    while True:
        user_input = input("Você: ").strip().lower()
        if user_input == 'sair':
            print("Até logo!")
            break
        else:
            response = process_input(user_input)
            print("Bot: ", response)


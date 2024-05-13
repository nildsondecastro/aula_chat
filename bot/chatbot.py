def search_question(query, cursor):
    # Consulta SQL para recuperar a resposta com base na pergunta
    cursor.execute("SELECT resposta FROM perguntas_respostas WHERE pergunta ILIKE %s", (query,))
    answer = cursor.fetchone()

    return answer[0] if answer else "Desculpe, não consegui encontrar uma resposta para sua pergunta."

# Função principal do chatbot
def chat(cursor):
    print("Olá! Eu sou um chatbot. Como posso te ajudar hoje?")
    while True:
        user_input = input("Você: ").strip().lower()

        if user_input == 'sair':
            print("Até logo!")
            break
        else:
            response = search_question(user_input, cursor)
            print("Bot: ", response)

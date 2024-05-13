from database.connection import connect_to_database
from bot.chatbot import chat

def main():
    # Estabelecer conexão com o banco de dados
    conn, cursor = connect_to_database()

    # Iniciar o chatbot
    chat(cursor)

    # Fechar o cursor e a conexão ao sair
    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()

from twilio.rest import Client
from config import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_WHATSAPP_NUMBER

def send_whatsapp_message(to, message):
    try:
        # Inicializando o cliente Twilio
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

        # Enviando a mensagem via WhatsApp
        message = client.messages.create(
            body=message,           # Conteúdo da mensagem
            from_=f'whatsapp:{TWILIO_WHATSAPP_NUMBER}',  # Remetente
            to=f'whatsapp:{to}'      # Destinatário
        )
        
        return message.sid  # Retorna o SID da mensagem

    except Exception as e:
        print(f"Erro ao enviar mensagem: {e}")
        return None

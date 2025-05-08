# script de execução da função send_whatsapp_message (arquivo whatsapp.py)

from merlot.service.whatsapp import send_whatsapp_message  # Importação do módulo com a função

# Número do destinatário e a mensagem
numero = "whatsapp:+556791499806"  # Número precisa estar registrado no sandbox da Twilio, senão dá certo!!!
mensagem = "Seja bem-vindo(a) ao sistema de notificação Merlot"  

# Chamada da função e impressão do SID (rastreio)
sid = send_whatsapp_message(numero, mensagem)

if sid:
    print(f"Mensagem enviada! SID: {sid}")  # SID é o identificador único da mensagem
else:
    print("Falha ao enviar mensagem.")  

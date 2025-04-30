import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Carregar credenciais da Twilio
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
from_whatsapp = os.getenv("TWILIO_WHATSAPP_NUMBER")

# Verificar se as variáveis de ambiente foram carregadas corretamente
if not all([account_sid, auth_token, from_whatsapp]):
    raise EnvironmentError("Probelma nas variaveis do Twilio!")

# Variáveis de configuração para o Twilio
TWILIO_ACCOUNT_SID = account_sid
TWILIO_AUTH_TOKEN = auth_token
TWILIO_WHATSAPP_NUMBER = from_whatsapp

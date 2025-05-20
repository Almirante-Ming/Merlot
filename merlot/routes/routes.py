from flask import Blueprint, request
from twilio.twiml.messaging_response import MessagingResponse

from merlot.database.database import SessionLocal
from merlot.models.paciente import Paciente
from merlot.models.consulta import Consulta
from merlot.models.medico import Medico
from sqlalchemy.orm import joinedload


SAUDACOES = ["oi", "olá", "ola", "bom dia", "boa tarde", "boa noite"]

bp = Blueprint('bot', __name__)


def msg_saudacao(msg):
    return any(s in msg.lower() for s in SAUDACOES)


def buscar_paciente(msg):
    db = SessionLocal()
    paciente = db.query(Paciente).filter(
        (Paciente.nome.ilike(f"%{msg}%")) | (Paciente.cpf == msg)
    ).first()
    db.close()
    return paciente

# Função para verificar consultas ativas (com joinedload)
def consultar_consultas(paciente):
    db = SessionLocal()
    consultas = db.query(Consulta).options(
        joinedload(Consulta.medico)
    ).filter_by(
        id_paciente=paciente.id_paciente,
        status="ativa"
    ).all()
    db.close()
    return consultas

# Rota principal do WhatsApp
@bp.route("/mensagem", methods=["POST"])
def mensagem_whatsapp():
    msg = request.form.get("Body", "").strip()
    
    resp = MessagingResponse()
    resposta = resp.message()

    if not msg:
        resposta.body("Mensagem vazia! Digite seu CPF ou Nome Completo.")
        return str(resp)

    if msg_saudacao(msg):
        resposta.body(
            "👋 Olá! Você está falando com o *Sistema de Consultas Merlot*.\n\n"
            "Envie seu *nome completo* ou *CPF* para verificarmos suas consultas."
        )
        return str(resp)

    paciente = buscar_paciente(msg)
    
    if paciente:
        consultas = consultar_consultas(paciente)

        if consultas:
            texto = f"Consultas ativas para {paciente.nome}:\n"
            for c in consultas:
                texto += (
                    f"- Agendado para {c.data.strftime('%d/%m/%Y')} "
                    f"às {c.hora.strftime('%Hh%M')} com {c.medico.nome}\n"
                )
            resposta.body(texto)
        else:
            resposta.body("Paciente encontrado, mas nenhuma consulta ativa no momento.")
    else:
        resposta.body("Paciente não encontrado. Verifique se o nome ou CPF está correto.")

    return str(resp)

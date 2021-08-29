# Teste da FastZap
Implementação de um chat realtime com django + django rest + web sockets (django channels)

# Requirements
## Pacotes python:
pip install -r requirements.txt

## Redis na porta 6379:
 docker run -p 6379:6379 -d redis:5
 
# Visualizar chat cliente:
http://127.0.0.1:8000/chat/id-atendimento/

# Visualizar chat atendente
http://127.0.0.1:8000/chat/atendente/id-atendimento/

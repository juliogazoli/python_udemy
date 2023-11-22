"""
Ambientes virtuais em Python (venv)
Um ambiente virtual carrega toda a sua instalação
do Python para uma pasta no caminho escolhido.
Ao ativar um ambiente virtual, a instalação do
ambiente virtual será usada.
venv é o módulo que vamos usar para
criar ambientes virtuais.
Você pode dar o nome que preferir para um
ambiente virtual, mas os mais comuns são:
venv env .venv .env
"""

# Criar ambiente virtual
# python -m venv venv

# Verificar local de um executável (Windows PowerShell)
# gcm python
# gcm python -Syntax

# Verificar local de um executável (Linux)
# which python3

# Ativar o ambiente virtual (Windows)
# .\venv\Scripts\activate

# Ativar o ambiente virtual (Windows)
# source venv/bin/activate
# . venv/bin/activate

# Desativar ambiente virtual
# deactivate


# pip - instalando pacotes e bibliotecas

# Instalar versão mais atual:
# pip install nome_pacote

# Instalar versão específica:
# (tem outras formas também não mencionadas)
# pip install nome_pacote==0.0.0

# Verificar versões:
# pip index versions nome_pacote

# Atualizar pacote
# pip install nome_pacote --upgrade

# Desinstalar pacote:
# pip uninstall nome_pacote

# Congelar (ver pacotes):
# pip freeze

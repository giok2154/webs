"""
OpenAI Client
-------------
Configuración oficial basada en la documentación:
https://platform.openai.com/docs/api-reference/introduction
"""

import os
from openai import OpenAI

# Crear cliente global de OpenAI usando la API Key desde el entorno (.env)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

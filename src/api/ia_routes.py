"""
IA Routes Module
---------------
Blueprint que agrupa las rutas relacionadas con Inteligencia Artificial.
Documentación oficial: https://flask.palletsprojects.com/en/3.0.x/blueprints/
"""

from flask import Blueprint, jsonify, request
from api.ai_utils.openai_client import client  # 👈 IMPORTACIÓN CORRECTA DEL CLIENTE

ia_api = Blueprint('ia_api', __name__)

@ia_api.route('/test', methods=['GET'])
def test_ia():
    """
    Ruta de prueba para verificar que el módulo IA está activo.
    """
    return jsonify({
        "status": "ok",
        "message": "El módulo de IA está funcionando correctamente 🚀"
    }), 200


@ia_api.route('/image', methods=['POST'])
def generate_image():
    """
    Endpoint oficial para generar imágenes con OpenAI.
    Documentación: https://platform.openai.com/docs/api-reference/images/create
    """
    data = request.get_json()
    prompt = data.get("prompt")

    if not prompt:
        return jsonify({"error": "Missing 'prompt' field"}), 400

    try:
        result = client.images.generate(
            model="gpt-image-1",
            prompt=prompt,
            size="1024x1024"
        )

        # Extraemos la URL de la imagen generada
        image_url = result.data[0].url

        return jsonify({
            "status": "ok",
            "prompt": prompt,
            "image_url": image_url
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

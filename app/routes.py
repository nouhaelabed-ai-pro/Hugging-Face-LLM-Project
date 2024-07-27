from flask import Blueprint, request, jsonify, render_template, current_app
from .models import LangChainModel

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/api/llm/generate', methods=['POST'])
def generate_response():
    repo_id = current_app.config['HF_API_REPO']
    api_key = current_app.config['HF_API_KEY']
    model = LangChainModel(repo_id=repo_id, api_key=api_key)

    prompt = request.json.get('prompt')
    response = model.generate_response(prompt)
    return jsonify({'response': response})

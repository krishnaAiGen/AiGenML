from flask import Flask, request, jsonify

from controllers.sentiment_controller import SentimentController
from controllers.translation_controller import TranslationController
from controllers.poem_controller import PoemController
from utils import load_config, class_factory

app = Flask(__name__)

# Load configuration
CONFIG = load_config()


@app.route('/translate', methods=['POST'])
def translate_text():
    try:
        data = request.get_json()
        text = data['text']
        model = data.get('model', 'phi3')  # Use a default model if not provided
        controller_name = 'TranslationController'
        translated_text = generate_response(text, model, controller_name)
        return jsonify({'response': translated_text})
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/sentiment', methods=['POST'])
def analyze_sentiment():
    try:
        data = request.get_json()
        text = data['text']
        model = data.get('model', 'phi3')  # Use a default model if not provided
        controller_name = 'SentimentController'
        sentiment_result = generate_response(text, model, controller_name)
        return jsonify({'response': sentiment_result})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/poem', methods=['POST'])
def generate_poem():
    try:
        data = request.get_json()
        print(data)
        text = data['text']
        model = data.get('model', 'phi3')  # Use a default model if not provided
        controller_name = 'PoemController'
        poem_result = generate_response(text, model, controller_name)
        return jsonify({'response': poem_result})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

def generate_response(text, model, controller_name):
    try:
        model = CONFIG[model]
        controller = class_factory(controller_name, model)

        if isinstance(controller, TranslationController):
            translated_text = controller.generate_translation(text)
            return translated_text

        elif isinstance(controller, SentimentController):
            sentiment_result = controller.generate_sentiment(text)
            return sentiment_result
        
        elif isinstance(controller, PoemController):
            poem_result = controller.generate_poem(text)
            return poem_result
            
        else:
            raise ValueError(f"Unsupported controller type: {controller_name}")

    except Exception as e:
        print(f"An error occurred: {e}")
        return None


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


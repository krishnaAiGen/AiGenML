import json
import os

from controllers.sentiment_controller import SentimentController
from controllers.translation_controller import TranslationController
from controllers.poem_controller import PoemController

def load_config():
    config_path = os.path.join(os.path.dirname(__file__), 'config.json')
    with open(config_path, 'r') as config_file:
        return json.load(config_file)
    
def load_prompt():
    with open(os.getcwd() + "/controllers/prompt.json", 'r') as file:
        prompt = json.load(file)
    
    return prompt

def class_factory(controller_name, model):
    if controller_name == "TranslationController":
        return TranslationController(model)
    elif controller_name == "SentimentController":
        return SentimentController(model)
    elif controller_name == "PoemController":
        return PoemController((model))
    else:
        raise ValueError(f"Unknown controller name: {controller_name}")


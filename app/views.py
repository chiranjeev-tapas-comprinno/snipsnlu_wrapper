"""
This app is just to wrap the snipsnlu library in a container.
The code and the logic is taken from the snipsnlu's github page.
Ref: https://github.com/snipsco/snips-nlu#sample-code

The app is suppose to process a query which is made in natural language
like english and return a structured output.
The app trains a NLP engine created by snipsnlu, with the help of a sample
dataset provided in the repository itself.
The training dataset can be extended to get a more precise answer and reduce
false positive results.

Program Logic:
    - On starting the app we will load the sample dataset which act as a
    training data for out NLP model.
    - The api will accept call made to /nlu api,
        - This api will accept only POST request which must be in a json format.
        - The sample request data will be as follows:
            {"sentence": "What will be the weather in paris at 9pm?"}
        - The data will then be passed to our trained NLP model and we get our
        output in a json format itself.
"""
import json

from nlu import NLU
from flask import Blueprint, request, jsonify

nlu_bp = Blueprint('nlu', __name__)

# Global variables
_nlu = None


# We define a function here which will be called when the the app is started.
def get_ready():
    """
    This method will be called only once to setup and train the NLU engine.
    :return:
    """
    global _nlu
    _nlu = NLU()
    _nlu.train_engine()


@nlu_bp.route('/nlu', methods=['POST'])
def parse_query():
    """
    Here we have denied a method which will parse the query which is in natural
    language using the trained nlp engine.
    :return:
    """
    required_output = dict()
    if request.method == "POST":
        post_data = request.get_json()
        print(post_data.get("sentence"))
        result = _nlu.parse_sentence(post_data.get("sentence"))
        required_output['intent'] = result.get('intent')
        required_output['slots'] = result.get('slots')
        return jsonify(required_output)

from __future__ import unicode_literals, print_function
from pathlib import Path

import io
import json

from snips_nlu import SnipsNLUEngine, load_resources
from snips_nlu.default_configs import CONFIG_EN


class NLU:

    def __init__(self):
        self.sample_dataset = NLU.load_dataset()

    @staticmethod
    def load_dataset():
        """
        Load the sample dataset which will be used to train the snipsnlu NLP
        engine.
        :return:
        """
        try:
            with io.open(str(Path('app', 'static', 'samples', 'sample_dataset.json'))) as fr:
                sample_dataset = json.load(fr)
            return sample_dataset
        except Exception as e:
            print("Could not load dataset {}".format(str(e)))

    def train_engine(self):
        """
        # Setup the snipsnlu NLP engine and pass the training data.
        :return:
        """
        load_resources("en")
        self.nlu_engine = SnipsNLUEngine(config=CONFIG_EN)
        self.nlu_engine.fit(self.sample_dataset)

    def parse_sentence(self, sentence):
        """
        Get the sentence and parse it to get the result.
        The sentence is a query made in any natural language(for now we are
        setting this language as english) and the result is the json string
        with the parsed help of trained engine and the possible correct
        prediction of what the query actually meant.
        :param sentence:
        :return:
        """
        parsing = self.nlu_engine.parse(sentence)
        return parsing





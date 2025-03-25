import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import jedi
import subprocess
import pandas as pd

class CorneliusAI:
    def __init__(self, model_path, tokenizer):
        self.model = tf.keras.models.load_model(model_path)
        self.tokenizer = tokenizer
        self.max_length = self.model.input_shape[1]

    def code_completion(self, code):
        sequence = self.tokenizer.texts_to_sequences([code])
        padded_sequence = pad_sequences(sequence, maxlen=self.max_length, padding='post')
        prediction = self.model.predict(padded_sequence)
        predicted_word_index = np.argmax(prediction, axis=-1)[0]
        predicted_word = self.tokenizer.index_word.get(predicted_word_index, '')
        return predicted_word

    def error_detection(self, code):
        with open('temp_code.py', 'w', encoding='utf-8') as f:
            f.write(code)
        result = subprocess.run(['pylint', 'temp_code.py'], capture_output=True, text=True)
        return result.stdout

    def get_documentation(self, keyword):
        script = jedi.Script(f'import {keyword}')
        docstring = script.help()
        return docstring

# Example usage
if __name__ == "__main__":
    # Load tokenizer and data
    tokenizer = Tokenizer()
    data = pd.read_csv('processed_code_data.csv')['code'].values
    tokenizer.fit_on_texts(data)

    # Initialize Cornelius AI
    assistant = CorneliusAI('cornelius_model.h5', tokenizer)

    # Example code completion
    code = "import os\nos."
    print("Code Completion:", assistant.code_completion(code))

    # Example error detection
    code_with_error = "import os\nos.listdir("
    print("Error Detection:", assistant.error_detection(code_with_error))

    # Example documentation retrieval
    keyword = "os.listdir"
    print("Documentation:", assistant.get_documentation(keyword))
import openai
import tensorflow as tf
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Embedding
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

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
        predicted_word = self.tokenizer.index_word[predicted_word_index]
        return predicted_word

    def error_detection(self, code):
        with open('temp_code.py', 'w') as f:
            f.write(code)
        result = subprocess.run(['pylint', 'temp_code.py'], capture_output=True, text=True)
        return result.stdout

    def get_documentation(self, keyword):
        script = jedi.Script(f'import {keyword}')
        docstring = script.help()
        return docstring

def collect_code_data(directory):
    code_data = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    code_data.append(f.read())
    return code_data

def preprocess_code_data(code_data):
    processed_data = []
    for code in code_data:
        # Remove comments and docstrings
        code = '\n'.join([line for line in code.split('\n') if not line.strip().startswith('#')])
        code = '\n'.join([line for line in code.split('\n') if not line.strip().startswith('"""')])
        processed_data.append(code)
    return processed_data

def load_data(file_path):
    df = pd.read_csv(file_path)
    return df['code'].values

def preprocess_data(data, tokenizer, max_length):
    sequences = tokenizer.texts_to_sequences(data)
    padded_sequences = pad_sequences(sequences, maxlen=max_length, padding='post')
    return padded_sequences

def build_model(vocab_size, max_length):
    model = Sequential([
        Embedding(vocab_size, 128, input_length=max_length),
        LSTM(128, return_sequences=True),
        LSTM(128),
        Dense(128, activation='relu'),
        Dense(vocab_size, activation='softmax')
    ])
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    return model

# Example usage
if __name__ == "__main__":
    tokenizer = Tokenizer()
    data = pd.read_csv('processed_code_data.csv')['code'].values
    tokenizer.fit_on_texts(data)

    assistant = CorneliusAI('cornelius_model.h5', tokenizer)

    code = "import os\nos."
    print("Code Completion:", assistant.code_completion(code))

    code_with_error = "import os\nos.listdir("
    print("Error Detection:", assistant.error_detection(code_with_error))

    keyword = "os.listdir"
    print("Documentation:", assistant.get_documentation(keyword))

    directory = "path_to_code_directory"
    code_data = collect_code_data(directory)
    processed_data = preprocess_code_data(code_data)
    df = pd.DataFrame(processed_data, columns=['code'])
    df.to_csv('processed_code_data.csv', index=False)

    data = load_data('processed_code_data.csv')
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(data)
    vocab_size = len(tokenizer.word_index) + 1
    max_length = max([len(code.split()) for code in data])

    X = preprocess_data(data, tokenizer, max_length)
    y = X[:, 1:]
    X = X[:, :-1]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = build_model(vocab_size, max_length)
    model.fit(X_train, y_train, epochs=10, validation_data=(X_test, y_test))

    model.save('cornelius_model.h5')
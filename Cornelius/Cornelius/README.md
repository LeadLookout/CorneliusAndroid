# Cornelius AI

Cornelius is an independent and self-learning AI assistant designed to help sole developers with tasks such as code completion, error detection, and providing documentation.

## Setup

1. Clone the repository:
    ```sh
    git clone <repository_url>
    cd Cornelius/Cornelius
    ```

2. Create a virtual environment:
    ```sh
    python -m venv venv
    ```

3. Activate the virtual environment:
    - On Windows:
        ```sh
        .\venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source venv/bin/activate
        ```

4. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

5. Collect and preprocess code data:
    ```sh
    python data/data_preprocessing.py
    ```

6. Train the model:
    ```sh
    python models/train_model.py
    ```

7. Optimize the model:
    ```sh
    python models/optimize_model.py
    ```

## Usage

Run the `main.py` script to see the basic functionalities of Cornelius:

```sh
python main.py
```
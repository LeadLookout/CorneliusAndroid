# CorneliusAndroid
Cornelius AI
Cornelius is an independent and self-learning AI assistant designed to help sole developers with tasks such as code completion, error detection, and providing documentation.

Setup
Clone the repository:

git clone <repository_url>
cd Cornelius/Cornelius
Create a virtual environment:

python -m venv venv
Activate the virtual environment:

On Windows:
.\venv\Scripts\activate
On macOS/Linux:
source venv/bin/activate
Install the dependencies:

pip install -r requirements.txt
Collect and preprocess code data:

python data/data_preprocessing.py
Train the model:

python models/train_model.py
Optimize the model:

python models/optimize_model.py
Usage
Run the main.py script to see the basic functionalities of Cornelius:

python main.py

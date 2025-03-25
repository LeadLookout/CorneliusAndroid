import logging
from core import AutonomousLearning

def setup_logging():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    setup_logging()
    logging.info("Starting Cornelius launch process")
    try:
        learning_system = AutonomousLearning()
        learning_system.start()
        logging.info("Cornelius launched successfully")
    except Exception as e:
        logging.error(f"Error during launch: {e}")
        raise

if __name__ == "__main__":
    main()

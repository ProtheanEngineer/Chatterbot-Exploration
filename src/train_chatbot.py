import os
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

def get_yaml_files(directory):
    # Get all YAML files in the specified directory
    return [f for f in os.listdir(directory) if f.endswith('.yml')]

def train_chatbot():
    # Initialize the chatbot
    chatbot = ChatBot('Chatbot')

    # Create a new trainer for the chatbot
    trainer = ChatterBotCorpusTrainer(chatbot)

    # Train the chatbot on the ChatterBot corpora
    # trainer.train('chatterbot.corpus.english')
    trainer.train('chatterbot.corpus.spanish')

    # Train the chatbot on custom datasets in language folders
    data_path = 'data/'
    for language_folder in os.listdir(data_path):
        language_path = os.path.join(data_path, language_folder)
        if os.path.isdir(language_path):
            yaml_files = get_yaml_files(language_path)
            for yaml_file in yaml_files:
                file_path = os.path.join(language_path, yaml_file)
                trainer.train(file_path)

if __name__ == "__main__":
    train_chatbot()

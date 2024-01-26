import chatterbot
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import chatterbot.comparisons
import chatterbot.response_selection

import os

def get_yaml_files(directory):
    # Get all YAML files in the specified directory
    return [f for f in os.listdir(directory) if f.endswith('.yml')]

## initialize chatter bot
bot = ChatBot(
    'robot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    preprocessors=[
        'chatterbot.preprocessors.clean_whitespace',
    ],
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.BestMatch'
    ],
    database_uri='sqlite:///database.db',
    read_only=True
)


## training corpus list
## Disable these two lines below AFTER first run when a *.db file is generated in project directory
trainer = ChatterBotCorpusTrainer(bot)

# Train the chatbot on custom datasets in language folders
data_path = 'data/'
for language_folder in os.listdir(data_path):
    language_path = os.path.join(data_path, language_folder)
    if os.path.isdir(language_path):
        yaml_files = get_yaml_files(language_path)
        for yaml_file in yaml_files:
            file_path = os.path.join(language_path, yaml_file)
            # print(file_path)
            trainer.train(file_path)

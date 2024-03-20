from openai import OpenAI
import json
import openai
import os


OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
client = OpenAI(api_key=OPENAI_API_KEY)

def create_assistant(client):
    assistant_file_path = 'assistant.json'
  
    if os.path.exists(assistant_file_path):
        with open(assistant_file_path, 'r') as file:
            assistant_data = json.load(file)
            assistant_id = assistant_data['assistant_id']
            print("Loaded existing assistant ID.")
    else:
        file = client.files.create(file=open("marketing_expenses.docx", "rb"),
                               purpose='assistants')
  
        assistant = client.beta.assistants.create(
            instructions="You are an assistant bot, and you have access to files to answer employee questions about marketing expenses of the current month.",
            name="Marketing_expense Helper",
            tools=[{"type": "retrieval"}],
            model="gpt-4-turbo-preview",
            file_ids=[file.id],    
        )   

        with open(assistant_file_path, 'w') as file:
            json.dump({'assistant_id': assistant.id}, file)
            print("Created a new assistant and saved the ID.")
            
        assistant_id = assistant.id
        
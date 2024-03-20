import functions
import time
import json
import os
import openai
from packaging import version


OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]

required_version = version.parse("1.1.1")
current_version = version.parse(openai.__version__)

print("Checking version compatibility...")
time.sleep(2)

if current_version < required_version:
    raise ValueError(f"Incompatible version {current_version}")
else:
    print("compatible version")    

client = openai.OpenAI(api_key=OPENAI_API_KEY)

time.sleep(2)
print("Checking the existence of an assistant or creating a new one")
time.sleep(2)


assistant_id = functions.create_assistant(client)
time.sleep(2)


def start_conversation():
    print("Starting a new conversation...")
    time.sleep(2)
    print("Checking the existence of thread or creating one...")
    time.sleep(2)
    thread_file_path = 'thread.json'
    if os.path.exists(thread_file_path):
        with open(thread_file_path, 'r') as file:
            thread_data = json.load(file)
            thread_id = thread_data['thread_id']
            print("Loaded existing thread ID.")
    else:
        thread = client.beta.threads.create()
        thread_id = thread.id
        print(f"New thread created with ID: {thread.id}")

        with open(thread_file_path, 'w') as file:
            json.dump({'thread_id': thread_id}, file)
            print("Created a new thread and saved the ID.")

        thread_id = thread.id
  
    client.beta.threads.messages.create(thread_id=thread_id,
                                      role="user",
                                      content="Great. Now, what are the CRM expenses?")

  
    run = client.beta.threads.runs.create(thread_id=thread_id,
                                        assistant_id="asst_7P9gtuEnqx4PBXm3Fpnx8kCS")
    
    while True:
        run_status = client.beta.threads.runs.retrieve(thread_id=thread_id,
                                                   run_id=run.id)
    
        if run_status.status == 'completed':
            break

    messages = client.beta.threads.messages.list(thread_id=thread_id)
    response = messages.data[0].content[0].text.value

    print(f"Assistant response: {response}")

start_conversation()






import pymongo
import os

from google import genai
from google.genai import types
from dotenv import load_dotenv
from utils import retrieve_context

if __name__ == '__main__':
    load_dotenv()

    google_client = genai.Client(api_key=os.getenv("GEMINI"))

    uri = os.getenv("MONGODB_URI")
    mongo_client = pymongo.MongoClient(uri, 
                                       server_api=pymongo.server_api.ServerApi(
                                       version="1", 
                                       strict=False, 
                                       deprecation_errors=True))
    
    Prakharbase = mongo_client["Prakharbase"]
    vector_database = Prakharbase["vector_database"]

    with open('system_prompt.txt', 'r') as file:
        system_prompt = file.read()
        
    chat = google_client.chats.create(model="gemini-2.0-flash",
                                      config=types.GenerateContentConfig(
                                          system_instruction=system_prompt))

    print(f"PrakharGaming: Hi, my name is PrakharGaming, I am an LLM based on Google Gemini 2.0 Flash and I'm here to answer questions about Prakhar's software engineering background! How can I help you?\n")
    while True:
        user_input = input("You: ")
        if user_input == "EXIT":
            print("Goodbye.")
            break
        
        context = retrieve_context(google_client, vector_database, user_input)
        response = chat.send_message(f"Context: {context} \n Query: {user_input} \n")
        print(f"\nPrakharGaming: {response.text}\n")



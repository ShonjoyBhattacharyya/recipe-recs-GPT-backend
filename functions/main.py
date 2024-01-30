import openai
import os
from firebase_functions import firestore_fn, https_fn
import json 

openai.api_key = "OPEN-AI-KEY"


# Initialize Firebase Admin
# Assuming firebase_admin has been initialized in your project

# OpenAI API key setup

@https_fn.on_request()
def chat(req: https_fn.Request) -> https_fn.Response:
    try:
        # Get the prompt from the URL query parameter
        request_args = req.args
        prompt = request_args.get('prompt', '') if request_args else 'give me a motivational quote'

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Specify the model
            messages=[{"role": "system", "content": "You are a helpful assistant."},
                      {"role": "user", "content": prompt}],
            max_tokens=50
        )

        # Send response back
        return https_fn.Response(json.dumps({"reply": response.choices[0].message["content"]}), 
                                 status=200, 
                                 headers={"Content-Type": "application/json"})
    except Exception as e:
        return https_fn.Response(json.dumps({"error": str(e)}), 
                                 status=500, 
                                 headers={"Content-Type": "application/json"})


import json
from firebase_admin import credentials, initialize_app
from flask import Flask, request, jsonify
from openai import OpenAIApi

cred = credentials.Certificate('path/to/your/firebase-service-account.json')
initialize_app(cred)

app = Flask(__name__)

# Initialize OpenAI API
openai = OpenAIApi('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')

@app.route('/generateMotivationalQuote', methods=['POST'])
def generate_motivational_quote():
    request_data = request.get_json()
    prompt = request_data['prompt']

    try:
        response = openai.create_completion(
            engine='davinci',
            prompt=prompt,
            max_tokens=50  # Adjust based on your desired response length
        )

        quote = response['choices'][0]['text']
        return jsonify({'quote': quote}), 200
    except Exception as e:
        print(str(e))
        return jsonify({'error': 'Failed to generate a quote.'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

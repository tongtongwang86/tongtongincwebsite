# dependencies: pip3 install flask
from flask import Flask, request, send_file
from flask_cors import CORS
from pathlib import Path
from gpt4all import GPT4All
import threading



app = Flask(__name__)
CORS(app)
@app.route('/api/text-gen', methods=['OPTIONS'])
def handle_preflight():
    response_headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'POST',
        'Access-Control-Allow-Headers': 'Content-Type',
    }
    return ('', 204, response_headers)

lock = threading.Lock()
@app.route('/api/text-gen', methods=['POST'])

def receive_text():

    with lock:
        data = request.json

        if 'simplegen' in data:

            Prompt = data["simplegen"]["prompt"]

            
            
            model_name = 'mistral-7b-openorca.Q4_0.gguf'
            model_path = Path('D:\\System\\Models')

            model = GPT4All(model_name, model_path, device='gpu')


            with model.chat_session():
                tokens = []
                output = model.generate(Prompt, max_tokens=500)
                return (output)
                
            
            
            
            return jsonify(output)
            
        else:
            return {'error': 'Text field not found in request'}, 400

if __name__ == '__main__':
    app.run(host='192.168.124.20', port=5000, debug=True)

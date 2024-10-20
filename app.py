from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Route to display the HTML form
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submission
@app.route('/send-command', methods=['POST'])
def send_command():
    data = request.json
    command = data['command']
    
    # You can send this command to your Telegram bot here
    # Example to send a message to Telegram (you'll replace this with your bot token and chat ID)
    bot_token = '7276766433:AAEsEm032tZrX5JN-T1o5lUuIorTBMgKx7M'
    chat_id = '1086318600'
    telegram_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    
    payload = {
        'chat_id': chat_id,
        'text': command
    }
    
    requests.post(telegram_url, json=payload)

    return jsonify({"message": "Command sent successfully!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
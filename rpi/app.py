from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def html_page():
    return render_template('index.html')

@app.route('/send', methods=['POST'])
def send():
    number_input = request.form.get('numberInput', '')
    # Use the 'number' variable for further processing
    return 'Received number: ' + number_input

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

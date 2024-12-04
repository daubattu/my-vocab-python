from flask import Flask
from googletrans import Translator

app = Flask(__name__)

@app.route("/")
def hello_world():
 
    translator = Translator()
    
    translated = translator.translate('go', src='en', dest='vi')
    
    print(translated.text)

    return "<p>Hello, World!</p>"
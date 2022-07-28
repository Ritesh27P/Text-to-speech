from flask import Flask, redirect, render_template, request, url_for
from gtts import gTTS
import os
import PyPDF2 


def to_audio(mytext):
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    os.remove('./static/sound/sound.mp3')
    print('done compiling')
    myobj.save('./static/sound/sound.mp3')


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html', error=None)


@app.route('/convert', methods=['POST', 'GET'])
def convert():
    file = request.form.get('file')
    if file == '':
        return render_template('index.html', error='Paste your file path')
    pdfFileObj = open(str(file), 'rb') 
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
    pageObj = pdfReader.getPage(0) 
    to_audio(pageObj.extractText())
    pdfFileObj.close() 
    return render_template('convert.html')


if __name__ == '__main__':
    app.run(debug=True)
    pass

# to_audio('hii i am ritesh')
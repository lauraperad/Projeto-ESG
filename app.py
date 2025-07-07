from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    pergunta = request.form.get('pergunta')

    if file:
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)
        # Aqui você pode adicionar o código de processamento
        return f'Arquivo recebido: {file.filename}<br>Pergunta: {pergunta}'

    return 'Nenhum arquivo enviado.'

if __name__ == '__main__':
    app.run(debug=True)
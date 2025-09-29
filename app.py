from flask import Flask, render_template, request, redirect
import os

MOVIES_FOLDER = '/home/umbrel/Downloads/movies'
MUSIC_FOLDER = '/home/umbrel/Downloads/music'

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload1', methods=['POST'])
def upload1():
    file = request.files['file']
    if file:
        os.makedirs(MOVIES_FOLDER, exist_ok=True)
        file.save(os.path.join(MOVIES_FOLDER, file.filename))
    return redirect('/')

@app.route('/upload2', methods=['POST'])
def upload2():
    file = request.files['file']
    if file:
        os.makedirs(MUSIC_FOLDER, exist_ok=True)
        file.save(os.path.join(MUSIC_FOLDER, file.filename))
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

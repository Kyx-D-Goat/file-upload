from flask import Flask, render_template, request, redirect
import os

MOVIES_FOLDER = '/home/umbrel/umbrel/home/Downloads/movies'
MUSIC_FOLDER = '/home/umbrel/umbrel/home/Downloads/music'

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload1', methods=['POST'])
def upload1():
    file = request.files['file']
    if file:
        os.makedirs(MOVIES_FOLDER, exist_ok=True)
        save_path = os.path.join(MOVIES_FOLDER, file.filename)
        print(f"Saving to: {save_path}")
        file.save(save_path)
    else:
        print("No file received in upload1")
    return redirect('/')

@app.route('/upload2', methods=['POST'])
def upload1():
    file = request.files['file']
    if file:
        os.makedirs(MUSIC_FOLDER, exist_ok=True)
        save_path = os.path.join(MUSIC_FOLDER, file.filename)
        print(f"Saving to: {save_path}")
        file.save(save_path)
    else:
        print("No file received in upload2")
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

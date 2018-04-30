from flask import Flask, request, send_from_directory, render_template
from flask_cloudy import Storage

app = Flask(__name__, static_url_path='', static_folder='', template_folder='')

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('css', path)

@app.route('/components/<path:path>')
def send_components(path):
    return send_from_directory('components', path)

@app.route('/')
def send_index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
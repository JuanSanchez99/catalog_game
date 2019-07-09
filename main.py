from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    games = ['hen', 'head', 'ship', 'nn']
    return render_template('index.html', games=games)

@app.route('/game/<name>')
def game(name=None):
    return render_template(name +'.html')

if __name__ == "__main__":
    app.run(port=8003, debug=True)
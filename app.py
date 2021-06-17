from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello Word<br /> <strong>Agora a coisa vai.</strong> hehe."

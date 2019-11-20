from flask import Flask

app = Flask(__name__)

@app.route('/')

def hell() -> str:
    return 'Hello world from Flask!'

app.run()

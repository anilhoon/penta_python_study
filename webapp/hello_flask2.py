from flask import Flask
import vsearch

app = Flask(__name__)

@app.route('/')

def hell() -> str:
    return 'Hello world from Flask!'

@app.route('/vsearch4')
def do_search() -> str:
    return str(vsearch.search4letters('life, the universe, and everything', 'eiru,'))

app.run()

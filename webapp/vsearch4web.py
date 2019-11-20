from flask import Flask, render_template, request, redirect
import vsearch

app = Flask(__name__)

#@app.route('/')

#def hell() -> '302':
#    return redirect('/entry')
    #return 'Hello world from Flask!'

@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    #return str(vsearch.search4letters('life, the universe, and everything', 'eiru,'))
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    results = str(vsearch.search4letters(phrase, letters))
    return render_template('results.html', the_title=title,
                           the_phrase = phrase,
                           the_letters = letters,
                           the_results= results, )
                            
                           
                           

    # return str(vsearch.search4letters(phrase, letters))

@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Welcome to search4letters on the web!')

if __name__ == '__main__':
    app.run(debug=True)

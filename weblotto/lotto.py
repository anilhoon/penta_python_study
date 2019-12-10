from flask import Flask, render_template, request, redirect
import lottodef
import pymysql

app = Flask(__name__)

#@app.route('/')

#def hell() -> '302':
#    return redirect('/entry')
    #return 'Hello world from Flask!'

@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    ronum = request.form['ronum']
    clnum = request.form['clnum']
    title = 'Here are your results:'
    #박스에 공 담기
    Lotto_Box = lottodef.load_box_ball()
    #박스에서 공 뽑기
    LottoDic = lottodef.sel_box_ball(Lotto_Box,ronum)

    #뽑은 공 담기
    SortLottoNumCount = lottodef.lotto_sort(LottoDic)
    
    #많은 순서대로 나열 하기
    LevelLottoNum = lottodef.lotto_num_seq(SortLottoNumCount, 6)
    
    results = LevelLottoNum
    #results = str(vsearch.search4letters(ronum, clnum))
    return render_template('results.html', the_title=title,
                           the_ronum = ronum,
                           the_clnum = clnum,
                           the_lotto_row = LevelLottoNum,
                           the_results= results, )
                            
                    
@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title='Welcome to Lotto World on the web!')

@app.route('/lotto')
def lotto_his() -> 'html':

    dbconfig={'host':'127.0.0.1',
                  'port':3306,
                  'user':'lotto',
                  'password':'lottopasswd',
                  'database':'lottodb',
                  'charset':'utf8',}
    conn = pymysql.Connect(**dbconfig)
    
    with conn.cursor() as cursor:
        __SQL = """select lotto_event, lotto_date, lotto_num1,
                    lotto_num2, lotto_num3, lotto_num4,
                    lotto_num5, lotto_num6, lotto_num7 from lotto_db;"""
        cursor.execute(__SQL)
        results = cursor.fetchall()
        conn.commit()
    
    return render_template('lotto_show.html',
                           the_title='Lotto History List!',
                           the_results = results, )

if __name__ == '__main__':
    app.run(debug=True)

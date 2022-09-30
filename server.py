from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)  
app.secret_key = 'keep it secret, keep it safe'


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def post():
    session['name'] = request.form['name']
    session['city'] = request.form['city']
    session['lang'] = request.form['lang']
    session['comment'] = request.form['comment']
    return redirect('/result')

@app.route('/result')
def results():
    return render_template("result.html", name = session['name'], city = session['city'], lang = session['lang'], comment = session['comment'])



if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/entradas_carne')
def entradas_carne():
    return render_template('entradas_carne.html')

@app.route('/ec')
def ec():
    return render_template('ec.html')

@app.route('/em')
def em():
    return render_template('em.html')

@app.route('/ev')
def ev():
    return render_template('ev.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/registo')
def registo():
    return render_template('registo.html')

@app.route('/carrinho')
def carrinho():
    return render_template('carrinho.html')

if __name__ == '__main__':
    app.run(debug=True)

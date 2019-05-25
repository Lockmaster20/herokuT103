from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/entradas_carne')
def entradas_carne():
    return render_template('entradas/entradas_carne.html')

@app.route('/entradas_carne/bcf')
def bcf():
    return render_template('entradas/entradas_carne/bcf.html')

@app.route('/entradas_carne/mom')
def mom():
    return render_template('entradas/entradas_carne/mom.html')

@app.route('/entradas_carne/cr')
def cr():
    return render_template('entradas/entradas_carne/cr.html')



@app.route('/entradas_marisco')
def entradas_marisco():
    return render_template('entradas/entradas_marisco.html')

@app.route('/entradas_marisco/sgffa')
def sgffa():
    return render_template('entradas/entradas_marisco/sgffa.html')

@app.route('/entradas_marisco/cmc')
def cmc():
    return render_template('entradas/entradas_marisco/cmc.html')



@app.route('/entradas_vegetais')
def entradas_vegetais():
    return render_template('entradas/entradas_vegetais.html')

@app.route('/entradas_vegetais/fvg')
def fvg():
    return render_template('entradas/entradas_vegetais/fvg.html')

@app.route('/entradas_vegetais/pv')
def pv():
    return render_template('entradas/entradas_vegetais/pv.html')

@app.route('/entradas_vegetais/sfbs')
def sfbs():
    return render_template('entradas/entradas_vegetais/sfbs.html')

@app.route('/entradas_vegetais/wa')
def wa():
    return render_template('entradas/entradas_vegetais/wa.html')

@app.route('/entradas_vegetais/bgb')
def bgb():
    return render_template('entradas/entradas_vegetais/bgb.html')



@app.route('/sobremesas_caramelo')
def sobremesas_caramelo():
    return render_template('sobremesas/sobremesas_caramelo.html')

@app.route('/sobremesas_caramelo/sbctcs')
def sbctcs():
    return render_template('sobremesas/sobremesas_caramelo/sbctcs.html')



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

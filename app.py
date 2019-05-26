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



@app.route('/prato_principal_carne')
def prato_principal_carne():
    return render_template('prato_principal/prato_principal_carne.html')

@app.route('/prato_principal_carne/cp_carne')
def cp_carne():
    return render_template('prato_principal/prato_principal_carne/cp_carne.html')

@app.route('/prato_principal_carne/fcb')
def fcb():
    return render_template('prato_principal/prato_principal_carne/fcb.html')



@app.route('/prato_principal_peixe')
def prato_principal_peixe():
    return render_template('prato_principal/prato_principal_peixe.html')

@app.route('/prato_principal_peixe/beca')
def beca():
    return render_template('prato_principal/prato_principal_peixe/beca.html')

@app.route('/prato_principal_peixe/cp_peixe')
def cp_peixe():
    return render_template('prato_principal/prato_principal_peixe/cp_peixe.html')

@app.route('/prato_principal_peixe/cs')
def cs():
    return render_template('prato_principal/prato_principal_peixe/cs.html')



@app.route('/prato_principal_marisco')
def prato_principal_marisco():
    return render_template('prato_principal/prato_principal_marisco.html')

@app.route('/prato_principal_marisco/lspmml')
def lspmml():
    return render_template('prato_principal/prato_principal_marisco/lspmml.html')

@app.route('/prato_principal_marisco/pa')
def pa():
    return render_template('prato_principal/prato_principal_marisco/pa.html')



@app.route('/prato_principal_arroz')
def prato_principal_arroz():
    return render_template('prato_principal/prato_principal_arroz.html')

@app.route('/prato_principal_arroz/aff')
def aff():
    return render_template('prato_principal/prato_principal_arroz/aff.html')



@app.route('/prato_principal_massa')
def prato_principal_massa():
    return render_template('prato_principal/prato_principal_massa.html')

@app.route('/prato_principal_massa/emt')
def emt():
    return render_template('prato_principal/prato_principal_massa/emt.html')

@app.route('/prato_principal_massa/ppts')
def ppts():
    return render_template('prato_principal/prato_principal_massa/ppts.html')



@app.route('/prato_principal_batatas')
def prato_principal_batatas():
    return render_template('prato_principal/prato_principal_batatas.html')

@app.route('/prato_principal_batatas/esbdb')
def esbdb():
    return render_template('prato_principal/prato_principal_batatas/esbdb.html')



@app.route('/sobremesas_caramelo')
def sobremesas_caramelo():
    return render_template('sobremesas/sobremesas_caramelo.html')

@app.route('/sobremesas_caramelo/sbctcs')
def sbctcs():
    return render_template('sobremesas/sobremesas_caramelo/sbctcs.html')



@app.route('/sobremesas_chocolate')
def sobremesas_chocolate():
    return render_template('sobremesas/sobremesas_chocolate.html')

@app.route('/sobremesas_chocolate/bacb')
def bacb():
    return render_template('sobremesas/sobremesas_chocolate/bacb.html')

@app.route('/sobremesas_chocolate/bbd')
def bbd():
    return render_template('sobremesas/sobremesas_chocolate/bbd.html')

@app.route('/sobremesas_chocolate/pmc')
def pmc():
    return render_template('sobremesas/sobremesas_chocolate/pmc.html')

@app.route('/sobremesas_chocolate/sf')
def sf():
    return render_template('sobremesas/sobremesas_chocolate/sf.html')

@app.route('/sobremesas_chocolate/tcb')
def tcb():
    return render_template('sobremesas/sobremesas_chocolate/tcb.html')



@app.route('/sobremesas_fruta')
def sobremesas_fruta():
    return render_template('sobremesas/sobremesas_fruta.html')

@app.route('/sobremesas_fruta/fmm')
def fmm():
    return render_template('sobremesas/sobremesas_fruta/fmm.html')

@app.route('/sobremesas_fruta/lmbm')
def lmbm():
    return render_template('sobremesas/sobremesas_fruta/lmbm.html')

@app.route('/sobremesas_fruta/mmc')
def mmc():
    return render_template('sobremesas/sobremesas_fruta/mmc.html')

@app.route('/sobremesas_fruta/pfvnvb')
def pfvnvb():
    return render_template('sobremesas/sobremesas_fruta/pfvnvb.html')



@app.route('/sobremesas_queijo')
def sobremesas_queijo():
    return render_template('sobremesas/sobremesas_queijo.html')

@app.route('/sobremesas_queijo/brv')
def brv():
    return render_template('sobremesas/sobremesas_queijo/brv.html')

@app.route('/sobremesas_queijo/cc')
def cc():
    return render_template('sobremesas/sobremesas_queijo/cc.html')

@app.route('/sobremesas_queijo/pcaf')
def pcaf():
    return render_template('sobremesas/sobremesas_queijo/pcaf.html')

@app.route('/sobremesas_queijo/t')
def t():
    return render_template('sobremesas/sobremesas_queijo/t.html')



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

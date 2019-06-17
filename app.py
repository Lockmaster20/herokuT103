from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


#Base de Dados Início
def herokudb():
    Host='ec2-54-217-225-16.eu-west-1.compute.amazonaws.com'
    Database='d3qhdom2o3ji6r'
    User='dohxigdbtfncha'
    Password='f1b15ad3b66a1e2b270914be425f88e08a25d7fb540ac19a49f7749c742d2a7b'
    return psycopg2.connect(host=Host, database=Database, user=User, password=Password, sslmode='require')

def existe(v1):
    try:
        ficheiro = herokudb()
        db = ficheiro.cursor()
        db.execute("SELECT * FROM usr WHERE nome= %s", (v1,))
        valor = db.fetchone()
        ficheiro.close()
    except:
        valor=None
    return valor

def gravar(v1, v2, v3):
    ficheiro = herokudb()
    db = ficheiro.cursor()
    db.execute("CREATE TABLE IF NOT EXISTS usr (nome text, email text, passe text)")
    db.execute("INSERT INTO usr VALUES (%s, %s, %s)", (v1, v2, v3))
    ficheiro.commit()
    ficheiro.close()

@app.route('/registo', methods=['GET', 'POST'])
def route():
    erro = None
    if request.method == 'POST':
        v1 = request.form['utilizador']
        v2 = request.form['email']
        v3 = request.form['passe']
        v4 = request.form['cpasse']
        if existe(v1):
            erro = 'O utilizador já existe'
        elif v3 != v4:
            erro = 'A palavra passe não coincide.'
        else:
            gravar(v1, v2, v3)
    return render_template('registo.html', erro=erro)

def log(v1, v2):
    ficheiro = herokudb()
    db = ficheiro.cursor()
    db.execute("SELECT * FROM usr WHERE nome = %s AND passe = %s ", (v1, v2,))
    valor = db.fetchone()
    ficheiro.close()
    return valor

@app.route('/login', methods=['GET', 'POST'])
def login():
    erro = None
    if request.method == 'POST':
        v1 = request.form['utilizador']
        v2 = request.form['passe']
        if not existe(v1):
            erro = 'O utilizador não existe'
        elif not log(v1, v2):
            erro = 'O utilizador e a palavra passe não coincidem'
        else:
            erro = 'Bem-vindo.'
    return render_template('login.html', erro=erro)

def alterar(v1, v2):
    import sqlite3
    ficheiro = sqlite3.connect('db/Utilizadores.db')
    db = ficheiro.cursor()
    db.execute("UPDATE usr SET passe = %s WHERE nome= %s", (v2, v1))
    ficheiro.commit()
    ficheiro.close()

@app.route('/newpasse', methods=['GET', 'POST'])
def npasse():
    erro = None
    if request.method == 'POST':
        v1 = request.form['utilizador']
        v2 = request.form['passe']
        v3 = request.form['cpasse']
        if not existe(v1):
            erro = 'O utilizador não existe'
        if v2 != v3:
            erro = 'A palavra passe não coincide.'
        else:
            alterar(v1, v2)
    return render_template('npasse.html', erro=erro)

def apagar(v1):
    ficheiro = herokudb()
    db = ficheiro.cursor()
    db.execute("DELETE FROM usr WHERE nome= %s", (v1,))
    ficheiro.commit()
    ficheiro.close()

@app.route('/delete', methods=['GET', 'POST'])
def delete():
    erro = None
    if request.method == 'POST':
        v1 = request.form['utilizador']
        v2 = request.form['passe']
        if not existe(v1):
            erro = 'O utilizador não existe'
        elif not log(v1, v2):
            erro = 'O utilizador e a palavra passe não coincidem'
        else:
            apagar(v1)
            erro = 'Utilizador eliminado.'
    return render_template('delete.html', erro=erro)

#Base de Dados Fim

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

if __name__ == '__main__':
    app.run(debug=True)

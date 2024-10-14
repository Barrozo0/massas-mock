from flask import Flask, jsonify, render_template
from cpf_generator1 import gerar_cpf     #CPF FRESH SEGMENTO AUTORIZADO
from cnpj_generator1 import gerar_cnpj   #CNPJ BASE SEGMENTO AUTORIZADO
from cnpj_generator2 import gerar_cnpj2  #CNPJ FRESH - SEGMENTO AUTORIZADO
from cnpj_generator3 import gerar_cnpj3  #CNPJ NÃO EXISTE - SEGMENTO NÃO VALIDADO
from cnpj_generator4 import gerar_cnpj4  #CNPJ BASE SEGMENTO NÃO AUTORIZADO
from cpf_generator2 import gerar_cpf2    #CPF BASE - AUTORIZADO
from cpf_generator3 import gerar_cpf3    #CPF BASE - NÃO AUTORIZADO
from cpf_generator4 import gerar_cpf4    #CPF NÃO EXISTE - NÃO AUTORIZADO
from cpf_generator5 import gerar_cpf5    #CPF NÃO EXISTE SFA - NÃO AUTORIZADO

app = Flask(__name__)

# Rota para servir a página HTML
@app.route('/')
def index():
    return render_template('index.html')

# Rota para gerar o CNPJ BASE SEGMENTO AUTORIZADO
@app.route('/gerar-cnpj', methods=['GET'])
def gerar_cnpj_api():
    cnpj = gerar_cnpj()
    return jsonify({'cnpj': cnpj})

# Rota para gerar o CPF FRESH SEGMENTO AUTORIZADO
@app.route('/gerar-cpf', methods=['GET'])
def gerar_cpf_api():
    cpf = gerar_cpf()
    return jsonify({'cpf': cpf})

# Rota para gerar o novo tipo de CNPJ FRESH - SEGMENTO AUTORIZADO
@app.route('/gerar_cnpj2', methods=['GET'])
def gerar_cnpj2_api():
    novo_cnpj = gerar_cnpj2()
    return jsonify({'cnpj': novo_cnpj})

# Rota para gerar o novo tipo de CNPJ NÃO EXISTE - SEGMENTO NÃO VALIDADO
@app.route('/gerar_cnpj3', methods=['GET'])
def gerar_cnpj3_api():
    novo_cnpj = gerar_cnpj3()
    return jsonify({'cnpj': novo_cnpj})

# Rota para gerar o novo tipo de CNPJ BASE SEGMENTO AUTORIZADO
@app.route('/gerar_cnpj4', methods=['GET'])
def gerar_cnpj4_api():
    novo_cnpj = gerar_cnpj4()
    return jsonify({'cnpj': novo_cnpj})

# Rota para gerar o CPF BASE - AUTORIZADO
@app.route('/gerar-cpf2', methods=['GET'])
def gerar_cpf2_api():
    cpf2 = gerar_cpf2()
    return jsonify({'cpf': cpf2})

# Rota para gerar o BASE - NÃO AUTORIZADO
@app.route('/gerar-cpf3', methods=['GET'])
def gerar_cpf3_api():
    cpf = gerar_cpf3()
    return jsonify({'cpf': cpf})

# Rota para gerar o CPF NÃO EXISTE - NÃO AUTORIZADO
@app.route('/gerar-cpf4', methods=['GET'])
def gerar_cpf4_api():
    cpf = gerar_cpf4()
    return jsonify({'cpf': cpf})

# Rota para gerar o CPF NÃO EXISTE SFA - NÃO AUTORIZADO
@app.route('/gerar-cpf5', methods=['GET'])
def gerar_cpf5_api():
    cpf = gerar_cpf5()
    return jsonify({'cpf': cpf})


if __name__ == '__main__':
    app.run(debug=True)
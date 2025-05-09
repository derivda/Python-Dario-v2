from flask import Flask, render_template, jsonify

app = Flask(__name__)

VAGAS=[{

    'titulo': 'Analista de Dados',
    'localidade': 'Nampula',
    'salario': '850000',
    'descricao': 'Analista de dados para Analista de dados '
},
{

    'titulo': 'Egenheiro de Dados',
    'localidade': 'Beira',
    'salario': '80000',
    'descricao': 'Analista de dados para Analista de dados ' 
  },
   {
       
    'titulo': 'Seguransa Cybernetica',
    'localidade': 'Nacala porto',
    'salario': '850000',
    'descricao': 'Analista de dados para Analista de dados '
       
   },
       {

    'titulo': 'Gestao de Cualidades',
    'localidade': 'Maputo provincia',
    'salario': '850000',
    'descricao': 'Analista de dados para Analista de dados ' 
       }
      ]

@app.route("/")
def hello_world():
    return render_template('home.html', vagas=VAGAS)


@app.route("/vagas")
def lista_vagas():
    return jsonify(VAGAS)


    
if __name__=="__main__": 
    app.run(host='0.0.0.0', debug=True)
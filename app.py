from flask import Flask, render_template, jsonify
from database import dario_vagas_db

app = Flask(__name__)


@app.route("/")
def hello_world():
    vagas = dario_vagas_db()
    return render_template('home.html', vagas=vagas)


@app.route("/vagas")
def lista_vagas():
 vagas = dario_vagas_db()
 return jsonify(vagas)


    
if __name__=="__main__": 
    app.run(host='0.0.0.0', debug=True)
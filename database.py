from sqlalchemy import String, create_engine, text
import os


string_conexao = os.environ['db_conexao_string']
engine = create_engine("mysql+pymysql://root:QVztbzgWMXEghQAnsTsTapNoPFPfhCoH@caboose.proxy.rlwy.net:38170/railway")


  
def dario_vagas_db():
  with engine .connect() as conn:
    resultado = conn.execute(text("SELECT * FROM vagas")) 

  vagas = []
  for vaga in resultado.all():
    vagas.append(vaga._asdict())
  return vagas
 



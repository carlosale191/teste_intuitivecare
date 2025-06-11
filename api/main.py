from flask import Flask, jsonify, g, abort, send_from_directory
import sqlite3

app = Flask(__name__)
DATABASE = 'teste.db'

def get_db():
    db = getattr(g, '_database', None)  # g armazena a conexão com db
    if db is None:
        db = g._database = sqlite3.connect(DATABASE) #se não existe, é criada
        db.row_factory = sqlite3.Row
    return db

@app.teardown_appcontext  #encerra conexão pós requisições feitas
def close_connection(exception):
    db = getattr(g, '_database', None)  
    if db is not None:
        db.close()

@app.route('/registros', methods=['GET'])
def get_items():
    conn = get_db()
    cursor = conn.execute('SELECT * FROM teste_intuitive')
    rows = cursor.fetchall()
    items = [dict(row) for row in rows]
    return jsonify(items)

@app.route('/registros/<int:item_reg>', methods=['GET'])
def get_item(item_reg):
    conn = get_db()
    cursor = conn.execute('SELECT Registro_ANS, Razao_Social, Cidade FROM teste_intuitive WHERE Registro_ANS = ?', (item_reg,))
    row = cursor.fetchone()
    if row is None:
        abort(404, description="Item não encontrado")
    return jsonify(dict(row))

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

if __name__ == '__main__':
    app.run(debug=True)

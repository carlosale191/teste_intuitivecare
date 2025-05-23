import sqlite3
import pandas as pd
from pathlib import Path

CSV_FILE = Path("Relatorio_cadop.csv")
DB_PATH  = Path("teste.db")
TABLE_NAME = 'demonstracoes_contabeis'

#cria conexão
conn = sqlite3.connect(DB_PATH)

try:
    tab = pd.read_csv(
        CSV_FILE,
        sep=";",
        on_bad_lines='skip',  # ou error_bad_lines=False
        quotechar='"',
        engine='python'
    )
except pd.errors.ParserError as e:
    print(f"Erro no parser: {e}")

df = pd.DataFrame(tab)


# Salvar o DataFrame no SQLite (cria a tabela automaticamente)
df.to_sql(
    name=TABLE_NAME,       # Nome da tabela
    con=conn,              # Conexão com o banco
    if_exists='replace',   # Substitui a tabela se já existir
    index=False,           # Não incluir o índice do DataFrame
    dtype={col: 'TEXT' for col in df.columns}  # Tipos padrão (opcional)
)

conn.close()
print('pronto')
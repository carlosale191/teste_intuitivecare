# Sobre
Resolução de teste prática da Intuitive Care. Consiste nas etapas:
- Criação de um bot para web scraping que abre o Chrome no endereço, busca arquivos pdf, faz o download e depois os compacta em um zip.
- Analisar e tratar informações dos pdfs baixados, extraindo as tabelas contidas e transferindo os dados para um dataframe, salva em csv e compacta em zip.
- Criar conexão com banco de dados SQLite e transferir dados da tabela Relatorio_cadop.csv para o banco.
- API com duas rotas GET que consulta todos registros ou apenas um, seguindo o número de registro ANS. Consultas feitas via Postman.

## Tecnologias
- Python
- Selenium, Pyautogui
- Jupyter, Pandas
- Flask
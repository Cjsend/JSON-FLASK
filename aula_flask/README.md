Passo a passo para executar o servidor Flask localmente

1) Crie e ative um ambiente virtual (opcional, mas recomendado)

Windows (PowerShell):
python -m venv venv; .\venv\Scripts\Activate.ps1

macOS / Linux:
python3 -m venv venv; source venv/bin/activate

2) Instale dependências
pip install -r requirements.txt

3) Rode o servidor
python app.py

4) Teste as rotas
- Acesse: http://127.0.0.1:5000/ -> {"mensagem": "Servidor Flask ativo!"}

- Teste POST /saudar
fetch('http://127.0.0.1:5000/saudar', {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: JSON.stringify({ nome: 'Maria' })
}).then(r => r.json()).then(j => console.log(j))

- Teste POST /dobro
fetch('http://127.0.0.1:5000/dobro', {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: JSON.stringify({ numero: 7 })
}).then(r => r.json()).then(j => console.log(j))

Entrega sugerida:
- app.py
- requirements.txt
- print do teste com resposta JSON

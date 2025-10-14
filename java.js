fetch('http://127.0.0.1:5000/saudar', {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: JSON.stringify({ nome: 'Maria' })
})
.then(res => res.json())
.then(dado => console.log(dado.mensagem));



fetch('http://127.0.0.1:5000/dobro', {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: JSON.stringify({ numero: 7 })
})
.then(res => res.json())
.then(dado => console.log(dado.resultado));

# 📡 Servidor HTTP em Python

## 🧠 O que é um Servidor HTTP?

Um servidor HTTP é um programa que:

Espera conexões vindas de clientes (ex.: navegador);

Recebe uma requisição HTTP;

Processa essa requisição;

Envia uma resposta HTTP de volta

HTTP significa HyperText Transfer Protocol, e é o protocolo usado na Web para trocar informações.


<img width="967" height="339" alt="image" src="https://github.com/user-attachments/assets/32993f0d-d098-45e1-ab97-d3b0cc923893" />


## 🛰 Como funciona a comunicação HTTP?

### 📌 1. Você abre um navegador e digita:

http://localhost:8080

O navegador então:

Cria uma conexão TCP com o servidor na porta 8080.

Envia uma requisição HTTP parecida com:

<img width="316" height="138" alt="image" src="https://github.com/user-attachments/assets/312c24fc-01f6-4177-8315-6361a5e47740" />

## 🔍 Como funciona uma requisição GET?

Quando você abre um navegador e acessa:

acontece isto:

O navegador abre uma conexão TCP com o servidor.

Ele envia uma requisição HTTP parecida com esta:

GET / HTTP/1.1
Host: localhost:8080
User-Agent: ...

Essa é a famosa requisição GET, usada para pedir um recurso (uma página, por exemplo).

O servidor lê essa requisição e responde com algo assim:

HTTP/1.1 200 OK
Content-Type: text/plain
Content-Length: 13

Olá Mundo!!!


O navegador recebe a resposta, interpreta e exibe o conteúdo.

## 🧩 Como o código faz tudo isso?

O código implementa um servidor HTTP na unha, usando apenas socket:

### 🔌 1. Criando o servidor TCP

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)


socket.AF_INET → IPv4

socket.SOCK_STREAM → TCP

bind → diz onde o servidor vai rodar

listen → começa a esperar conexões

### 📞 2. Aceitando conexões

conn, addr = server.accept()


O servidor bloqueia aqui e espera um cliente conectar.
Quando o navegador conecta, addr tem IP + porta do cliente.

### 📥 3. Lendo a requisição HTTP

<img width="354" height="61" alt="image" src="https://github.com/user-attachments/assets/f7dc0567-2d8e-4cff-977c-ec47c29fc70d" />

pega os dados enviados pelo cliente (o navegador).

A primeira linha normalmente será:

GET / HTTP/1.1

📤 4. Enviando a resposta HTTP

<img width="339" height="185" alt="image" src="https://github.com/user-attachments/assets/524f95be-2f98-4882-b37c-53d3106906a5" />


Sua resposta contém:

Status Line → HTTP/1.1 200 OK

Headers → tipo do conteúdo e tamanho

Linha em branco → separa cabeçalho do corpo

Corpo da resposta → texto "Olá Mundo!!!"

Depois envia tudo:

conn.sendall(response.encode())
conn.close()

🎯 Resultado final

Quando o navegador acessa http://localhost:8080:

Ele envia um GET.

Seu servidor lê.

Responde com "Olá Mundo!!!".

O navegador exibe isso na tela.

# 🏁 Conclusão

Este projeto demonstra, de forma simples e direta, como funciona um servidor HTTP por dentro, sem o uso de frameworks. Através de sockets TCP, o código recebe conexões, interpreta a requisição enviada pelo navegador (especialmente a linha GET / HTTP/1.1) e retorna uma resposta HTTP completa, incluindo status, cabeçalhos e corpo.

Com isso, fica evidente como navegadores e servidores se comunicam por meio do protocolo HTTP, reforçando conceitos fundamentais como métodos (GET), cabeçalhos, conexão TCP e formatação correta da resposta.

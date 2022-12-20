# *lampada*

## O que é **lampada**?

**lampada** é um projeto relacionado à matéria de PROJETOS DE ENGENHARIA I.
Simplesmente faz uma lampada conectada com um arduino ser acionada apartir da interação com um site.

Acesse: [votala.com.br](http://votala.com.br)


## Como instalar?
Tendo um servidor vps(acessível) de "qualquer distro" rodando na núvem, acesse-o com o comando:
`$ssh root@<o ip do seu servidor aqui>`
Ele precisa ter o docker instalado.
Clone este repositório e configure TODOS OS SEGUINTES TÓPICOS:

- Arduino
- Backend
- Frontend

### Instalar o código do Arduino

Abra o arquivo `para_o_arduino/para_o_arduino.ino` na ArduinoIDE ou semelhante.
Grave-o no seu microcontrolador que precisa ser compatível com a própria IDE.

Além disso, quando quiser que o microcontrolador sincronize o estado da lampada física rodando o
script `ard.py`.


### Instalar o código do Backend

**Mova** a pasta `para_o_servidor/` para o seu servidor para a pasta que deseja.
Tomaremos como exemplo uma pasta fictícia chamada `projeto` que pertence à pasta home do usuário atual.

Execute:
```
scp -r ./para_o_servidor usuario@ip_do_servidor:projeto
```

Depois de ter copiado, construa a imagem que será *deployada*.
Rotularemos a imagem resultante como `lampada-backend` quando estiver dentro do servidor
na pasta do projeto:
```
cd backend
docker build . -t lampada-backend
```

Para por o backend no ar, devemos executar o seguinte código:
```
docker run -d -p 8080:8080 lampada-backend
```

### Instalar o código do frontend.
Estando na pasta `projeto`:
```
cd frontend
docker build . -t lampada-frontend
```
Para por o frontend no ar, devemos executar o seguinte código:
```
docker run -d -p 8080:80 lampada-frontend
```

## Como funciona?
O sistema completo depende de algums pontos principais:
- Conexão com o arduino
- Backend
- Frontend

### Conexão com o arduino
O arduino pode se dizer que quando gravado o código de conexão `para_o_arduino.ino` no microcontrolador, 
o próprio se torna um leitor da porta serial que por sua vez é constantemente atualizado pelo backend.
Ou seja, ele recebe as informações sobre o estado da lâmpada e transforma a informação recebida em
comportamento desligando ou ligando o led conectado no arduino.
O código está bastante comentado, limpo e simples de entender, recomendo bastante conferir pelo próprio código fonte como funciona.

### Backend
É bastante complexo se comparado com os requisitos mínimos para realização da disciplina porém
apesar de a construção ter sido um tanto exótica, seu funcionamento/conceito é simples.


Ele ouve clientes websockets e altera o estado de uma variável interna que representa o estado lógico da lâmpada conforme o que foi alterado no website e notifica a todos os clientes conectados os estado atual quando isso acontecer.

Simplificando:

- *Cliente 1* conecta e é informado do estado atual da lâmpada(por exemplo:desligada).
- *Cliente 1* altera o estado(lampada liga tanto no arduino quanto no website).
- Todos os clientes *(Cliente 1)* é informado do estado atual da lâmpada(ligada).
- *Cliente 2* conecta é informado do estado atual da lâmpada(ligada).
- *Cliente 2* altera o estado(lampada desliga no site e no arduino).
- Todos os clientes *(Cliente 1 e Cliente 2)* são informados do estado atual da lâmpada(desligada).

# Agradecimentos
Agradecemos a todos os colaboradores do projeto, àos voluntários que tiveram coragem de testar o nosso site.

#### Desenvolvedores
Todos os envolvidos na elaboração foram bastante assíduos em colaborar com o projeto como um todo porém vale destacar a especialidade de cada um:
- Lucas Sousa Silva
- Dayvison Lima
- Alexsander Nunes Bezerra


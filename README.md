# *lampada*

## O que é **lampada**?

**lampada** é um projeto relacionado à matéria de PROJETOS DE ENGENHARIA I.
Simplesmente faz uma lampada conectada com um arduino ser acionada apartir da interação com um site.

## Como instalar?
Tendo um servidor vps(acessível) de "qualquer distro" rodando na núvem, acesse-o com o comando:
`$ssh root@<o ip do seu servidor aqui>`
Clone este repositório e 

## Como funciona?
O sistema completo depende de algums pontos principais:
- Arduino
- Servidor
- Website

### Arduino
Para acendermos a lâmpada no Arduino, precisamos que o arduino esteja gravado com o código
que está na pasta `para_o_arduino` pela própria ArduinoIDE ou semelhante.

### Servidor
Instalar o container que está dentro da pasta `para_o_servidor` através de um comando
```
docker build .
docker run 
```



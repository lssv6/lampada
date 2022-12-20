var lampada = "DESCONECTADO";

function esconder(elementos){
  elementos.forEach(elemento => {
    try{
      elemento.setAttribute("hidden", true);
    }catch(e){
      console.error(e)
    }
  });
}

function mostrar(elemento){
  elemento.attributes.removeNamedItem("hidden");
}

function mudar(estado){
  let on = document.getElementById("lamp_on");
  let off = document.getElementById("lamp_off");
  let des = document.getElementById("desconectado");
  esconder([on,off,des]);
  if (estado === "LIGADA"){
    mostrar(on);
  }else if (estado === "DESLIGADA") {
    mostrar(off);
  }else if (estado === "DESCONECTADO"){
    mostrar(des);
  }
}


window.onload = () => {

  // Faz com que inicialize o estado da lampada como desconectado.
  mudar(lampada);
  
  // Objeto websocket para manipulação de dados.
  var ws = new WebSocket("ws://votala.com.br:8080");

  // Quando clicar na lampada: Tenta mandar dados ao servidor
  document.querySelector("div.lamp").onclick = () => {
    ws.send("L");
  };

  ws.onopen = () => {
    console.log("Conectado!!!");
  }

  ws.onmessage = (event) => {
    lampada = event.data;
    console.log(lampada);
    console.log("Estado atual da lâmpada: "+ lampada);
    mudar(lampada);
  }

  // Quando houver erros
  var err = () =>{
    console.log("Alguma coisa errada aconteceu.");
    lampada = "DESCONECTADO";
    mudar(lampada);
  }

  ws.onclose = err;
  ws.onerror = err;
}

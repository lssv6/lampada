"""Este código faz com que seus clientes consultem ou alterem o estado de uma lâmpada """
import asyncio, uuid, websockets
async def spammar_novo_estado():
    global CLIENTES, LAMPADA
    for websocket in CLIENTES.values():
        try:
            await websocket.send(LAMPADA)
        except Exception as e: 
            print(e)


LAMPADA = "DESLIGADA"
CLIENTES = {}


async def ouvinte(websocket):
    """Escuta o usuário. Caso queira mudar o valor da lampada"""
    global LAMPADA, CLIENTES
    identificacao = str(uuid.uuid4())
    CLIENTES[identificacao] = websocket  # gerenciamento de memória?
    
    print(f"Entrou algum usuário codigo={identificacao}")
    await websocket.send(LAMPADA)
    async for mensagem in websocket:
        print(f"{identificacao} --mandou--> {mensagem=}")
        if mensagem == "L":
            print(f"Mudando de {LAMPADA} para ", end="")
            LAMPADA = "LIGADA" if LAMPADA == "DESLIGADA" else "DESLIGADA"
            print(f"{LAMPADA}")
            await spammar_novo_estado()

        else:
            await websocket.send(LAMPADA)
    del CLIENTES[identificacao]


async def main():
    async with websockets.serve(ouvinte, "0.0.0.0", 8080):
        print("Rodando app com websockets")
        await asyncio.Future()


asyncio.run(main())


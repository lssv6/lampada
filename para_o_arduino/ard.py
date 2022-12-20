""" MODULO """
import asyncio, serial
from traceback import print_stack
from websockets import connect

try:
    ser = serial.Serial('/dev/ttyUSB0')
except Exception as e:
    print_stack(e)

URI = "ws://votala.com.br:8080"

async def hello(uri):
    print("---PROGRAMA DE CONEXÃO COM ARDUINO---")
    print(f"Conectando com {URI=} ...")
    async with connect(uri) as websocket:
        print("Conectado !!!")
        while True:
            letra = bytes((await websocket.recv())[0], "ascii")
            print(f"Letra recebida ={letra}")
            ser.write(letra)


asyncio.run(hello(URI))

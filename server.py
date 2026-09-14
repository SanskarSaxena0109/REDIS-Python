import asyncio
from database import Database
from parser import RESPParser
from router import CommandRouter

db=Database()
router=CommandRouter(db)    

async def handle_client(reader,writer):
    try:

        while True:
            command_parts=await RESPParser.decode(reader)
            if command_parts is None:
                break
            print(f"DEBUG PARSED TOKENS: {command_parts}")
            response=router.execute(command_parts)
            encoded_response=RESPParser.encode(response)
            writer.write(encoded_response)
            await writer.drain()
    except asyncio.CancelledError:
        pass
    finally:
        print("Client Disconnected")
        writer.close()
        await writer.wait_closed()

async def main():
    server=await asyncio.start_server(handle_client,'127.0.0.1',6380)
    print("Redis clone server running on 127.0.0.1:6380...")
    async with server:
        await server.serve_forever()

if __name__=="__main__":
    asyncio.run(main())

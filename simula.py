from asyncio import ensure_future, gather, get_event_loop
import time
from aiohttp import ClientSession

inicio = time.time()
async def fetch(session,url):
    async with session.get(url) as response:
        return await response.json()

async def run():
    tasks = []
    async with ClientSession() as session:
        for pokemom in range(1,2):
            task = ensure_future(
                            fetch(
                                session
                                ,f"https://pokeapi.co/api/v2/pokemon/{pokemom}"
                                )
                             )
            tasks.append(task)

        responses = await gather(*tasks)
        [print(resp["id"],resp["name"]) for resp in responses] 

loop = get_event_loop()
future = ensure_future(run())
loop.run_until_complete(future)  

termino = time.time()
print(f"Tempo total da execução:{abs(int(termino - inicio))} segundos")
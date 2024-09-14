import asyncio


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    balls = 5
    for ball in range(balls):
        await asyncio.sleep(1 / power)
        print(f'Силач {name}  поднял {ball + 1} шар')
    print(f'Силач {name} закончил соревнования.')


async def start_tournament(*args):
    list_=[]
    for strongman in args:
        list_.append(asyncio.create_task(start_strongman(strongman[0], strongman[1])))
    for finish_strongman in list_:
        await finish_strongman


b = start_tournament(('Pasha', 3), ('Denis', 4), ('Apollon', 5))

asyncio.run(b)

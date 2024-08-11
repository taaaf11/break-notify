import asyncio
import time

from break_notif.utils import min_to_sec


# TODO: Use notification daemons

async def water_notif() -> None:
    while True:
        minutes = 40
        await asyncio.sleep(min_to_sec(minutes))
        print("drink water")


async def eye_20_rule() -> None:
    while True:
        minutes = 20
        await asyncio.sleep(min_to_sec(minutes))
        print("20 rule act")


async def main() -> None:
    async with asyncio.TaskGroup() as tg:
        tg.create_task(water_notif())
        tg.create_task(eye_20_rule())


def runner() -> None:
    asyncio.run(main())

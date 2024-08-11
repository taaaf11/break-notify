import asyncio
import time

from notifypy import Notify

from break_notif.utils import min_to_sec


async def water_notif() -> None:
    summary = "Drink water."
    message = "Drink half a glass of water."
    minutes = 40
    while True:
        await asyncio.sleep(min_to_sec(minutes))
        Notify(summary, message).send()


async def eye_20_rule() -> None:
    summary = "Eye care break"
    message = "Focus your eyes something 20 feet away for 20 minutes."
    minutes = 20
    while True:
        await asyncio.sleep(min_to_sec(minutes))
        Notify(summary, message).send()


async def main() -> None:
    async with asyncio.TaskGroup() as tg:
        tg.create_task(water_notif())
        tg.create_task(eye_20_rule())


def runner() -> None:
    asyncio.run(main())

import asyncio
import time

from break_notif.utils import min_to_sec


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


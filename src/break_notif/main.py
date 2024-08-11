import asyncio
import time

from notifypy import Notify

from break_notif.type import Notification
from break_notif.utils import get_notifs, min_to_sec


async def start_notif(notif: Notification) -> None:
    mins = min_to_sec(notif.timer)
    while True:
        await asyncio.sleep(mins)
        Notify(notif.heading, notif.body).send()


async def main() -> None:
    notifs = get_notifs()
    if not notifs:
        return
    async with asyncio.TaskGroup() as tg:
        for notif in notifs:
            tg.create_task(start_notif(notif))


def runner() -> None:
    asyncio.run(main())

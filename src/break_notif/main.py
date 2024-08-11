import asyncio
import sys
from argparse import ArgumentParser

from notifypy import Notify

from break_notif.type import Notification
from break_notif.utils import get_notifs, min_to_sec, save_notif


async def start_notif(notif: Notification) -> None:
    mins = min_to_sec(notif.timer)
    while True:
        await asyncio.sleep(mins)
        Notify(notif.heading, notif.body).send()


async def main() -> None:
    if len(sys.argv) == 1:
        notifs = get_notifs()
        if not notifs:
            return
        async with asyncio.TaskGroup() as tg:
            for notif in notifs:
                tg.create_task(start_notif(notif))

    parser = ArgumentParser(prog="bnotify", description="A lightweight break notifier.")
    parser.add_argument(
        "-c",
        "--create",
        action="store_true",
        help="Create a notification (data). Note that options e, b, t and i have no effect without this option.",
    )
    parser.add_argument("-e", "--heading", type=str, help="Heading of notification.")
    parser.add_argument("-b", "--body", type=str, help="Body of notification.")
    parser.add_argument(
        "-t",
        "--timer",
        type=int,
        help="Time (in minutes) after which the notification should be triggered.",
    )
    parser.add_argument(
        "-i", "--icon", type=str, help="Path to file containing icon for notification."
    )

    args = parser.parse_args()

    if args.create:
        heading = args.heading
        body = args.body
        timer = args.timer
        icon = args.icon

        margs_present = all((heading, body, timer))

        if margs_present:
            notif = Notification(heading, body, timer, icon)
            save_notif(notif)
        else:
            print(
                "bnotify: create argument requires heading, body and timer arguments to be specified. Icon argument is optional"
            )


def runner() -> None:
    asyncio.run(main())

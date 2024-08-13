import asyncio
import sys
from argparse import ArgumentParser

from notifypy import Notify

from renotify.type import Notification
from renotify.utils import get_notifs, min_to_sec, save_notif


async def start_notif(notification: Notification) -> None:
    mins: int = min_to_sec(notification.timer)
    notify = Notify()
    notify.title = notification.heading
    notify.message = notification.body
    if notification.icon:
        notify.icon = notification.icon
    if notification.sound:
        notify.audio = notification.sound
    while True:
        await asyncio.sleep(mins)
        notify.send()


async def main() -> None:
    if len(sys.argv) == 1:
        notifs: list[Notification] = get_notifs()
        if not notifs:
            return
        async with asyncio.TaskGroup() as tg:
            for notif in notifs:
                tg.create_task(start_notif(notif))

    parser = ArgumentParser(prog="renotify", description="A lightweight break notifier.")
    parser.add_argument(
        "-c",
        "--create",
        action="store_true",
        help="Create a notification (data). Options e, b, t and i have no effect without this option.",
    )
    parser.add_argument("-e", type=str, help="Heading of notification.")
    parser.add_argument("-b", type=str, help="Body of notification.")
    parser.add_argument(
        "-t",
        type=int,
        help="Time (in minutes) after which the notification should be triggered.",
    )
    parser.add_argument(
        "-i", type=str, help="Path to file containing icon for notification."
    )

    parser.add_argument(
        "-s", type=str, help="Path to sound file to play when notification arrives."
    )

    args = parser.parse_args()

    if args.create:
        heading = args.e
        body = args.b
        timer = args.t
        icon = args.i
        sound = args.s

        # check presence of mandatory args
        margs_present = all((heading, body, timer))

        if margs_present:
            notif = Notification(heading, body, timer, icon, sound)
            save_notif(notif)
        else:
            print(
                "bnotify: create argument requires heading, body and timer (e,b and t) arguments to be specified.\n"
                "Icon and sound (i and a) argument is optional"
            )


def runner() -> None:
    asyncio.run(main())

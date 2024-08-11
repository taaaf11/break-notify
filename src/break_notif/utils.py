import os
import json

from break_notif.type import Notification


HOME_PATH = os.environ["HOME"]
DF_PATH = f"{HOME_PATH}/Documents/notifs.json"  # data file path

create_empty_file = lambda filename: open(filename, "w").close()
create_missing_datafile = lambda: create_empty_file(DF_PATH) if not os.path.isfile(DF_PATH) else 0


def get_notifs() -> list[Notification]:
    create_missing_datafile()
    notifs = []
    with open(DF_PATH) as f:
        notifs_data = json.load(f)
        if not notifs_data:
            return []

    for heading, other_data in notifs_data.items():
        body = other_data.get("body")
        icon = other_data.get("icon")
        timer = other_data.get("timer")
        notif = Notification(heading, body, timer, icon)
        notifs.append(notif)
    return notifs


def save_notif(notif: Notification) -> None:
    with open(DF_PATH) as f:
        notifs_data = f.read()
    notifs_data[notif.heading] = {"body": notif.body, "timer": notif.timer}
    with open(DF_PATH, "w") as f:
        notifs_data = json.dumps(notifs_data, indent=4)
        f.write(notifs_data)


def min_to_sec(minutes: float) -> float:
    return minutes * 60

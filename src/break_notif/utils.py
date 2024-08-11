import json
import os

from break_notif.type import Notification

HOME_PATH = os.environ["HOME"]
DF_PATH = f"{HOME_PATH}/Documents/notifs.json"  # data file path

_create_empty_file = lambda filename: open(filename, "w").close()
_create_missing_datafile = (
    lambda: _create_empty_file(DF_PATH) if not os.path.isfile(DF_PATH) else 0
)


def get_notifs() -> list[Notification]:
    _create_missing_datafile()
    notifs = []
    with open(DF_PATH) as f:
        notifs_data = json.load(f)
        if not notifs_data:
            return []

    for heading, other_data in notifs_data.items():
        body = other_data.get("body")
        timer = other_data.get("timer")
        icon = other_data.get("icon")
        sound = other_data.get("sound")

        notif = Notification(heading, body, timer, icon, sound)
        notifs.append(notif)
    return notifs


def save_notif(notif: Notification) -> None:
    with open(DF_PATH) as f:
        notifs_data = json.load(f)
    notifs_data[notif.heading] = {"body": notif.body, "timer": notif.timer, "icon": notif.icon, "sound": notif.sound}
    with open(DF_PATH, "w") as f:
        notifs_data = json.dumps(notifs_data, indent=4)
        f.write(notifs_data)


def min_to_sec(minutes: float) -> float:
    return minutes * 60

import json
import os

from break_notif.type import Notification

HOME_PATH = os.environ["HOME"]
DF_DIR = f"{HOME_PATH}/Documents"
DF_PATH = f"{DF_DIR}/notifs.json"  # data file path


def _create_empty_file(filename: str) -> None:
    open(filename, "w").close()


def _create_missing_paths() -> None:
    """Create missing files and directories"""
    if not os.path.isdir(DF_DIR):
        print(f"Creating {DF_DIR} directory for saving notifications data file...")
        os.mkdir(DF_DIR)
    if not os.path.isfile(DF_PATH):
        print(f"Creating {DF_PATH} file for saving notifications data...")
        _create_empty_file(DF_PATH)


def get_notifs() -> list[Notification]:
    _create_missing_paths()
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
    notifs_data[notif.heading] = {
        "body": notif.body,
        "timer": notif.timer,
        "icon": notif.icon,
        "sound": notif.sound,
    }
    with open(DF_PATH, "w") as f:
        notifs_data = json.dumps(notifs_data, indent=4)
        f.write(notifs_data)


def min_to_sec(minutes: float) -> float:
    return minutes * 60

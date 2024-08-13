# renotify
A tool for repeatedly creating a notification. This started as a project for notifying for breaks. Now it has become a repeating notifier. (More in history.)


## Installation
1. Clone the repo or download zip.
2. Change directory to the project root.
3. Run: `pip install .`


## Usage
- Create a notification:
```bash
renotify -c -e notification-heading -b notification-body -t 1
```
This will create data for a notification with heading as "notification-heading" and body as "notification-body".
The notification will arrive after 1 minute.

- Start the notifier:
```bash
renotify
```

- More with:
```bash
renotify -h
```


## History
I wanted to write a simple break notifier, which would repeatedly tell me to do two things,
drink water and 20 minute rule for eyes care. The project did not seem too interesting,
as the user would have to hardcode functions into the source file to get notification.
So I decided to make it more approachable, and allowed for notifications' data be written
in a json file. The result is this.


## Author
Muhammad Altaaf (taafuuu@gmail.com)

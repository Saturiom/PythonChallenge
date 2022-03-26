import abc


statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
    "Douglas": "online"
}


def online_count(d):
    online = 0
    for x in statuses:
        if statuses[x] == "online":
            online += 1

    return print(online)


online_count(statuses)

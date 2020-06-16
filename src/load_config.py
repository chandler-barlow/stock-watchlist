import json
def start():
    with open("../config.json") as json_file:
        data = json.load(json_file)
        conf = {
                "options":
                {
                    "delay": data["options"]["delay"]
                },
                "watchlist": data["watchlist"]
                }
    return conf

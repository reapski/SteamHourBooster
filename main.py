import ctypes
import datetime
import os

import steam.client
import steam.enums.common

with open("config", "r") as f:
    config = f.read().split("\n")
    account = config[0].split(":")
    games = list(map(int, [x.strip() for x in set(config[1].split(",")) if x.strip() != "" and x.strip().isdigit()]))

os.system("title Steam Hour Booster")
client = steam.client.SteamClient()
client.cli_login(account[0], account[1])
client.change_status(persona_state=1)
client.games_played(games)
os.system("cls")

start = datetime.datetime.now()
while True:
    if ctypes.windll.user32.GetAsyncKeyState(0x1B):
        break
    else:
        current_time = ".".join(str(datetime.datetime.now() - start).replace(":", ".").split(".")[:-1])
        os.system(f"title Steam Hour Booster - {client.user.name} - {current_time}")
        print(f"\r[Steam Hour Booster] -> Username: [{client.user.name}] | Boosting For: [{current_time}]", end="")

client.logout()
client.disconnect()

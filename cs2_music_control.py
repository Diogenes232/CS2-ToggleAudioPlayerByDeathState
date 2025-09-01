from flask import Flask, request, abort
import time, keyboard

AUTH_TOKEN = "supersecret"  # must match the cfg file
PORT = 3000
MY_STEAMID = "ADD-STEAM-ID-HERE"

app = Flask(__name__)

is_dead = None

def set_dead(dead_now: bool):
    global is_dead
    if dead_now != is_dead:
        print("state changed; toggle music state")
        is_dead = dead_now
        waitSeconds = 3 if dead_now else 10
        
        time.sleep(waitSeconds)
        
        # toggle play/pause state
        keyboard.send("play/pause media")


@app.route("/gsi", methods=["POST"])
def gsi():
    auth = request.json.get("auth", {})
    if AUTH_TOKEN and auth.get("token") != AUTH_TOKEN:
        return "abort"

    player = request.json.get("player", {})
    if player.get("steamid") != MY_STEAMID:
        return "ignore"

    state = player.get("state", {})
    health = state.get("health")

    global was_dead
    if isinstance(health, int):
        dead_now = health <= 0
        if dead_now == False and (was_dead == None or was_dead == True):
            toggleStateAndMusic(dead_now)
        elif dead_now == True and was_dead == False:
            toggleStateAndMusic(dead_now)
    elif was_dead == False:
        toggleStateAndMusic(dead_now)

    return "ok"


if __name__ == "__main__":
    print(f"Listening on http://127.0.0.1:{PORT}/gsi")
    app.run(host="127.0.0.1", port=PORT, debug=False)


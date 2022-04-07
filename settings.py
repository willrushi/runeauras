import json

def get_user_buffs():
    with open("./custom_buffs.json", "r") as f:
        buffs = json.load(f)
    
    return buffs
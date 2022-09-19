import requests
import sys
import json

def sendMessage(token , uid, message):
    requests.post(
        url="https://api.telegram.org/bot"+token+"/sendMessage",
        data={'chat_id': uid, 'text': message}
    ).json()

with open('config.json','r') as outfile:
    config = json.load(outfile)
    token = config["token"]
    users = config["users"][0:]
    if sys.argv[1] == "add" or sys.argv[1] == "remove":
        with open('config.json','w') as f:
            if sys.argv[1] == "add":
                for user in users:
                    if user == sys.argv[2]:
                        users.remove(user)
                        print("uid {} removed".format(user))
            else:
                users.append(sys.argv[2])
                print("uid {} added".format(sys.argv[2]))
                
            data = dict()
            data["token"] = token
            data["users"] = users
            f.write(json.dumps(data, ensure_ascii=False))
    else:
        message = "地震震度{} \n即將在{}秒後抵達".format(sys.argv[1],sys.argv[2])
        for user in users:
            sendMessage(token,user,message)

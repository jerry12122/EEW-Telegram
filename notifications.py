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
    token = config[0]["token"]
    users = config[1:]
    argc = len(sys.argv)
    if argc > 2:
        message = "地震震度{} \n即將在{}秒後抵達".format(sys.argv[1],sys.argv[2])
        for i in users:
            sendMessage(token,i["uid"],message)
    else:
        with open('config.json','w') as f:
            add = 1
            for i in users:
                if i["uid"] == sys.argv[1]:
                    add = 0
                    users.remove(i)
                    print("uid {} removed".format(i["uid"]))
            if add:
                user = dict()
                user["uid"] = sys.argv[1]
                users.append(user)
                print("uid {} added".format(sys.argv[1]))
            config = [config[0]] + users
            f.write(json.dumps(config, ensure_ascii=False))

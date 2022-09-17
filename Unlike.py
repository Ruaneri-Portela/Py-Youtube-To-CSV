import json
import requests


def main(videoId, mode):
    headers = {"Github/Ruaneri-Portela": "Py-Youtube-To-CSV", }
    returnJson = requests.get(
        "https://returnyoutubedislikeapi.com/votes?videoId="+videoId, headers=headers)
    text = returnJson.text
    data = json.loads(text)
    if (mode):
        return (str(data['dislikes']))
    else:
        return (text)

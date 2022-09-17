import json, requests
def main(videoId):
 headers = {"Github/Ruaneri-Portela": "Py-Youtube-To-CSV",}
 returnJson = requests.get("https://returnyoutubedislikeapi.com/votes?videoId="+videoId,headers=headers)
 text = returnJson.text
 data = json.loads(text)
 return(str(data['dislikes']))

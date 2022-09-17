from ast import Return
import json, requests
def main(videoId):
 returnJson = requests.get("https://returnyoutubedislikeapi.com/votes?videoId="+videoId)
 text = returnJson.text
 data = json.loads(text)
 return(str(data['dislikes']))
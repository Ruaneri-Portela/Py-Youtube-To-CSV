class dataVideo:
    def getData(youtube,id,mode):  
     nextPage_token = None
     playlist_videos=[]
     listId=[]
     stats1 = []
     stats2 = []
     videos = []
     videoData = []

     if mode == 0:
       while True:
         reply= youtube.playlistItems().list(part="snippet",playlistId = id, maxResults = 500, pageToken = nextPage_token).execute()
         playlist_videos+=reply["items"]
         nextPage_token = reply.get("nestPageToken")
         if nextPage_token is None:
            break
       for i in range(0,len(playlist_videos)):
         listId.append(playlist_videos[i]["snippet"]["resourceId"]["videoId"])
     elif mode == 1:
         listId.append(id)

     for i in range(0,len(listId)):
      reply = youtube.videos().list(part="snippet",id=listId[i]).execute()
      stats1 += reply["items"]
     for i in range(0,len(listId)):
      reply = youtube.videos().list(part="statistics",id=listId[i]).execute()
      stats2 += reply["items"]
     for i in range(0,len(listId)):
      video = []
      video.append(stats1[i]["snippet"]["title"])
      video.append(stats2[i]["statistics"]["viewCount"])
      video.append(stats2[i]["statistics"]["likeCount"])
      video.append(stats2[i]["statistics"]["commentCount"])
      video.append(stats1[i]["snippet"]["publishedAt"])
      stringLink = "https://www.youtube.com/watch?v="+listId[i]
      video.append(stringLink)
      videoData.append(video)
     return videoData
    def a(youtube,idV):
      #print(youtube.capiions().list(part="statistics",id=idV).execute())
      print(youtube.captions().list(part="snippet",videoId=idV).execute())
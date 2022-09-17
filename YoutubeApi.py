import Unlike


class dataVideo:
    # Get data from video or playlist
    # This script is able to recive playlist or video ID, but need youtube login object, what as content in "Login.py"
    # The statement is "YoutubeApi" object (if can get from class object in Login.py) , ID (can be video or playlist) and mode (if Id is of playlist or video)
    def getData(youtube, id, mode, listIndex, listaVideo):
        nextPage_token = None
        playlist_videos = []
        listId = []
        stats1 = []
        stats2 = []
        stats3 = []
        videoData = []
        # To Get Data Of One Playlist (Get All Videos ID)
        print("Iniciando importação! Aguarde...")
        if mode == 0:
            while True:
                reply = youtube.playlistItems().list(part="snippet", playlistId=id,
                                                     maxResults=500, pageToken=nextPage_token).execute()
                playlist_videos += reply["items"]
                nextPage_token = reply.get("nestPageToken")
                if nextPage_token is None:
                    break
            for i in range(0, len(playlist_videos)):
                listId.append(
                    playlist_videos[i]["snippet"]["resourceId"]["videoId"])
        # Add Single Video To Get Data
        elif mode == 1:
            listId.append(id)
        # Get Part One Of Data
        tam = len(listId)
        for i in range(0, tam):
            reply = youtube.videos().list(
                part="snippet", id=listId[i]).execute()
            stats1 += reply["items"]
        # Get Part Two Of Data
        for i in range(0, tam):
            reply = youtube.videos().list(
                part="statistics", id=listId[i]).execute()
            stats2 += reply["items"]
        # Get Content Details
        for i in range(0, tam):
            reply = youtube.videos().list(
                part="contentDetails", id=listId[i]).execute()
            stats3 += reply["items"]
        # Set New List From Videos Informations
        for i in range(0, tam):
            tamCheck = len(listaVideo)
            boolCheck = False
            for l in range(0, tamCheck):
                if ((str(listId[i]) == str(listaVideo[l][8]).replace("https://youtu.be/", "")) and tamCheck > 0):
                    boolCheck = True
            if (boolCheck):
                print("Item já importado, pulando!")
            else:
                print("Importando...", i+1, "de", tam)
                video = []
                video.append(listIndex)
                video.append(stats1[i]["snippet"]["title"])
                video.append(stats2[i]["statistics"]["viewCount"])
                video.append(stats2[i]["statistics"]["likeCount"])
                video.append(Unlike.main(listId[i], True))
                video.append(stats2[i]["statistics"]["commentCount"])
                video.append(stats3[i]["contentDetails"]["duration"])
                video.append(stats1[i]["snippet"]["publishedAt"])
                stringLink = "https://youtu.be/"+listId[i]
                video.append(stringLink)
                videoData.append(video)
                listIndex = listIndex+1
        # Return List Contanin Video(s) Data!
        print("Importação completa!")
        return videoData

    def allData(youtube, idVar):
        stringReturn = ""
        reply = ""
        reply = youtube.videos().list(
            part="snippet", id=idVar).execute()
        stringReturn = stringReturn+"\n" + \
            "====================="+"\nSnippet\n"+str(reply)
        reply = youtube.videos().list(
            part="statistics", id=idVar).execute()
        stringReturn = stringReturn+"\n\n" + \
            "====================="+"\nStatistics\n"+str(reply)
        reply = youtube.videos().list(
            part="contentDetails", id=idVar).execute()
        stringReturn = stringReturn+"\n\n" + \
            "====================="+"\nContent Details\n"+str(reply)
        reply = Unlike.main(idVar, False)
        stringReturn = stringReturn+"\n\n"+"=====================" + \
            "\nAlternative Data And Unlike\n"+str(reply)
        return stringReturn

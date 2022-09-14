import YoutubeApi
import Login
def getVideos(playlistId,mode):
    youtubeImport = YoutubeApi.dataVideo
    return youtubeImport.getData(youtube,playlistId,mode)
    pass
def main():
    listVideo = []
    print("#######################\nWelcome to youtube get data pyscript")
    while True:

        comandVar = ""
        comandVar =input("#~>")

        if (comandVar == "Playlist Video") or (comandVar == "1"):
            comandVar = input("#Playlist id~>")  
            if(comandVar == "Return") or (comandVar == "9"):
                pass
            elif(comandVar == "Exit") or (comandVar == "0"):
                break
            else:
                try:
                 listVideo.extend(getVideos(comandVar,0)) 
                except:
                 print("Ocorreu um erro! Tente novamente.")

        elif (comandVar == "Single Video") or (comandVar == "2"):
            comandVar = input("#Single video id~>")  
            if(comandVar == "Return") or (comandVar == "9"):
                pass
            elif(comandVar == "Exit") or (comandVar == "0"):
                break
            else:
                try:
                 listVideo.extend(getVideos(comandVar,1)) 
                except:
                 print("Ocorreu um erro! Tente novamente.")

        elif  (comandVar == "Get Video Table") or (comandVar == "3"):
            for i in range(0,len(listVideo)):
                print(listVideo[i])

        elif (comandVar == "Export to CSV") or (comandVar == "4"):
            comandVar = input("Whats as file name? ALERT if name file exist, this file as clean overwrite\n#Export to CSV~>")
            if(comandVar == "Return") or (comandVar == "9"):
                pass
            elif(comandVar == "Exit") or (comandVar == "0"):
                break
            else:
                csv = open(comandVar+".csv","w") 
                csv.write("Titulo do Video▎Numero De Visualizações▎Numero De Gosteis▎Quantidade De Comentarios▎Data De Publicação▎Endereço Video\n")
                nonDup=NonDuplicated(listVideo)
                for i in  range(0,len(nonDup)):
                  stringLine = nonDup[i][0]+"▎"+nonDup[i][1]+"▎"+nonDup[i][2]+"▎"+nonDup[i][3]+"▎"+nonDup[i][4]+"▎"+nonDup[i][5]+"\n"
                  csv.write(stringLine)
                csv.close()

        elif (comandVar == "NIP") or (comandVar == "99"):
            comandVar = input("#NIP~>")  
            if(comandVar == "Return") or (comandVar == "9"):
                pass
            elif(comandVar == "Exit") or (comandVar == "0"):
                break
            else:
                try:
                 print(YoutubeApi.dataVideo.a(youtube,comandVar))
                except:
                 print("Ocorreu um erro! Tente novamente.")

        elif (comandVar == "Exit") or (comandVar == "0"):
            print("\nBye")
            break

        else:
            print("Comand unvaliable")
def NonDuplicated(lista):
    l = []
    for i in lista:
        if i not in l:
            l.append(i)
    return l

loginMode=None
try:
    while(True):
        loginMode=input("#")
        if(loginMode=="1"):
            break
        elif(loginMode=="2"):
            break
        else:
            print("Erro")
    youtube = Login.Auth.Main(loginMode)
    print("Login Api Ok!")
except:
    print(("Login Api not okay!"))
main()

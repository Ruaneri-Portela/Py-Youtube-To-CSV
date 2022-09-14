import YoutubeApi
import Login
#Connect To YoutubeAPI
def getVideos(playlistId,mode):
    youtubeImport = YoutubeApi.dataVideo
    return youtubeImport.getData(youtube,playlistId,mode)
#Main Script loop
def main():
    listVideo = []
    #Header
    print("#######################\nBem vindo ao importador de dados de videos e playlist do youtube")
    while True:
        #Input
        comandVar = ""
        comandVar =input("#~>")
        #Append Videos On Playlsit To List
        if (comandVar == "Ler Playlist") or (comandVar == "1"):
            comandVar = input("#Id de uma playlist~>")  
            if(comandVar == "Retornar") or (comandVar == "9"):
                pass
            elif(comandVar == "Sair") or (comandVar == "0"):
                break
            else:
                try:
                 listVideo.extend(getVideos(comandVar,0)) 
                except:
                 print("Ocorreu um erro! Tente novamente.")
        #Append Single Video To List
        elif (comandVar == "Ler Video") or (comandVar == "2"):
            comandVar = input("#Id de um video~>")  
            if(comandVar == "Retornar") or (comandVar == "9"):
                pass
            elif(comandVar == "Sair") or (comandVar == "0"):
                break
            else:
                try:
                 listVideo.extend(getVideos(comandVar,1)) 
                except:
                 print("Ocorreu um erro! Tente novamente.")
        #View Video List
        elif  (comandVar == "Mostrar lista de videos importados") or (comandVar == "3"):
            for i in range(0,len(listVideo)):
                print(listVideo[i])
        #Export To CSV File
        elif (comandVar == "Exportar dados para um arquivo") or (comandVar == "4"):
            comandVar = input("Qual o nome do arquivo? ATENÇÃO caso o arquivo exista ele vai ser substituido\n#Exportar lista~>")
            if(comandVar == "Retornar") or (comandVar == "9"):
                pass
            elif(comandVar == "Sair") or (comandVar == "0"):
                break
            else:
                csv = open(comandVar+".csv","w") 
                csv.write("Titulo▎isualizações▎Gosteis▎Comentarios▎Data De Publicação▎Link\n")
                nonDup=NonDuplicated(listVideo)
                for i in  range(0,len(nonDup)):
                  stringLine = nonDup[i][0]+"▎"+nonDup[i][1]+"▎"+nonDup[i][2]+"▎"+nonDup[i][3]+"▎"+nonDup[i][4]+"▎"+nonDup[i][5]+"\n"
                  csv.write(stringLine)
                csv.close()
        #Clean Video List Data
        elif (comandVar == "Limpar Lista") or (comandVar == "7"):
            listVideo=[]
            print("Lista limpa!")
        #Teste Only
        elif (comandVar == "Teste") or (comandVar == "99"):
            comandVar = input("#Teste~>")  
            if(comandVar == "Retornar") or (comandVar == "9"):
                pass
            elif(comandVar == "Sair") or (comandVar == "0"):
                break
            else:
                try:
                 print(YoutubeApi.dataVideo.a(youtube,comandVar))
                except:
                 print("Ocorreu um erro! Tente novamente.")
        #Exit script
        elif (comandVar == "Sair") or (comandVar == "0"):
            print("Adeus")
            break
        #Erro statement if input command not found
        else:
            print("Comando não encontrado")
#Remove Duplicated On List
def NonDuplicated(lista):
    l = []
    for i in lista:
        if i not in l:
            l.append(i)
    return l

#Login
loginMode=None
try:
    while(True):
        loginMode=input("Modo API (1) / Modo OAUTH (2) # ~>")
        if(loginMode=="1"):
            break
        elif(loginMode=="2"):
            break
        else:
            print("Erro!")
    youtube = Login.Auth.Main(loginMode)
    print("Iniciado com sucesso")
except:
    print("API se comportou de forma inesperada!")
main()

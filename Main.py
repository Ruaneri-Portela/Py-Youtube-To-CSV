import YoutubeApi
import Login

#Lang variable

Text=Text2=Text3=Text4=Text5=Text6=Text7=Text8=Text9=Text10=Text11=Text12=Text13=Text14=Text15=Text16=Text17=Text18=Text19=Text20=Text21="null"

# Connect to YoutubeApi, get videos or playlist data list.
def getVideos(playlistId,mode):
    youtubeImport = YoutubeApi.dataVideo
    return youtubeImport.getData(youtube,playlistId,mode)

# Main loop for script funcitions
def main():
    listVideo = []
    print(Text20)
    while True:

        comandVar = ""
        comandVar =input("#~>")

        if (comandVar == Text) or (comandVar == "1"):
            comandVar = input(f"#%s~>",Text)  
            if(comandVar == Text10) or (comandVar == "9"):
                pass
            elif(comandVar == Text11) or (comandVar == "0"):
                break
            else:
                try:
                 listVideo.extend(getVideos(comandVar,0)) 
                except:
                 print(f"%s,%s",Text8,Text12)

        elif (comandVar == Text2) or (comandVar == "2"):
            comandVar = input(f"#%s~>",Text)  
            if(comandVar == Text10) or (comandVar == "9"):
                pass
            elif(comandVar == Text11) or (comandVar == "0"):
                break
            else:
                try:
                 listVideo.extend(getVideos(comandVar,1)) 
                except:
                 print(f"%s,%s",Text8,Text12)

        elif  (comandVar == Text3) or (comandVar == "3"):
            for i in range(0,len(listVideo)):
                print(listVideo[i])
                print(f"%d, %s",len[i],Text14)

        elif (comandVar == Text4) or (comandVar == "4"):
            comandVar = input(Text9)
            if(comandVar == Text10) or (comandVar == "9"):
                pass
            elif(comandVar == Text11) or (comandVar == "0"):
                break
            else:
                csv = open(comandVar+".csv","w") 
                csv.write(Text15)
                nonDup=NonDuplicated(listVideo)
                for i in  range(0,len(nonDup)):
                  stringLine = nonDup[i][0]+"▎"+nonDup[i][1]+"▎"+nonDup[i][2]+"▎"+nonDup[i][3]+"▎"+nonDup[i][4]+"▎"+nonDup[i][5]+"\n"
                  csv.write(stringLine)
                csv.close()

        elif  (comandVar == Text16) or (comandVar == "8"):
            listaVideo = []
            print(Text17)

        #This function is for testing purposes
        elif (comandVar == "Test/Teste") or (comandVar == "99"):
            comandVar = input("#Test/Teste~>")  
            if(comandVar == Text10) or (comandVar == "9"):
                pass
            elif(comandVar == Text11) or (comandVar == "0"):
                break
            else:
                try:
                 print(YoutubeApi.dataVideo.a(youtube,comandVar))
                except:
                 print(f"%s,%s",Text8,Text12)

        elif (comandVar == Text11) or (comandVar == "0"):
            print("\n",Text5)
            break
        else:
            print(Text13)

# Remove duplicates from list       
def NonDuplicated(listToRemoveDuplicates):
    listTemp = []
    for i in listToRemoveDuplicates:
        if i not in listTemp:
            listTemp.append(i)
    return listTemp

#Localization script
def setLang(langVar):
    #langVar = ""
    #langVar = input("Select language/Selecione o idioma\n1~> English | 2~> Português")
    while True:
     if(langVar == "English") or (langVar == "1"):
        break
     elif(langVar == "Português") or (langVar == "2"):
        Text = "Adcionar ao aquivo uma playlist"
        Text2 = "Adcionar ao arquivo um unico video"
        Text3 = "Listar objetos a serem gravados"
        Text4 = "Gravar arquivo"
        Text5 = "Adeus !"
        Text6 = "API de login se comportou de forma inesperada"
        Text7 = "Necessario encerrar o script"
        Text8 = "Ocorreu um erro!"
        Text9 = "Qual o nome do arquivo?\nAtenção caso o nome do arquivo existir o existente ira ser substiuido"
        Text10 = "Retornar"
        Text11 = "Sair"
        Text12 = "Tente Novemente"
        Text13 = "Opção não disponivel"
        Text14 = "Videos foram gravados para serem exportados para o arquivos"
        Text15 = "Titulo▎Visualizações▎Gosteis▎Comentarios▎Data De Publicação▎Link\n"
        Text16 = "Limpar lista de exportação"
        Text17 = "A lista de videos a serem exportados foram apagados"
        Text18 = "Ajuda"
        Text19 = "Ajuda Menu"
        Text20 = "###################\nBem-Vindo ao exportado de estatisticas de videos do youtube em python"
        Text21 = "Iniciado com sucesso"
        break
     else:
        print("Option not supported! / Opção não suportada!")

# Startup Script
setLang("2")
loginMode=None
try:
    while(True):
        loginMode=input("#")
        if(loginMode=="1"):
            break
        elif(loginMode=="2"):
            break
        else:
            print(Text8)
    youtube = Login.Auth.Main(loginMode)
    print(Text21)
    try:
     main()
    except:
     print(f"%s, %s",Text8,Text7)
     exit(1)
except:
    print(f"%s, %s",Text6,Text7)
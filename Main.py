import YoutubeApi
import Login

returnVar = True
loginMode = None
# Connect To YoutubeAPI


def getVideos(playlistId, mode, listIndex):
    youtubeImport = YoutubeApi.dataVideo
    return youtubeImport.getData(youtube, playlistId, mode, listIndex)


# Main Script loop
def main():
    listIndex = 0
    listVideo = []
    headerCSV = "#|Titulo|Visualizações|Gosteis|Não Gosteis|Comentarios|Duração|Data De Publicação|Link\n"
    # Header
    print("#######################\nBem vindo ao importador de dados de videos e playlist do youtube")
    while True:
        # Input
        comandVar = ""
        comandVar = input("#~>")
        # Append Videos On Playlsit To List
        if (comandVar == "Ler Playlist") or (comandVar == "1"):
            comandVar = input("#Id de uma playlist~>")
            if (comandVar == "Retornar") or (comandVar == "9"):
                pass
            elif (comandVar == "Sair") or (comandVar == "0"):
                break
            else:
                try:
                    listVideo.extend(getVideos(comandVar, 0, listIndex))
                    listIndex = len(listVideo)
                except:
                    print("Ocorreu um erro! Tente novamente.")
        # Append Single Video To List
        elif (comandVar == "Ler Video") or (comandVar == "2"):
            comandVar = input("#Id de um video~>")
            if (comandVar == "Retornar") or (comandVar == "9"):
                pass
            elif (comandVar == "Sair") or (comandVar == "0"):
                break
            else:
                try:
                    listVideo.extend(getVideos(comandVar, 1, listIndex))
                    listIndex = len(listVideo)
                except:
                    print("Ocorreu um erro! Tente novamente.")
        # View Video List
        elif (comandVar == "Mostrar lista de videos importados") or (comandVar == "3"):
            for i in range(0, len(listVideo)):
                print(listVideo[i])
            print("Existem ", len(listVideo), " videos importados")
        # Export To CSV File
        elif (comandVar == "Exportar dados para um arquivo") or (comandVar == "4"):
            comandVar = input(
                "Criando Arquivo\nQual o nome do arquivo? ATENÇÃO caso o arquivo exista ele vai ser substituido\n#Exportar lista~>")
            if (comandVar == "Retornar") or (comandVar == "9"):
                pass
            elif (comandVar == "Sair") or (comandVar == "0"):
                break
            else:
                csv = open(comandVar+".csv", "w")
                csv.write(headerCSV)
                nonDup = NonDuplicated(listVideo)
                for i in range(0, len(nonDup)):
                    stringLine = nonDup[i][0].replace(
                        ",", "/")+","+nonDup[i][1]+","+nonDup[i][2] + ","+nonDup[i][3]+","+nonDup[i][4]+","+nonDup[i][5]+","+nonDup[i][6]+","+nonDup[i][7]+"\n"
                    csv.write(stringLine)
                csv.write(
                    "Exportador de dados do youtube para planilha eletronica. Criador por Ruaneri Portela/Brasil 2022")
                csv.close()
            print("Dados exportados em", comandVar+".csv")
        # Get all data
        elif (comandVar == "Todos Os Dados") or (comandVar == "6"):
            indexVar = input(
                "#~>Qual o video da lista que você deseja mais informações? ")
            if (comandVar == "Retornar") or (comandVar == "9"):
                pass
            elif (comandVar == "Sair") or (comandVar == "0"):
                break
            else:
                try:
                    indexVar = (int)(indexVar)
                    print("Mostrando todos os dados de -> ",
                          (listVideo[indexVar][1]), "\n")
                    stringRemove = str(listVideo[indexVar][8])
                    id = str(stringRemove.replace("https://youtu.be/", ""))
                    print(YoutubeApi.dataVideo.allData(youtube, id))
                except:
                    print("Ocorreu um erro! Tente novamente.")
        # Clean Video List Data
        elif (comandVar == "Limpar Lista") or (comandVar == "7"):
            listVideo = []
            listIndex = 0
            print("Lista limpa!")
        # Help informations
        elif (comandVar == "Ajuda") or (comandVar == "8"):
            print("Tela de Ajuda:\n1 -> Ler uma Playlist\n2 -> Ler um video\n3 -> Listar videos importados\n4 -> Exportar para um arquivo os dados dos videos importados\n6 -> Obter todos os dados de um video na lista\n7 -> Limpar lista de videos importados\n8 -> Ajuda \n9 -> Retornar para tela de login\n0 -> Sair\n ")
        # Return to login
        elif (comandVar == "Login") or (comandVar == "9"):
            print("Voltando para tela de login")
            youtube.close()
            return True
        # Exit script
        elif (comandVar == "Sair") or (comandVar == "0"):
            print("Adeus")
            return False
        # Erro statement if input command not found
        else:
            print("Comando não encontrado\n(8) Tela de Ajuda")


# Remove Duplicated On List
def NonDuplicated(removeDuplicatedOnList):
    newNonHaveDuplicate = []
    for i in removeDuplicatedOnList:
        if i not in newNonHaveDuplicate:
            newNonHaveDuplicate.append(i)
    return newNonHaveDuplicate


try:
    while (returnVar):
        loginMode = input("Modo API (1) / Modo OAUTH (2) # ~>")
        if (loginMode == "1"):
            youtube = Login.Auth.Main(loginMode)
            print("Iniciado com sucesso")
            returnVar = main()
            pass
        elif (loginMode == "2"):
            youtube = Login.Auth.Main(loginMode)
            print("Iniciado com sucesso")
            returnVar = main()
            pass
        elif (loginMode == "0"):
            break
        else:
            print("Erro!")
except:
    print("API se comportou de forma inesperada!")

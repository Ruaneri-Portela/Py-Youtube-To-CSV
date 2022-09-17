from email import header
import YoutubeApi
import Login
import sys

returnVar = True
loginMode = None
# Connect To YoutubeAPI


def getVideos(playlistId, mode):
    youtubeImport = YoutubeApi.dataVideo
    return youtubeImport.getData(youtube, playlistId, mode)


# Main Script loop
def main():
    listVideo = []
    headerCSV = "Titulo|Visualizações|Gosteis|Não Gosteis|Comentarios|Data De Publicação|Link\n"
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
                    listVideo.extend(getVideos(comandVar, 0))
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
                    listVideo.extend(getVideos(comandVar, 1))
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
                "Qual o nome do arquivo? ATENÇÃO caso o arquivo exista ele vai ser substituido\n#Exportar lista~>")
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
                        "|", " , ")+"|"+nonDup[i][1]+"|"+nonDup[i][2] + "|"+nonDup[i][3]+"|"+nonDup[i][4]+"|"+nonDup[i][5]+"|"+nonDup[i][6]+"\n"
                    csv.write(stringLine)
                csv.close()
            print("Dados exportados em", comandVar+".csv")
        # Clean Video List Data
        elif (comandVar == "Limpar Lista") or (comandVar == "7"):
            listVideo = []
            print("Lista limpa!")
        # Help informations
        elif (comandVar == "Ajuda") or (comandVar == "8"):
            print("Tela de Ajuda:\n1 -> Ler uma Playlist\n2 -> Ler um video\n3 -> Listar videos importados\n4 -> Exportar para um arquivo os dados dos videos importados\n7 -> Limpar lista de videos importados\n8 -> Ajuda \n9 -> Retornar para tela de login\n0 -> Sair\n ")
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

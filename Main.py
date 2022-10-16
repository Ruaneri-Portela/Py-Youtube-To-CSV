import YoutubeApi
import Login
from os import system, name

returnVar = True
loginMode = None
# Connect To YoutubeAPI


def getVideos(playlistId, mode, listIndex, listVideo):
    youtubeImport = YoutubeApi.dataVideo
    return youtubeImport.getData(youtube, playlistId, mode, listIndex, listVideo)


# Main Script loop
def main():
    listIndex = 0
    listVideo = []
    headerCSV = "#,Titulo,Visualizações,Gosteis,Não Gosteis,Comentarios,Duração,Data De Publicação,Link\n"
    # Header
    print("#######################\nBem vindo ao importador de dados de videos e playlist do youtube")
    while True:
        try:
            # Input
            comandVar = ""
            comandVar = input("#~>")
            # Append Videos On Playlsit To List
            if (comandVar == "Ler Playlist") or (comandVar == "1"):
                clear()
                comandVar = input("#Id de uma playlist~>")
                if (comandVar == "Retornar") or (comandVar == "9"):
                    pass
                elif (comandVar == "Sair") or (comandVar == "0"):
                    break
                else:
                    listVideo.extend(
                        getVideos(comandVar, 0, listIndex, listVideo))
                    listIndex = len(listVideo)
            # Append Single Video To List
            elif (comandVar == "Ler Video") or (comandVar == "2"):
                clear()
                comandVar = input("#Id de um video~>")
                if (comandVar == "Retornar") or (comandVar == "9"):
                    pass
                elif (comandVar == "Sair") or (comandVar == "0"):
                    break
                else:
                    listVideo.extend(
                        getVideos(comandVar, 1, listIndex, listVideo))
                    listIndex = len(listVideo)
            # View Video List
            elif (comandVar == "Mostrar lista de videos importados") or (comandVar == "3"):
                clear()
                print("Mostrando videos importados")
                for i in range(0, len(listVideo)):
                    print(listVideo[i])
                print("Existem ", len(listVideo), " videos importados")
            # Export To CSV File
            elif (comandVar == "Exportar dados para um arquivo") or (comandVar == "4"):
                clear()
                comandVar = input(
                    "Criando Arquivo\nQual o nome do arquivo? ATENÇÃO caso o arquivo exista ele vai ser substituido\n#Exportar lista~>")
                if (comandVar == "Retornar") or (comandVar == "9"):
                    pass
                elif (comandVar == "Sair") or (comandVar == "0"):
                    break
                else:
                    csv = open(comandVar+".csv", "w")
                    csv.write(headerCSV)
                    for i in range(0, len(listVideo)):
                        stringLine = str(listVideo[i][0])+","+listVideo[i][1].replace(
                            ",", "/")+","+listVideo[i][1]+","+listVideo[i][2] + ","+listVideo[i][3]+","+listVideo[i][4]+","+listVideo[i][5]+","+listVideo[i][6]+","+listVideo[i][7]+"\n"
                        csv.write(stringLine)
                    csv.write(
                        "Exportador de dados do youtube para planilha eletronica. Criador por Ruaneri Portela/Brasil 2022")
                    csv.close()
                print("Dados exportados em", comandVar+".csv")
            # Get all data
            elif (comandVar == "Todos Os Dados") or (comandVar == "6"):
                clear()
                indexVar = input(
                    "#~>Qual o video da lista que você deseja mais informações? ")
                if (comandVar == "Retornar") or (comandVar == "9"):
                    pass
                elif (comandVar == "Sair") or (comandVar == "0"):
                    break
                else:
                    indexVar = (int)(indexVar)
                    print("Mostrando todos os dados de -> ",
                          (listVideo[indexVar][1]), "\n")
                    stringRemove = str(listVideo[indexVar][8])
                    id = str(stringRemove.replace("https://youtu.be/", ""))
                    print(YoutubeApi.dataVideo.allData(youtube, id))
            # Clean Video List Data
            elif (comandVar == "Limpar Lista") or (comandVar == "7"):
                clear()
                listVideo = []
                listIndex = 0
                print("Lista limpa!")
            # Help informations
            elif (comandVar == "Ajuda") or (comandVar == "8"):
                clear()
                print("Tela de Ajuda:\n1 -> Ler uma Playlist\n2 -> Ler um video\n3 -> Listar videos importados\n4 -> Exportar para um arquivo os dados dos videos importados\n6 -> Obter todos os dados de um video na lista\n7 -> Limpar lista de videos importados\n8 -> Ajuda \n9 -> Retornar para tela de login\n0 -> Sair\n ")
            # Return to login
            elif (comandVar == "Login") or (comandVar == "9"):
                clear()
                print("Voltando para tela de login")
                youtube.close()
                return True
            # Exit script
            elif (comandVar == "Sair") or (comandVar == "0"):
                clear()
                print("Adeus")
                return False
            # Erro statement if input command not found
            else:
                clear()
                print("Comando não encontrado\n(8) Tela de Ajuda")
        except:
            erro(True, "0x00")


# Clear Display

def clear():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")

# Erro Display


def erro(statment, code):
    print('\a')
    if (statment):
        print("Ocorreu um erro! Tente novamente."+code)
    else:
        print("Erro Fatal"+code)

class API:
    def getInformation(id,youtube):
     getVideos(comandVar, 1, listIndex, listVideo)
     return(getVideos(comandVar, 1, listIndex, listVideo))

try:
    while (returnVar):
        clear()
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
            erro(True, "0x00")
except:
    erro(False, "0x01")

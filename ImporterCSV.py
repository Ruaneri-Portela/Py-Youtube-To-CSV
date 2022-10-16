import Login
import YoutubeApi
import time
import datetime
import os
input = open(r"input.csv", "r")
output = open(r"output.csv", "w")
array_data = (input.readlines())
list_consute = []
youtube = Login.Auth.Main("1")
youtubeImport = YoutubeApi.dataVideo
for i in array_data:
    rmv = i.split(",")
    for a in range(0, len(rmv)):
        rmv[a] = rmv[a].replace("\\ufeff", "")
        rmv[a] = rmv[a].replace("\n", "")
    list_consute.append(rmv)
output.write("QUALIDADE CONFIABILIDADE SUST.CIENT.(CST)\nAVALIAÇÃO GERAL CONTEÚDO DIDÁTICO-METODOLÓGICOS TÉCNICOS CST\n")
output.write("Titulo,Visualizações,Gosteis,Não Gosteis,Comentarios,Duração,Data De Publicação,Link,Nome Canal,Inscritos,1.Clareza nos Objetivos,2.Objet.Alcanc.,3.É relevante?,4.Fonte de Inform.,5.Clareza Inform.,6.Viés e Equilíbrio,7.Fontes Adic.de Inform.,8.Refer.Áreas Incert.,9.Comp.Quím.Á.Nucl.Nucleotd.,10.Papel do DNA/RNA,11.Diferenças DNA/RNA,12.Forças.Intermolec.Conform.DNA,13.Influência PH.Temp.Enovelamento e Mudança Conform.Estrutural DNA,14.Contextualização com Cotidiano e Transdiscip.,15.Clareza e Coesão,16.Aproxim.com Aceito na Comun.Científica,17.Recursos eficazes e Duração do Vídeo,18.Edição dos Vídeos,19.Dados Autorais e Produção,20.Interligação Aspectos Técnicos/Didat.Metodol. e de Conteúdo,21.Zooms/Enquad/Visão de Fundo,22.Editado Profissionalmente,23.Qualidade do vídeo como Fonte de Inform.,24.Infor.Claras e Objetivas,25.Fontes Confiáveis de Inform.,26.Inform.Equilibrada e Imparcial,27.Confiabilidade do vídeo como Fonte de Inform.,\n")
for i in range (0,len(list_consute)):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Carrengando Item Numero "+str(i)+"\n")
    time.sleep(0.8)
    idv = list_consute[i][1].replace("https://youtu.be/", "")
    listIndex = 0
    listVideo = []
    listVideo = youtubeImport.getData(youtube,idv, 1, listIndex, listVideo)
    stringData=""
    for s in range (2,len(list_consute[i])):
        stringData=stringData+str(list_consute[i][s]+",")
    stats=[]
    reply = youtube.videos().list(part="snippet", id=idv).execute()
    stats += reply["items"]
    idCh=(stats[0]["snippet"]["channelId"])
    nameCH=(stats[0]["snippet"]["channelTitle"])
    stats=[]
    reply = youtube.channels().list(part="statistics",id=idCh).execute()
    stats += reply["items"]
    subCont=(stats[0]["statistics"]["subscriberCount"])
    stringLine = listVideo[0][1].replace(",", "/")+","+listVideo[0][2]+","+listVideo[0][3] + ","+listVideo[0][4]+","+listVideo[0][5]+","+listVideo[0][6]+","+listVideo[0][7]+","+listVideo[0][8]+","+nameCH.replace(",", "/")+","+subCont+","+stringData+"\n"
    output.write(stringLine)
    listVideo = []
Current_Date = datetime.datetime.today()
output.write("Data da consulta => "+str(Current_Date)+ " UTC TIME - AAAA-MM-DD / Planilha gerada dados obtidos robotizadamente usando a Youtube API e Python / Codigo disponivel em https://github.com/Ruaneri-Portela/Py-Youtube-To-CSV / Codigo criado por Ruaneri Portela \n Classificado por Marcelo Dias Rodrigues")
output.close()
input.close()

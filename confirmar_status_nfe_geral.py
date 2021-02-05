#Libs necessarias
import requests
from bs4 import BeautifulSoup

#Capturando todos os status de todos os serviços
link = "https://www.nfe.fazenda.gov.br/portal/disponibilidade.aspx?versao=0.00&tipoConteudo=Skeuqr8PQBY="
site_receita = requests.get(link).text #Requests to text.html
soup = BeautifulSoup(site_receita, 'html.parser') #Lendo o conteudo do requests
todos_titulos = soup.findAll("th") #Todos os titulos
todas_tr_impar = soup.findAll("tr", {"class":"linhaImparCentralizada"}) #Todas linhas impars TR
todas_tr_par = soup.findAll("tr", {"class":"linhaParCentralizada"}) #Todas linhas pares TR
todas_tr = todas_tr_impar + todas_tr_par #Juntando as TR

#Limpeza -> Confere o status das imagens e textos
def confirmar_status(entrada):
    #Confere se é imagema
    try:
        imagens = entrada.findAll("img")
        imagens = imagens[0]['src']
    except:
        imagens = None
    #Retorno dos valores
    if imagens is not None:
        #Se tem servico com status anormal
        if imagens == "imagens/bola_verde_P.png":
            return True
        else:
            return False
    else:
        #Texto
        if len(entrada.text) == 0:
            return "-"
        else:
            return entrada.text
            
#Titulos
campos = []
for i in todos_titulos:
    campos.append(i.text)

#Buscando os campos 
todos_campos = []
for linha in todas_tr:
    estados = []
    for i in zip(campos, linha.findAll("td")):
        posLimpeza = [i[0], confirmar_status(i[1])]
        estados.append(posLimpeza)
    todos_campos.append(estados)

#Conferindo o que esta com problemas

#status inicial do problema
problemas = False #Mensagem que deu ruim
locais_com_problemas = ["Estado ==> Servico ==> Status"] #Guardar os status da operacao

#Buscando quem ta com problemas
for linhas_campos in todos_campos:
    for c in linhas_campos:
        #So mostrar que ta com problema
        if c[1] == False:
            locais_com_problemas.append("{} ==> {} ==> Problema".format(linhas_campos[0][1],c[0]))
            problemas = True

#Saida dos status
if problemas:
    for i in locais_com_problemas:
        print(i)
else:
    print("Status Nfe Ok")           
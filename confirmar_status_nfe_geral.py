import requests
from bs4 import BeautifulSoup

#Capturando todos os status de todos os serviços
link = "https://www.nfe.fazenda.gov.br/portal/disponibilidade.aspx?versao=0.00&tipoConteudo=Skeuqr8PQBY="
site_receita = requests.get(link).text
soup = BeautifulSoup(site_receita, 'html.parser')
todas_tr_impar = soup.findAll("tr", {"class":"linhaImparCentralizada"})
todas_tr_par = soup.findAll("tr", {"class":"linhaParCentralizada"})
todas_tr = todas_tr_impar + todas_tr_par

#Limpeza
def confirmar_status(entrada):
    entrada = entrada['src']
    if entrada == "imagens/bola_verde_P.png":
        return True
    else:
        return False

#Buscando  os campos 
todas_tr_limpa = []
for linha in todas_tr:
    for campo in linha:
        #O try é por causa do findall
        try:
            entrada = campo.findAll("img")
            if (len(entrada)) == 1:
                todas_tr_limpa.append(entrada[0])
        except:
            pass

#Acusa se tiver problemas
problemas = False
for valor in todas_tr_limpa:
    if not(confirmar_status(valor)):
        print("1")
        problemas = True
        break

#Ultima msg caso nao tiver problemas
if not(problemas):
    print("0")

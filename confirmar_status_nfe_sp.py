import requests
from bs4 import BeautifulSoup

#Capturando todos os status de determinados estados
link = "https://www.nfe.fazenda.gov.br/portal/disponibilidade.aspx?versao=0.00&tipoConteudo=Skeuqr8PQBY="
site_receita = requests.get(link).text
soup = BeautifulSoup(site_receita, 'html.parser')
todas_tr = soup.findAll("tr", {"class":"linhaImparCentralizada"})
estado_sp = todas_tr[5].findAll("td")

#Limpeza
def confirmar_status(entrada):
    if entrada.get_text() != "-":
        entrada = entrada.findAll("img")
        for imagem in entrada:
            entrada = imagem['src']
        if entrada == "imagens/bola_verde_P.png":
            return "Verde"
        elif entrada == "imagens/bola_amarela_P.png":
            return "Amarelo"
        elif entrada == "imagens/bola_vermelho_P.png":
            return "Vermelho"
        else:
            return "Estado indefinido"
    else:
        return "-"

#Saida do estado
print("Autorizador: {}\n\
Autorização4: {}\n\
Retorno Autorização4: {}\n\
Inutilização4: {}\n\
Consulta Protocolo4: {}\n\
Status Serviço4: {}\n\
Tempo Médio: {}\n\
Consulta Cadastro4: {}\n\
Recepção Evento4: {}".format(
        estado_sp[0].get_text(),
        confirmar_status(estado_sp[1]),
        confirmar_status(estado_sp[2]),
        confirmar_status(estado_sp[3]),
        confirmar_status(estado_sp[4]),
        confirmar_status(estado_sp[5]),
        confirmar_status(estado_sp[6]),
        confirmar_status(estado_sp[7]),
        confirmar_status(estado_sp[8])
    ))
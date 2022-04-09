import requests

############################################################## MOEDAS #################################################
#Dólar Americano = USD
#Euro = EUR
#Libra esterlina = GBP
#Iene = JPY
#Dólar Australiano = AUD
#Franco Suíço = CHF
#Dólar Canadense = CAD
#Renminbi (Yuan) = CNY
#Peso Argentino = ARS

#Ethereum = ETH
#Bitcoin = BTC
#Dogecoin = DOGE


## MOEDAS COM CONVERSÃO COMPLETA (ORIGEM): BRL, EUR, USD
## MOEDAS COM CONVERSÃO PARCIAL (ORIGEM): GBP, JPY, AUD, CHF, CAD, CNY, ARS
## MOEDAS SEM CONVERSÃO (ORIGEM): BTC, ETH, DOGE


###############  MOEDA --> BRL ##############
requisicaobrl = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL,GBP-BRL,JPY-BRL,AUD-BRL,CHF-BRL,CAD-BRL,CNY-BRL,ARS-BRL,ETH-BRL,DOGE-BRL')
requisicaobrl_dic = requisicaobrl.json()

cotacao_usdbrl = requisicaobrl_dic['USD']['bid']
cotacao_eurbrl = requisicaobrl_dic['EUR']['bid']
cotacao_btcbrl = requisicaobrl_dic['BTC']['bid']
cotacao_gbpbrl = requisicaobrl_dic['GBP']['bid']
cotacao_jpybrl = requisicaobrl_dic['JPY']['bid']
cotacao_audbrl = requisicaobrl_dic ['AUD']['bid']
cotacao_chfbrl = requisicaobrl_dic ['CHF']['bid']
cotacao_cadbrl = requisicaobrl_dic ['CAD']['bid']
cotacao_cnybrl = requisicaobrl_dic ['CNY']['bid']
cotacao_arsbrl = requisicaobrl_dic ['ARS']['bid']
cotacao_ethbrl = requisicaobrl_dic ['ETH']['bid']
cotacao_dogebrl = requisicaobrl_dic ['DOGE']['bid']
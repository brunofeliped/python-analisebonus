import pandas as pd
from twilio.rest import Client

# Twilio client config
account_sid = "XXXXXXX"
auth_token = "XXXXXXX"
client = Client(account_sid, auth_token)

lista_meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto"]

for mes in lista_meses:
    # print(mes)
    tabela_vendas = pd.read_excel(f"{mes}.xlsx")
    # print(tabela_vendas)
    if (tabela_vendas["Vendas"] > 90000).any():
        vendedor = tabela_vendas.loc[tabela_vendas["Vendas"] > 90000, "Vendedor"].values[0]
        vendas = tabela_vendas.loc[tabela_vendas["Vendas"] > 90000, "Vendas"].values[0]
        print(f"No mês de {mes} alguém bateu a meta. Vendedor {vendedor} vendeu R${vendas} !")
        message = client.messages.create(
            to="XXXXXXX",
            from_="XXXXXX",
            body=f"No mês de {mes} alguém bateu a meta. Vendedor {vendedor} vendeu R${vendas} !")
        print("SID MSG: " + message.sid)
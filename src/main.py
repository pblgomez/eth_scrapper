import os
from oauth2client.service_account import ServiceAccountCredentials
import gspread
from datetime import datetime, timedelta

from bs4 import BeautifulSoup
from requests import get as url_get


eth_wallet = os.environ['ETH_WALLET']
print("Cheking ethereum wallet: "+eth_wallet)
url = 'https://etherscan.io/txsInternal?a='+eth_wallet
header = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64)'}
r = url_get(url, headers=header)
soup = BeautifulSoup(r.text, "html.parser")
latest_value = soup("td")[8:9]
latest_value= str(latest_value[0].text).strip(" Ether")
print(latest_value)

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
        "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]


dir_path = os.path.dirname(os.path.realpath(__file__))
creds = ServiceAccountCredentials.from_json_keyfile_name(
    dir_path+"/creds.json", scope)
client = gspread.authorize(creds)

sheet = client.open(os.environ['SHEET_NAME']).worksheet(
    os.environ["WORKSHEET_NAME"])


# Get data filled
data = sheet.get_all_records()
num_rows = len(data)
num_rows = num_rows + 1
new_row = num_rows + 1

date_last = sheet.cell(num_rows, 1).value
print("Última fecha:", date_last)


now = datetime.now()

lastValue = sheet.cell(num_rows, 3).value
value = latest_value + " ETH"
print("Último valor: "+lastValue)
print("Nuevo  valor: "+value)

if (value != lastValue):
    sheet.update_cell(num_rows+1, 1, now.strftime("%d/%b/%Y"))
    sheet.update_cell(num_rows+1, 3, value.strip(" ETH"))
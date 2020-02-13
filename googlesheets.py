import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
             "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("sheet.json", scope)
client = gspread.authorize(creds)
sheet = client.open("pythonsheet").sheet1



def google_sort(code):
    global sheet
    cell = sheet.find(str(code))
    row = sheet.row_values(cell.row)

    #return code + row[1] + ', осталось ' + str(row[2]) + ' штук'
    return 'код товара - ' + code + '\n' + '\n' + row[1] + '\n' + '\n' + 'цена - ' + row[2] + '\n' + '\n' + row[3]



import gspread
from oauth2client.service_account import ServiceAccountCredentials

auth_json_path = 'PythonUpload.json'
gss_scopes = ['https://spreadsheets.google.com/feeds']

#連線
credentials = ServiceAccountCredentials.from_json_keyfile_name(auth_json_path,gss_scopes)
gss_client = gspread.authorize(credentials)

#開啟 Google Sheet 資料表
spreadsheet_key = 'GOOGLE雲端EXCEL的ID'
sheet = gss_client.open_by_key(spreadsheet_key).sheet1

# Google Sheet 資料表
sheet.clear() # 清除 Google Sheet 資料表內容
listtitle=["姓名","電話"]
sheet.append_row(listtitle)  # 標題
listdata=["Gatsby","0982-000000"]
sheet.append_row(listdata)  # 資料內容
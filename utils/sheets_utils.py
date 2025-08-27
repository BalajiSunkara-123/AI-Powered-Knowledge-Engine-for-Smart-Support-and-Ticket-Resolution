import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd


# Read all records into a list of dicts
# data = sheet.get_all_records()

# # Convert to pandas DataFrame
# df = pd.DataFrame(data)

# sheet.append_row([2,"das","ddwa","wda","dadsd","dsada"])

def connectToSheets():
    scope = ["https://spreadsheets.google.com/feeds",
            "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
    client = gspread.authorize(creds)
    return client

def sheet():
    client=connectToSheets()
    sheet=client.open("Ticket Details").sheet1
    return sheet


def insertRecord(row):
    client=connectToSheets()
    sheet = client.open("Ticket Details").sheet1  # first worksheet
    sheet.append_row(row)
    sheet


# print(df.head())

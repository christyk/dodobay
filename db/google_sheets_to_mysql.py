import os
import mysql.connector
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
SPREADSHEET_ID = "13d_LAJPlxMa_DubPTuirkIV4DERBMXbrWQsmSh8ReK4"
CREDS_FILE = "google_credentials.json"

def main():

    # Establish Google Credentials
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    try:

        # Create Database
        mydb = mysql.connector.connect(
            host="localhost",
            user="ck_portfolio",
            password="CreatureIntersection!23"
        )
        mycursor = mydb.cursor()

        mycursor.execute("SHOW DATABASES")

        dbexist = False

        for x in mycursor:
            if 'DODOBAY' in x:
                dbexist = True
                break

        if not dbexist:
            mycursor.execute("CREATE DATABASE DODOBAY")

        # Login to Database
        mydb = mysql.connector.connect(
            host="localhost",
            user="ck_portfolio",
            password="CreatureIntersection!23",
            database="DODOBAY"
        )
        mycursor = mydb.cursor()

        # Connect to Google Sheets service
        service = build("sheets", "v4", credentials=creds)
        sheets = service.spreadsheets()
        
        # Get properties of the identified spreadsheet (without grid data)
        sheets_metadata = sheets.get(spreadsheetId=SPREADSHEET_ID).execute()
        properties = sheets_metadata.get('sheets')

        # Initialize the list of categories to be filled with table names
        categories = []

        # Iterate sheets identified in the spreadsheet properties
        for sheet in properties:

            sheet_title = sheet.get("properties").get('title')

            # Skipping the Read Me sheet
            if sheet_title != "Read Me":

                # Initiate names and types used in creating database table
                table_name = sheet_title.upper().replace(' ', '_').replace('/', '_').replace('-', '_').replace('?', '').replace('#', 'NUMBER_').replace('(', '').replace(')', '').replace('\'', '').replace('\'', '')
                if table_name == 'SET': table_name = 'IN_SET'
                if table_name == 'NUMBER_': table_name = 'NUMBER'
                print(table_name)
                categories.append((sheet_title, 'SHEETS_ITEMS_' + table_name))
                table_columns = []
                table_column_types = []
                table_column_values = []

                if sheet.get("properties").get('sheetType') == 'GRID':

                    sheet_data = sheets.get(spreadsheetId=SPREADSHEET_ID, ranges=sheet_title, includeGridData=True).execute()
                    grid_data = sheet_data.get('sheets')
                    for this_sheet in grid_data:
                        
                        row_data = this_sheet.get('data')[0].get('rowData')
                        
                        rownum=0
                        for row in row_data:
                            rownum=rownum+1

                            row = row.get('values')
                            
                            # Initiate Column values for each row
                            table_column_values.clear()

                            for cell in row:
                                
                                data_key_value = cell.get('userEnteredValue')

                                if data_key_value == None:
                                    table_column_values.append('NA')
                                    if rownum == 2:
                                        table_column_types.append('VARCHAR(255)')
                                else:
                                    if 'stringValue' in data_key_value:
                                        data_type = 'VARCHAR(255)'
                                        data_value = data_key_value['stringValue']
                                    
                                    elif 'numberValue' in data_key_value:
                                        data_type = 'VARCHAR(255)'
                                        data_value = str(data_key_value['numberValue'])
                                    
                                    elif 'boolValue' in data_key_value:
                                        data_type = 'BOOL'
                                        data_value = str(data_key_value['boolValue'])
                                    
                                    elif 'formulaValue' in data_key_value and ('=IMAGE' in data_key_value['formulaValue'] or '=image' in data_key_value['formulaValue']):
                                        data_type = 'VARCHAR(255)'
                                        data_value = data_key_value['formulaValue'][8:-2]
                                    
                                    elif 'errorValue' in data_key_value:
                                        data_value = str(data_key_value['errorValue'])
                                    

                                    # From row 1, get column name of cell
                                    if rownum == 1:
                                        data_value = str(data_value).upper().replace(' ', '_').replace('/', '_').replace('-', '_').replace('?', '').replace('#', 'NUMBER_').replace('(', '').replace(')', '').replace('\'', '\\\'').replace('\"', '\\\"').replace('\\\\', '\\')
                                        if data_value == 'SET': data_value = 'IN_SET'
                                        if data_value == 'NUMBER_': data_value = 'NUMBER'
                                        table_columns.append(data_value)

                                    # From row 2, get column data type of cell
                                    elif rownum == 2:
                                        data_value = str(data_value).replace('\'', '\\\'').replace('\"', '\\\"').replace('\\\\', '\\')
                                        table_column_types.append(data_type)
                                        table_column_values.append(data_value)

                                    # All other rows, get data value of cell
                                    else:
                                        data_value = str(data_value).replace('\'', '\\\'').replace('\"', '\\\"').replace('\\\\', '\\')
                                        table_column_values.append(data_value)

                            # For row 1, do nothing, waiting on data types from row 2
                            if rownum == 1:
                                continue

                            # For row 2, create table if it does not exist, insert data
                            elif rownum == 2:

                                mycursor.execute("SHOW TABLES")
                                tbexist = False
                                for x in mycursor:
                                    if 'SHEETS_ITEMS_' + table_name in x:
                                        tbexist = True

                                if not tbexist:
                                    create_table_columns = list(map(' '.join, zip(table_columns, table_column_types)))
                                    create_table_string = 'CREATE TABLE SHEETS_ITEMS_' + table_name + ' (' + ', '.join(create_table_columns) + ', PRIMARY KEY (UNIQUE_ENTRY_ID))'
                                    create_table_string = create_table_string.replace('DESCRIPTION VARCHAR(255)', 'DESCRIPTION VARCHAR(1000)')
                                    create_table_string = create_table_string.replace('LIST VARCHAR(255)', 'LIST VARCHAR(1000)')
                                    create_table_string = create_table_string.replace('NOTES VARCHAR(255)', 'NOTES VARCHAR(1000)')
                                    create_table_string = create_table_string.replace('_NH VARCHAR(255)', '_NH VARCHAR(20)')
                                    create_table_string = create_table_string.replace('_SH VARCHAR(255)', '_SH VARCHAR(20)')
                                    create_table_string = create_table_string.replace('IMAGE_SH VARCHAR(20)', 'IMAGE_SH VARCHAR(255)')  
                                    create_table_string = create_table_string.replace('DIY_ICON_FILENAME_SH VARCHAR(20)', 'DIY_ICON_FILENAME_SH VARCHAR(255)')                               
                                    print(create_table_string)
                                    mycursor.execute(create_table_string)

                                insert_data_string = 'INSERT INTO SHEETS_ITEMS_' + table_name + ' (' + ', '.join(table_columns) + ') VALUES (\"' + '\", \"'.join(table_column_values) + '\")'
                                print(insert_data_string)
                                mycursor.execute(insert_data_string)

                            # For other rows, insert data
                            else:
                                insert_data_string = 'INSERT INTO SHEETS_ITEMS_' + table_name + ' (' + ', '.join(table_columns) + ') VALUES (\"' + '\", \"'.join(table_column_values) + '\")'
                                print(insert_data_string)
                                mycursor.execute(insert_data_string)                          
                else:
                    print('No grid found in sheet ' + sheet_title)

        # Create the CATEGORIES table and insert each category as row
        mycursor.execute("SHOW TABLES")
        tbexist = False
        for x in mycursor:
            if 'CATEGORIES' in x:
                tbexist = True
                break

        if not tbexist:
            mycursor.execute('CREATE TABLE CATEGORIES (id INT AUTO_INCREMENT PRIMARY KEY, NAME VARCHAR(255), TABLE_NAME VARCHAR(255), CLASS_NAME VARCHAR(255), TRADABLE BOOL)')
        
            insert_categories_string = 'INSERT INTO CATEGORIES (NAME, TABLE_NAME) VALUES (%s, %s)'
            print(categories)
            mycursor.executemany(insert_categories_string, categories)

        # Commit the changes and close the cursor and connection
        mydb.commit()
        mycursor.close()
        mydb.close()
        
    except HttpError as error:
        print(error)

if __name__ == "__main__":
    main()
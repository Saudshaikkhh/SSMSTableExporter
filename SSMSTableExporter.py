import pyodbc
import pandas as pd

# Database connection configuration
server = '183.83.177.224,53585'
database = 'hpscb_bancscan'
username = 'sa'
password = 'ntplupl@123'
driver = '{ODBC Driver 17 for SQL Server}'  # Update the driver if necessary

# Output files
output_txt_file = 'table_names.txt'
output_excel_file = 'table_names.xlsx'

# Connection string
connection_string = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'

try:
    # Connect to the database
    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()

    # Query to get all table names in the database
    cursor.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE';")
    tables = cursor.fetchall()

    # Extract table names into a list
    table_names = [table.TABLE_NAME for table in tables]

    # Write table names to a text file
    with open(output_txt_file, 'w') as file:
        for table_name in table_names:
            file.write(table_name + '\n')

    # Write table names to an Excel file using pandas
    df = pd.DataFrame(table_names, columns=['Table Name'])
    df.to_excel(output_excel_file, index=False)

    print(f"Table names have been written to {output_txt_file} and {output_excel_file}")

except pyodbc.Error as err:
    print(f"Error: {err}")

finally:
    # Close the connection
    if 'connection' in locals() and connection:
        connection.close()
        print("Database connection closed.")
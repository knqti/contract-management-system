import sqlite3
from pathlib import Path
from queries import select_all, view_contract_summary, view_contract_details
from setup import create_table, insert_data

# Setup db
root_dir = Path(__file__).parent
connection = sqlite3.connect(root_dir / 'cms.db')
cursor = connection.cursor()

# create_table(connection, cursor)
# insert_data(connection, cursor)

# select_all(cursor)
# view_contract_summary(cursor, id=11)
view_contract_details(cursor, id=11)

cursor.close()
connection.close()
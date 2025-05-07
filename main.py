import sqlite3
from pathlib import Path
from queries import select_all
from setup import create_table, insert_data

# Setup db
root_dir = Path(__file__).parent
connection = sqlite3.connect(root_dir / 'cms.db')
cursor = connection.cursor()

# create_table(connection, cursor)
insert_data(connection, cursor)

select_all(cursor)

cursor.close()
connection.close()
import sqlite3
from pathlib import Path
from queries import view_entire_table, view_contract_summary, view_contract_details, add_contract, update_contract
from setup import create_table, insert_data

# Setup db
root_dir = Path(__file__).parent
connection = sqlite3.connect(root_dir / 'cms.db')
cursor = connection.cursor()

# create_table(connection, cursor)
# insert_data(connection, cursor)

# view_contract_summary(cursor, id=54)
# view_contract_details(cursor, id=54)
# add_contract(
#     cursor, 
#     connection,
#     '2nd New Title',
#     'NewFakeVendor',
#     20,
#     'quarterly',
#     '2029-05-27'
# )

# view_entire_table(cursor)

update_contract(
    cursor=cursor, 
    id=54,
    title='Updated New Title',
    vendor='SecondFakeVendorName'
)

view_contract_details(cursor, id=54)

cursor.close()
connection.close()
import sqlite3
from argparse import ArgumentParser
from pathlib import Path
from queries import view_entire_table, view_contract_summary, view_contract_details, add_contract, update_contract, delete_contract
from setup import create_table, insert_data

# Set up database
root_dir = Path(__file__).parent
database = root_dir / 'cms.db'

connection = sqlite3.connect(database)
cursor = connection.cursor()

if database.stat().st_size == 0:
    create_table(connection, cursor)   
    insert_data(connection, cursor)
    print('Database created.')

# Set up argparse
parser = ArgumentParser()

parser.add_argument('--view-table', action='store_true', help='View the entire table')
parser.add_argument('--summary', type=int, help='View summary by contract ID')
parser.add_argument('--details', type=int, help='View details by contract ID')
parser.add_argument('--add', action='store_true', help='Add a new contract')
parser.add_argument('--update', type=int, help='Update a contract by ID')
parser.add_argument('--delete', type=int, help='Delete a contract by ID')

args = parser.parse_args()

# Command Line Interface
if args.view_table:
    view_entire_table(cursor)
elif args.summary:
    input_id = args.summary
    view_contract_summary(cursor, id=input_id)
elif args.details:
    input_id = args.details
    view_contract_details(cursor, id=input_id)
elif args.add:
    input_title = input('Title: ')    
    input_vendor = input('Vendor: ')
    input_cost = input('Cost: ')
    input_pay_cycle = input('Pay Cycle: ')
    input_expires_on = input('Expiration Date (yyyy-mm-dd): ')
    add_contract(
        cursor,
        connection,
        title=input_title,
        vendor=input_vendor,
        cost=input_cost,
        pay_cycle=input_pay_cycle,
        expires_on=input_expires_on
    )
elif args.update:
    input_id = args.update
    input_title = input('Title: ')    
    input_vendor = input('Vendor: ')
    input_cost = input('Cost: ')
    input_pay_cycle = input('Pay Cycle: ')
    input_expires_on = input('Expiration Date (yyyy-mm-dd): ')
    update_contract(
        cursor,
        connection,
        id=input_id,
        title=input_title,
        vendor=input_vendor,
        cost=input_cost,
        pay_cycle=input_pay_cycle,
        expires_on=input_expires_on
    )
elif args.delete:
    input_id = args.delete
    delete_contract(cursor, connection, id=input_id)
else:
    print('No arguments given. Use -h or --help for more information.')

cursor.close()
connection.close()
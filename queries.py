def select_all(cursor: object):
    cursor.execute('''SELECT * FROM Contracts''')
    results = cursor.fetchall()
    for row in results:
        print(row)

def create_table(cursor: object):
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Contracts(
            id INTEGER PRIMARY KEY,
            title TEXT,
            vendor TEXT,
            cost REAL,
            pay_cycle TEXT,
            expires_on TEXT)
    ''')
        
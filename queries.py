def select_all(cursor: object):
    cursor.execute('''SELECT * FROM Contracts''')
    results = cursor.fetchall()
    for row in results:
        print(row)
        
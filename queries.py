def select_all(cursor: object):
    cursor.execute('''SELECT * FROM Contracts''')
    results = cursor.fetchall()
    for row in results:
        print(row)

def view_contract_summary(cursor: object, id: int):
    cursor.execute('''
        SELECT
            id,
            title,
            CASE
                WHEN pay_cycle = 'yearly' THEN cost
                WHEN pay_cycle = 'quarterly' THEN cost * 4
                WHEN pay_cycle = 'monthly' THEN cost * 12
                WHEN pay_cycle = 'weekly' THEN cost * 52
                ELSE NULL
                END AS annual_cost,
            expires_on
        FROM Contracts
        WHERE id = ?''',
        (id,)
    )
    results = cursor.fetchall()

    headers = []
    for description in cursor.description:
        headers.append(description[0])
    header =' | '.join(headers)

    print(header)
    print('-' * len(header))    
    
    for row in results:
        print(' | '.join(str(value) for value in row))

def view_contract_details(cursor: object, id: int):
    cursor.execute('''SELECT * FROM Contracts WHERE id = ?''', (id,))
    results = cursor.fetchall()
    
    headers = []
    for description in cursor.description:
        headers.append(description[0])
    header =' | '.join(headers)

    print(header)
    print('-' * len(header))

    for row in results:
        print(' | '.join(str(value) for value in row))
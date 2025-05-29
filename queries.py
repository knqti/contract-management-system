def view_entire_table(cursor: object):
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

def add_contract(
    cursor: object,
    connection: object,
    title: str,
    vendor: str,
    cost: int,
    pay_cycle: str,
    expires_on: str
):        
    insert_values = {
        'title': title,
        'vendor': vendor,
        'cost': cost,
        'pay_cycle': pay_cycle,
        'expires_on': expires_on
    }
    cursor.execute('''
        INSERT INTO Contracts (
            title,
            vendor,
            cost,
            pay_cycle,
            expires_on)
        VALUES (
            :title,
            :vendor,
            :cost,
            :pay_cycle,
            :expires_on)''',
        insert_values
    )
    connection.commit()

def update_contract(
    cursor: object,
    id: int,
    title: str=None,
    vendor: str=None,
    cost: int=None,
    pay_cycle: str=None,
    expires_on: str=None
):
    update_values = {
        'title': title,
        'vendor': vendor,
        'cost': cost,
        'pay_cycle': pay_cycle,
        'expires_on': expires_on
    }
    
    # Remove None values
    update_values = {key: value for key, value in update_values.items() if value is not None}
    
    if not update_values:
        print('No fields to update')
        return
    
    # Add the id to the parameters
    update_values['id'] = id
    
    # Build SET clause
    set_clause = ', '.join([f'{key} = :{key}' for key in update_values.keys() if key != 'id'])
    
    # Single UPDATE query for all fields
    cursor.execute(f'''
        UPDATE Contracts
        SET {set_clause}
        WHERE id = :id''',
        update_values
    )
    
    print(f'Updated contract {id}\n')

def delete_contract(cursor: object, connection: object, id: int):
    cursor.execute('DELETE FROM Contracts WHERE id = ?', (id,))

    # Check number of rows affected by last query
    if cursor.rowcount == 0:
        print(f'ID {id} not found. Nothing deleted.')
        return

    connection.commit()
    print(f'ID {id} row deleted.')
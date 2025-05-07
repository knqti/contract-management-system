def create_table(connection: object, cursor: object):
    cursor.execute(
        '''CREATE TABLE IF NOT EXISTS Contracts(
            id INTEGER PRIMARY KEY,
            title TEXT,
            vendor TEXT,
            cost REAL,
            pay_cycle TEXT,
            expires_on TEXT)'''
    )
    connection.commit()

def insert_data(connection: object, cursor: object):
    test_data = [
        ('CRM Enterprise License', 'Salesforce', 3500.00, 'yearly', '2027-01-15'),
        ('Cloud Storage Solution', 'Amazon AWS', 799.50, 'monthly', '2026-08-22'),
        ('Email Marketing Platform', 'Mailchimp', 349.99, 'monthly', '2025-11-30'),
        ('Video Conferencing', 'Zoom', 249.95, 'monthly', '2026-04-10'),
        ('Accounting Software', 'Intuit', 599.00, 'yearly', '2026-03-05'),
        ('HR Management System', 'Workday', 1250.00, 'monthly', '2027-06-30'),
        ('Project Management Tool', 'Atlassian', 450.00, 'yearly', '2025-09-15'),
        ('Customer Support Software', 'Zendesk', 375.00, 'monthly', '2026-02-28'),
        ('Analytics Platform', 'Google', 799.00, 'monthly', '2025-12-01'),
        ('Design Software Suite', 'Adobe', 899.99, 'yearly', '2026-07-15'),
        ('VPN Service Enterprise', 'NordVPN', 299.50, 'yearly', '2025-10-31'),
        ('VoIP Phone System', 'RingCentral', 450.00, 'monthly', '2026-05-15'),
        ('Content Management System', 'WordPress', 199.99, 'yearly', '2025-11-20'),
        ('Security Software License', 'Symantec', 750.00, 'yearly', '2026-08-05'),
        ('Database Management', 'MongoDB', 675.00, 'monthly', '2027-02-15'),
        ('ERP System License', 'SAP', 4500.00, 'yearly', '2028-01-31'),
        ('Marketing Automation', 'HubSpot', 899.00, 'monthly', '2026-03-25'),
        ('Cloud Backup Service', 'Dropbox', 249.00, 'monthly', '2025-12-15'),
        ('Social Media Management', 'Hootsuite', 325.00, 'monthly', '2026-06-30'),
        ('eSignature Solution', 'DocuSign', 399.00, 'yearly', '2025-10-10'),
        ('Data Visualization Tool', 'Tableau', 850.00, 'yearly', '2026-04-20'),
        ('Website Hosting Service', 'GoDaddy', 179.99, 'yearly', '2025-11-05'),
        ('Inventory Management', 'Fishbowl', 695.00, 'monthly', '2026-09-15'),
        ('Antivirus Enterprise', 'McAfee', 399.99, 'yearly', '2026-02-28'),
        ('Recruitment Platform', 'LinkedIn', 550.00, 'monthly', '2025-12-31'),
        ('Calendar & Scheduling App', 'Calendly', 150.00, 'yearly', '2026-01-15'),
        ('Business Intelligence Tool', 'Power BI', 499.99, 'monthly', '2026-07-31'),
        ('Team Communication', 'Slack', 275.00, 'monthly', '2025-11-30'),
        ('Customer Feedback System', 'SurveyMonkey', 225.00, 'yearly', '2026-05-15'),
        ('Time Tracking Software', 'Toggl', 199.00, 'monthly', '2026-03-01'),
        ('Call Center Software', 'Five9', 795.00, 'monthly', '2026-08-31'),
        ('Network Monitoring Tool', 'SolarWinds', 899.00, 'yearly', '2026-01-20'),
        ('Email Security Gateway', 'Mimecast', 650.00, 'yearly', '2026-04-30'),
        ('Help Desk Solution', 'Freshdesk', 325.00, 'monthly', '2025-12-15'),
        ('Document Management', 'Box', 275.00, 'monthly', '2026-06-10'),
        ('Performance Monitoring', 'New Relic', 550.00, 'monthly', '2026-03-15'),
        ('Development Environment', 'JetBrains', 649.00, 'yearly', '2026-01-31'),
        ('Web Conferencing', 'Webex', 299.99, 'monthly', '2025-11-30'),
        ('Shipping Management', 'ShipStation', 199.95, 'monthly', '2026-05-15'),
        ('Asset Management System', 'AssetCloud', 450.00, 'yearly', '2026-02-28'),
        ('AI Customer Service', 'Intercom', 875.00, 'monthly', '2026-09-30'),
        ('API Management Platform', 'Apigee', 1250.00, 'yearly', '2027-04-15'),
        ('Mobile Device Management', 'AirWatch', 550.00, 'monthly', '2026-03-31'),
        ('Password Management', 'LastPass', 299.00, 'yearly', '2025-12-15'),
        ('Event Management Software', 'Cvent', 795.00, 'yearly', '2026-06-30'),
        ('Video Hosting Service', 'Vimeo', 199.99, 'monthly', '2026-01-15'),
        ('Graphic Design Platform', 'Canva', 249.95, 'yearly', '2025-11-30'),
        ('Web Analytics Tool', 'Matomo', 399.00, 'yearly', '2026-04-30'),
        ('Learning Management System', 'Cornerstone', 675.00, 'monthly', '2026-07-15'),
        ('Applicant Tracking System', 'Greenhouse', 499.00, 'monthly', '2026-03-31')
    ]
    cursor.executemany(
        '''INSERT INTO Contracts(
        title, vendor, cost, pay_cycle, expires_on)
        VALUES(?, ?, ?, ?, ?)''',
        test_data
    )
    connection.commit()
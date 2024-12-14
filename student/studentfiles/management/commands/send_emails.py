import smtplib
import datetime
import sqlite3

# Connect to the database
conn = sqlite3.connect(r'C:\Users\LENOVO\Desktop\student\db.sqlite3')
cursor = conn.cursor()

# Get records with end dates within a certain range
today = datetime.date.today()
query = f"SELECT email FROM studentfiles_Student WHERE last_date = '{today}'"
cursor.execute(query)
records_to_notify = cursor.fetchall()

# Send emails
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'monishamonisha0095@gmail.com'
smtp_password = 'qeyh feub qzyl units'

for record in records_to_notify:
    recipient_email = record[0]
    subject = 'Fees Pay remainder'
    message ='Today is the last date To Pay Your Fee 12.00'
    
    # Use an email library to send the email
    # smtplib is a basic example, but you may want to use a more advanced library
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()  # Add this line if your server requires TLS
    # Your email sending logic he
        server.login(smtp_username, smtp_password)
        server.sendmail(smtp_username, recipient_email, f'Subject: {subject}\n\n{message}')

# Close the database connection
print("Mail sent")
conn.close()

import datetime

file=open(r'C:\Users\LENOVO\Desktop\student\studentfiles\management\commands\output.txt','a')

file.write(f'{datetime.datetime.now()}-the script ran\n')
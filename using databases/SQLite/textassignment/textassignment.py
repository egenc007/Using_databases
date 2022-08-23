#This application will read the mailbox data (mbox.txt) 
#and count the number of email messages per organization 
#(i.e. domain name of the email address) using a database 
#with the following schema to maintain the counts

#Use mbox.txt

import sqlite3

#make a connection
conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Counts''')

#Create the table
cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

#open the file and create a list
fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox.txt'
fh = open(fname)
list_1 =[]


for line in fh:
    #find the data that startswith From
    if not line.startswith('From: '): continue
    pieces = line.split()
    #email is the second piece
    email = pieces[1]
    dom = email.find('@')
    #get the data that starts with @ till the length of the email
    org = email[dom+1:len(email)]
    
    #select count from database. 
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))

    #the information we are going to get from the database. get the first one
    row = cur.fetchone()
    #if row doesnt exists insert a column
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (org,))

    #if it exists epdate to this
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (org,))

#commit to database
conn.commit()

#Get the top ten
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

#row sub 0 is email and row sub 1 is count
for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
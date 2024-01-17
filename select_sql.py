import mysql.connector
try:
    conn = mysql.connector.connect(
        user = "userpython",
        host = "localhost",
        passwd ="123456",
        database ="arabicinfo"
        )
    cur =conn.cursor()
    cur.execute("select * from emp")
    for x in cur:
        print(x)
    for x in cur:
        print(x[0]) # this is will print first column
except mysql.connector.Error as e:
    print(e)
    

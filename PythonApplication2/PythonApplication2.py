
import requests
import json
import pyodbc 


url = "https://www.meistertask.com/api/projects"

headers = {
    'Accept': "*/*",
    'Authorization': "Bearer 8f9e4e59272232742edb40c5416b4012e4730cd00964d4fa6d896e010d32b4f4",
    'accept-encoding': "gzip, deflate"
    }

response = requests.request("GET", url, headers=headers)
input = response.text

print(type(input))

y = json.loads(input)

#print('parameter count:', len(y))

#tp = y[0]
for tp in y:
    for x, y in tp.items():
      print(x, y)

def create(conn):
    print("Create")
    cursor =  conn.cursor()
    cursor.execute('insert into dummy(a,b) values(?,?);',
                   ('cat',3232)
    )
    conn.commit()

conn = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=BB\SQLEXPRESS;"
    "Database=PyTest;"
    "Trusted_Connection=yes;"
    )

create(conn)

conn.close()

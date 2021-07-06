import requests
import mysql.connector
from bs4 import BeautifulSoup


url="https://www.google.com"
page=requests.get(url)
a=BeautifulSoup(page.text,'html.parser')
print(a.find_all("a"))

mydb=mysql.connector.connect(host="localhost",user="root",password="Magendra6the",database="mydatabase")
dbse=mydb.cursor()
dbse.execute("CREATE TABLE SCRAP (htm VARCHAR(2500),by INT")
dbse.execute("""INSERT INTO SCRAP VALUES(a.find_all("a"))""")
dbse.execute("SELECT * FROM SCRAP WHERE by>10 ")
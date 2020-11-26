import pandas as pd
import csv
import mysql.connector

# https://www.nelsontang.com/odbc-in-OSX/

data = pd.read_csv(r'/Users/duyanh2103/desktop/python/customer.csv')
df = pd.DataFrame(data, columns = ['customerid','firstname','lastname','companyname'
	, 'billingaddress1', 'billingaddress2', 'city', 'state', 'postalcode', 'country', 
	'phonenumber','emailaddress', 'createddate'])
# first way of reading a csv file
# print(df)

conn = mysql.connector.connect(host="localhost",user="root",passwd="Duyanh123!",database = "testdatabase"
	,auth_plugin="mysql_native_password") #struggling with server connection for 5 hours zzzz
print(conn)
if(conn):
	print("Successful")
else:
	print("Failed")
cursor = conn.cursor()

fname = "customer.csv"
with open(fname) as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	for row in csv_reader:
		for i,x in enumerate(row): #trying to fix the bug with changing all empty values to 0
			if len(x)< 1:
				x = row[i] = 0
		customerid = row[0]
		firstname = row[1]
		lastname = row[2]
		companyname = row[3]
		billingaddress1 = row[4]
		billingaddress2 = row[5]
		city = row[6]
		state = row[7]
		postalcode = row[8]
		country = row[9]
		phonenumber = row[10]
		emailaddress = row[11]
		createddate = row[12]
		cursor.execute('''INSERT INTO testdatabase.customer_info(customerid, firstname, lastname, companyname, billingaddress1, billingaddress2, city, state, postalcode, country,phonenumber, emailaddress,createddate) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''',(customerid, firstname, lastname, companyname, billingaddress1, billingaddress2, city, state, postalcode, country,phonenumber, emailaddress,createddate))
		conn.commit()
    # cursor.execute('INSERT INTO customer_info (customerid, firstname, lastname, companyname, billingaddress1, billingaddress2, city, state, postalcode, country,phonenumber, emailaddress,createddate) VALUES ({}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {})'.format(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12])

cursor.execute("SELECT * FROM customer_info")
result = cursor.fetchall()
for x in result:
	print(x)



    #######
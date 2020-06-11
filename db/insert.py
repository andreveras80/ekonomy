import os
import psycopg2

try:
   DATABASE_URL = os.environ['DATABASE_URL']
   connection = psycopg2.connect(DATABASE_URL, sslmode='require')

#   connection = psycopg2.connect(user="sysadmin",
#                                  password="pynative@#29",
#                                  host="127.0.0.1",
#                                  port="5432",
#                                  database="postgres_db")
   
   cursor = connection.cursor()

   postgres_insert_query = """ INSERT INTO tb_gdp (DATE, VALUE) VALUES (%s,%s)"""
   record_to_insert = ('2010-01-01', 950.0)
   cursor.execute(postgres_insert_query, record_to_insert)

   connection.commit()
   count = cursor.rowcount
   print (count, "Record inserted successfully into mobile table")

except (Exception, psycopg2.Error) as error :
    if(connection):
        print("Failed to insert record into mobile table", error)

finally:
    #closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")

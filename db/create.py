import psycopg2
from psycopg2 import Error

try:

    DATABASE_URL = os.environ['DATABASE_URL']
    connection = psycopg2.connect(DATABASE_URL, sslmode='require')

#    connection = psycopg2.connect(user = "postgres",
#                                  password = "pass@#29",
#                                  host = "127.0.0.1",
#                                  port = "5432",
#                                  database = "postgres_db")

    cursor = connection.cursor()
    
    create_table_query = '''CREATE TABLE tb_gdp
          (id serial PRIMARY KEY, 
           DATE date NOT NULL,
           VALUE REAL NOT NULL); '''
    
    cursor.execute(create_table_query)
    connection.commit()
    print("Table created successfully in PostgreSQL ")

except (Exception, psycopg2.DatabaseError) as error :
    print ("Error while creating PostgreSQL table", error)
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

import psycopg2
from config import config

def select_all(query, values=None):
    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(query, values)
        #return value
        data = cur.fetchall()
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Could not select data, database error: ", error)
    finally:
        if conn is not None:
            conn.close()

    return data

def select_one(query, values=None):
    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(query, values)
        #return value
        data = cur.fetchone()
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Could not select data, database error: ", error)
    finally:
        if conn is not None:
            conn.close()

    return data

def insert_data(sql, values):
    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, values)
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Could not insert data, database error: ", error)
    finally:
        if conn is not None:
            conn.close()

def update_data(sql, values):
    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, values)
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Could not update data, database error: ", error)
    finally:
        if conn is not None:
            conn.close()

def deletete_data(sql, values):
    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, values)
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Could not delete data, database error: ", error)
    finally:
        if conn is not None:
            conn.close()

# def connect():
#     """ Connect to the PostgreSQL database server """
#     conn = None
#     try:
#         # read connection parameters
#         params = config()

#         # connect to the PostgreSQL server
#         print('Connecting to the PostgreSQL database...')
#         conn = psycopg2.connect(**params)
		
#         # create a cursor
#         cur = conn.cursor()
        
# 	# execute a statement
#         print('PostgreSQL database version:')
#         cur.execute('SELECT version()')

#         # display the PostgreSQL database server version
#         db_version = cur.fetchone()
#         print(db_version)
       
# 	# close the communication with the PostgreSQL
#         cur.close()
#     except (Exception, psycopg2.DatabaseError) as error:
#         print(error)
#     finally:
#         if conn is not None:
#             conn.close()
#             print('Database connection closed.')


# if __name__ == '__main__':
#     sql = """SELECT * FROM movies ORDER BY movie_length;"""
#     #value = ('Frozen', )
#     movies = select_all(sql)
#     #movie = select_one(sql)
#     print(movies)
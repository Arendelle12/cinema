import psycopg2
from config import config

def select_all(query, values=None):
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(query, values)
        data = cur.fetchall()
        conn.commit()
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
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(query, values)
        data = cur.fetchone()
        conn.commit()
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
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, values)
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Could not insert data, database error: ", error)
    finally:
        if conn is not None:
            conn.close()

def insert_data_returning(sql, values):
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, values)
        index = cur.fetchone()[0]
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Could not insert data, database error: ", error)
    finally:
        if conn is not None:
            conn.close()
    
    return index

def update_data(sql, values):
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, values)
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Could not update data, database error: ", error)
    finally:
        if conn is not None:
            conn.close()

def delete_data(sql, values):
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, values)
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Could not delete data, database error: ", error)
    finally:
        if conn is not None:
            conn.close()

def calculate_price(price, discount):
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.callproc('price_after_discount', (price, discount))
        row = cur.fetchone()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return row

if __name__ == '__main__':
    #sql = """SELECT * FROM movies ORDER BY movie_length;"""
    #value = ('Frozen', )
    #movies = select_all(sql)
    #movie = select_one(sql)
    #print(movies)
    res = calculate_price(30, 50)
    print(res[0])
import psycopg2
from config import config


def insert_movie(title, year_of_production, movie_length):
    """ insert values into tables """
    sql = """INSERT INTO movies(title, year_of_production, movie_length)
             VALUES(%s,%s,%s);"""
    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (title, year_of_production, movie_length))
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def insert_hall(number_of_seats, number_of_free_seats):
    """ insert values into tables """
    sql = """INSERT INTO halls(hall_number, number_of_seats, number_of_free_seats)
             VALUES(nextval('hall_number_seq'),%s,%s) RETURNING hall_number;"""
    conn = None
    hall_number = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (number_of_seats, number_of_free_seats))
        # get the generated hall number back
        hall_number = cur.fetchone()[0]
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return hall_number

def insert_customer(first_name, last_name, email, phone_number):
    """ insert values into tables """
    sql = """INSERT INTO customers
             VALUES(nextval('customer_id_seq'),%s,%s,%s,%s);"""
    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (first_name, last_name, email, phone_number))
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def insert_discount(type_of_discount, discount):
    """ insert values into tables """
    sql = """INSERT INTO discounts
             VALUES(nextval('discount_id_seq'),%s,%s);"""
    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (type_of_discount, discount))
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def insert_screening(screening_time, screening_date, hall_number, title, year_of_production):
    """ insert values into tables """
    sql = """INSERT INTO screenings
             VALUES(nextval('screening_id_seq'),%s,%s,%s,%s,%s);"""
    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (screening_time, screening_date, hall_number, title, year_of_production))
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def insert_order(customer_id):
    """ insert values into tables """
    sql = """INSERT INTO orders
             VALUES(nextval('order_id_seq'),%s);"""
    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (customer_id,))
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def insert_ticket(price, percent_discount, number_of_seat, order_id, discount_id, screening_id):
    """ insert values into tables """
    sql = """INSERT INTO tickets(ticket_id, price, percent_discount, number_of_seat, order_id, discount_id, screening_id)
             VALUES(nextval('ticket_id_seq'),%s,%s,%s,%s,%s,%s);"""
    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (price, percent_discount, number_of_seat, order_id, discount_id, screening_id))
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    # insert record
    # insert_movie('Frozen', 2013, 108)
    # insert_hall(30, 16)
    # insert_customer('John', 'Smith', 'john.smith@mail.com', None)
    # insert_discount('student', 50)
    # insert_screening('12:00', '2020-01-14', 1, 'Frozen', 2013)
    # insert_order(2)
    insert_ticket(30, None, 14, 1, None, 1)
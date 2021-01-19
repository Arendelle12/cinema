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
    # insert_ticket(30, None, 14, 1, None, 1)
    # insert_movie('Knives Out', 2019, 130)
    # insert_movie('Intouchables', 2011, 112)
    # insert_movie('The Avengers', 2012, 142)
    # insert_movie('Joker', 2019, 122)
    # insert_movie('Soul', 2020, 90)
    # insert_movie('Jojo Rabbit', 2019, 108)
    # insert_movie('Inception', 2010, 148)
    # insert_movie('Titanic', 1997, 194)
    # insert_movie('Marriage Story', 2019, 136)

    # insert_discount('family', 30)

    # insert_hall(50, 50)
    # insert_hall(40, 40)
    # insert_hall(35, 35)

    # insert_screening('15:00', '2020-01-14', 1, 'Frozen', 2013)
    # insert_screening('15:00', '2020-01-15', 2, 'Frozen', 2013)
    # insert_screening('10:00', '2020-01-15', 2, 'Frozen', 2013)
    # insert_screening('12:30', '2020-01-15', 3, 'Frozen', 2013)
    # insert_screening('11:00', '2020-01-16', 3, 'Frozen', 2013)

    # insert_screening('20:00', '2020-01-14', 2, 'Knives Out', 2019)
    # insert_screening('20:00', '2020-01-15', 3, 'Knives Out', 2019)
    # insert_screening('20:00', '2020-01-16', 2, 'Knives Out', 2019)

    # insert_screening('17:00', '2020-01-14', 4, 'Intouchables', 2011)
    # insert_screening('17:00', '2020-01-16', 4, 'Intouchables', 2011)

    # insert_screening('18:00', '2020-01-14', 1, 'The Avengers', 2012)
    # insert_screening('18:00', '2020-01-15', 1, 'The Avengers', 2012)
    # insert_screening('17:00', '2020-01-15', 2, 'The Avengers', 2012)
    # insert_screening('20:00', '2020-01-17', 2, 'The Avengers', 2012)
    # insert_screening('19:00', '2020-01-16', 3, 'The Avengers', 2012)

    # insert_screening('20:00', '2020-01-14', 3, 'Joker', 2019)
    # insert_screening('15:00', '2020-01-15', 3, 'Joker', 2019)
    # insert_screening('20:00', '2020-01-17', 3, 'Joker', 2019)

    # insert_screening('10:00', '2020-01-15', 4, 'Soul', 2020)
    # insert_screening('14:00', '2020-01-15', 4, 'Soul', 2020)

    # insert_screening('16:00', '2020-01-16', 2, 'Jojo Rabbit', 2019)
    # insert_screening('13:00', '2020-01-16', 2, 'Jojo Rabbit', 2019)
    # insert_screening('16:00', '2020-01-14', 2, 'Jojo Rabbit', 2019)
    # insert_screening('13:00', '2020-01-17', 2, 'Jojo Rabbit', 2019)

    # insert_screening('20:00', '2020-01-14', 4, 'Inception', 2010)

    # insert_screening('18:00', '2020-01-15', 4, 'Titanic', 1997)
    # insert_screening('13:00', '2020-01-14', 4, 'Titanic', 1997)

    # insert_screening('11:00', '2020-01-16', 1, 'Marriage Story', 2019)
    # insert_screening('14:00', '2020-01-16', 1, 'Marriage Story', 2019)
    # insert_screening('17:00', '2020-01-16', 1, 'Marriage Story', 2019)
    insert_screening('20:00', '2020-01-16', 1, 'Marriage Story', 2019)
    

import psycopg2
from config import config


def create_sequences():
    """ create sequences in the PostgreSQL database"""
    commands = (
        """
        CREATE SEQUENCE customer_id_seq
        AS SMALLINT
        INCREMENT BY 1
        MINVALUE 1
        MAXVALUE 999
        OWNED BY customers.customer_id
        """,
        """
        CREATE SEQUENCE order_id_seq
        AS SMALLINT
        INCREMENT BY 1
        MINVALUE 1
        MAXVALUE 999
        OWNED BY orders.order_id
        """,
        """
        CREATE SEQUENCE ticket_id_seq
        AS SMALLINT
        INCREMENT BY 1
        MINVALUE 1
        MAXVALUE 999
        OWNED BY tickets.ticket_id
        """,
        """
        CREATE SEQUENCE discount_id_seq
        AS SMALLINT
        INCREMENT BY 1
        MINVALUE 1
        MAXVALUE 999
        OWNED BY discounts.discount_id
        """,
        """
        CREATE SEQUENCE screening_id_seq
        AS SMALLINT
        INCREMENT BY 1
        MINVALUE 1
        MAXVALUE 999
        OWNED BY screenings.screening_id
        """,
        """
        CREATE SEQUENCE hall_number_seq
        AS SMALLINT
        INCREMENT BY 1
        MINVALUE 1
        MAXVALUE 99
        OWNED BY halls.hall_number
        """,
        """
        CREATE SEQUENCE hall_one
        AS SMALLINT
        INCREMENT BY 1
        MINVALUE 1
        MAXVALUE 30
        OWNED BY halls.number_of_free_seats
        """,
        """
        CREATE SEQUENCE hall_two
        AS SMALLINT
        INCREMENT BY 1
        MINVALUE 1
        MAXVALUE 50
        OWNED BY halls.number_of_free_seats
        """,
        """
        CREATE SEQUENCE hall_three
        AS SMALLINT
        INCREMENT BY 1
        MINVALUE 1
        MAXVALUE 40
        OWNED BY halls.number_of_free_seats
        """,
        """
        CREATE SEQUENCE hall_four
        AS SMALLINT
        INCREMENT BY 1
        MINVALUE 1
        MAXVALUE 35
        OWNED BY halls.number_of_free_seats
        """)
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create sequence one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    create_sequences()
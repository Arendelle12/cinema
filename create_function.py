import psycopg2
from config import config


def create_function():
    """ create function in the PostgreSQL database"""
    commands = (
        """
        CREATE OR REPLACE FUNCTION price_after_discount(price numeric, discount numeric)
        RETURNS numeric
        LANGUAGE plpgsql
        AS
        $$
        DECLARE calculated_price numeric;
        BEGIN
        calculated_price := (100 - discount)/100 * price;
        RETURN calculated_price;
        END;
        $$
        """)
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        
        #for command in commands:
        cur.execute(commands)
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
    create_function()
import psycopg2
from config import config


def create_procedure():
    commands = (
        """
        CREATE OR REPLACE PROCEDURE update_user(
            p_first_name VARCHAR,
            p_last_name VARCHAR,
            p_email VARCHAR,
            p_phone_number VARCHAR
        )
        LANGUAGE plpgsql
        AS
        $$
        BEGIN
        UPDATE customers
        SET email = p_email, phone_number = p_phone_number
        WHERE first_name = p_first_name AND last_name = p_last_name;
        END;
        $$
        """)
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(commands)
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    create_procedure()
import psycopg2
from config import config


def create_index():
    commands = (
        """
        CREATE INDEX idx_screenings
        ON screenings(title);
        """,
        """
        CREATE INDEX idx_tickets
        ON tickets(order_id);
        """)
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        for command in commands:
            cur.execute(command)
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    create_index()
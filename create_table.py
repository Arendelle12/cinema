import psycopg2
from config import config


def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE movies (
            title VARCHAR(30),
            year_of_production SMALLINT,
            movie_length SMALLINT NOT NULL,
            PRIMARY KEY (title, year_of_production)
        )
        """,
        """
        CREATE TABLE halls (
            hall_number NUMERIC(2) PRIMARY KEY, 
            number_of_seats NUMERIC(2) NOT NULL,
            number_of_free_seats NUMERIC(2) NOT NULL,
            CONSTRAINT chk_num_of_seats CHECK(number_of_free_seats <= number_of_seats)
        )
        """,
        """
        CREATE TABLE customers (
            customer_id NUMERIC(3) PRIMARY KEY,
            first_name VARCHAR(20) NOT NULL,
            last_name VARCHAR(20) NOT NULL,
            email VARCHAR(30),
            phone_number VARCHAR(15)
        )
        """,
        """
        CREATE TABLE discounts (
            discount_id NUMERIC(3) PRIMARY KEY,
            type_of_discount VARCHAR(10) NOT NULL,
            discount NUMERIC(3) NOT NULL CONSTRAINT chk_discount CHECK(discount BETWEEN 0 AND 100)
        )
        """,
        """
        CREATE TABLE screenings (
            screening_id NUMERIC(3) PRIMARY KEY,
            screening_time TIME NOT NULL,
            screening_date DATE NOT NULL,
            hall_number NUMERIC(2) NOT NULL,
            title VARCHAR(30) NOT NULL,
            year_of_production SMALLINT NOT NULL,
            CONSTRAINT fk_movie FOREIGN KEY(title, year_of_production) REFERENCES movies(title, year_of_production) ON DELETE CASCADE,
            CONSTRAINT fk_hall FOREIGN KEY(hall_number) REFERENCES halls(hall_number) ON DELETE CASCADE
        )
        """,
        """
        CREATE TABLE orders (
            order_id NUMERIC(3) PRIMARY KEY,
            customer_id NUMERIC(3) NOT NULL,
            CONSTRAINT fk_customer FOREIGN KEY(customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE
        )
        """,
        """
        CREATE TABLE tickets ( 
            ticket_id NUMERIC(3) PRIMARY KEY,
            type_of_ticket VARCHAR(10) NOT NULL DEFAULT 'regular',
            price NUMERIC(6, 2) NOT NULL CONSTRAINT chk_price CHECK(price > 0),
            percent_discount NUMERIC(3) CONSTRAINT chk_percent_discount CHECK(percent_discount BETWEEN 0 AND 100),
            number_of_seat NUMERIC(2) NOT NULL CONSTRAINT chk_seat CHECK(number_of_seat > 0),
            order_id NUMERIC(3) NOT NULL,
            discount_id NUMERIC(3),
            screening_id NUMERIC(3) NOT NULL,
            CONSTRAINT fk_order FOREIGN KEY(order_id) REFERENCES orders(order_id) ON DELETE CASCADE,
            CONSTRAINT fk_discount FOREIGN KEY(discount_id) REFERENCES discounts(discount_id) ON DELETE CASCADE,
            CONSTRAINT fk_screening FOREIGN KEY(screening_id) REFERENCES screenings(screening_id) ON DELETE CASCADE
        )
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
    create_tables()
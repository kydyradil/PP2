import psycopg2
from config import load_config


config = load_config()

with psycopg2.connect(**config) as conn:
    with conn.cursor() as cur:
        cur.execute(
            """
            CREATE TABLE users (
                username VARCHAR(255) NOT NULL,
                level INT,
                score INT,
                GAatS BOOL,
                direction VARCHAR(255)
            )
            """
            )
        cur.execute(
            """
            CREATE TABLE coords (
                username VARCHAR(255) NOT NULL,
                x1 INT,
                y1 INT,
                x2 INT,
                y2 INT,
                x3 INT,
                y3 INT,
                x4 INT,
                y4 INT,
                x5 INT,
                y5 INT,
                x6 INT,
                y6 INT,
                x7 INT,
                y7 INT,
                x8 INT,
                y8 INT,
                x9 INT,
                y9 INT,
                ax INT,
                ay INT,
                av INT
            )
            """
            )
    conn.commit()
import psycopg2
from config import load_config


config = load_config()

with psycopg2.connect(**config) as conn:
    with conn.cursor() as cur:
        cur.execute("DROP TABLE users;")
        cur.execute("DROP TABLE coords;")
    conn.commit()
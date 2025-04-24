import psycopg2
import csv
from config import load_config


def create_tables():
    """ Create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE phonebook (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(255) NOT NULL,
            last_name VARCHAR(255) NOT NULL,
            number VARCHAR(255) NOT NULL
        )
        """,)
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # execute the CREATE TABLE statement
                for command in commands:
                    cur.execute(command)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

def drop_tables():
    """ Drop tables in the PostgreSQL database"""
    commands = (
        """
        DROP TABLE phonebook;
        """,)
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # execute the CREATE TABLE statement
                for command in commands:
                    cur.execute(command)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

def insert_contacts(contacts_list):
    """ Insert multiple vendors into the vendors table  """
    sql = "INSERT INTO phonebook(first_name, last_name, number) VALUES(%s, %s, %s) RETURNING *"
    config = load_config()
    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                # execute the INSERT statement
                cur.executemany(sql, contacts_list)
            # commit the changes to the database
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def insert_contacts_csv(path):
    """ Insert multiple vendors into the vendors table from a csv file (with header) """
    sql = "INSERT INTO phonebook(first_name, last_name, number) VALUES(%s, %s, %s) RETURNING *"
    config = load_config()
    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                with open(path, 'r') as f:
                    reader = csv.reader(f, delimiter=";")
                    next(reader) # Skip header if present
                    for row in reader:
                        cur.execute(sql, row)
                # commit the changes to the database
                conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def update(filter, f_value, attribute, a_value):
    """ Update some attribute located in the same row as some other attribute (filter); those shall
     respectively be id (filter only)/first_name/last_name/number """
    updated_row_count = 0
    config = load_config()
    if filter not in ["id", "first_name", "last_name", "number"] or attribute not in ["first_name", "last_name", "number"]: 
            print("Incorrect data input")
            if attribute == "id": print("You cannot edit id's")
            return updated_row_count
    if filter == "id": sql = f"UPDATE phonebook SET {attribute} = '{a_value}' WHERE {filter} = {f_value};"
    else: sql = f"UPDATE phonebook SET {attribute} = '{a_value}' WHERE {filter} = '{f_value}';"
    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                # execute the UPDATE statement
                cur.execute(sql, (attribute, a_value, filter, f_value))
                updated_row_count = cur.rowcount
            # commit the changes to the database
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return updated_row_count

def filter(filt=None, specif=None):
    """ Sort the phonebook by some parameter or output specific coincidences """
    config  = load_config()
    sql = "SELECT * FROM phonebook;"
    if specif: sql = sql[:-1] + f" WHERE {specif};"
    if filt: sql = sql[:-1] + f" ORDER BY {filt};"
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql)
                rows = cur.fetchall()
                print("The number of parts: ", cur.rowcount)
                for row in rows:
                    print(row)
                print()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def delete(name=None, number=None):
    """ Delete record by full name or number """
    rows_deleted  = 0
    if name or number:
        sql = "DELETE FROM phonebook WHERE;"
        if name: sql = sql[:-1] + f" first_name = '{name[0]}' AND last_name = '{name[1]}';"
        if number: sql = sql[:-1] + f" number = '{number}';"
        config = load_config()
        try:
            with  psycopg2.connect(**config) as conn:
                with  conn.cursor() as cur:
                    # execute the UPDATE statement
                    cur.execute(sql)
                    rows_deleted = cur.rowcount
                # commit the changes to the database
                conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            return rows_deleted

if __name__ == '__main__':  
    drop_tables()
    create_tables()
    insert_contacts([("Arman", "Ahmetov", "7785286187"), ("Maksat", "Omarov", "77745896587"),
                    ("Piter", "Holland", "77777077787")])
    insert_contacts_csv("sample_data.csv")
    filter()
    update("last_name", "Margo", "first_name", "Enstain ")
    filter("id", "LOWER(first_name) LIKE 'va%'")
    delete(("Adil", "Kydyr"))
    filter()
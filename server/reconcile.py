import datetime
import uuid
import psycopg2

def store_data(conn, email, phone_number):
    linked_id = 0
    link_preference = "PRIMARY"
    created_at = str(datetime.datetime.now())
    updated_at = str(datetime.datetime.now())
    deleted_at = str(datetime.datetime.now())
    query = f"insert into contact(phone_number, email, linked_id, link_preference, created_at, updated_at, deleted_at) values ( {phone_number}, '{email}', {linked_id}, '{link_preference}', '{created_at}', '{updated_at}', '{deleted_at}')"

    conn.cursor().execute(query)
    conn.commit()

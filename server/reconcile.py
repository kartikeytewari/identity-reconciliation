import time
import datetime
import psycopg2

def store_data(conn, email, phone_number):
    local_id = 2
    phone_number = "'" + phone_number + "'"
    email = "'" + email + "'"
    linked_id = 0
    link_preference = "'" + "ALPHA" + "'"
    created_at = "'" + str(datetime.datetime.now()) + "'"
    updated_at = "'" + str(datetime.datetime.now()) + "'"
    deleted_at = "'" + str(datetime.datetime.now()) + "'"
    query = f'insert into contact(id, phone_number, email, linked_id, link_preference, created_at, updated_at, deleted_at) values ({local_id}, {phone_number}, {email}, {linked_id}, {link_preference}, {created_at}, {updated_at}, {deleted_at})'
    print ("query = ", query, flush=True)
    conn.cursor().execute(query)
    conn.commit()
import uuid
import psycopg2
import operator
import json
from datetime import datetime
from dataclasses import dataclass

@dataclass
class contact_detail:
    id: str = None
    linked_id: str = None
    link_preference: str = None
    created_at: datetime = None
    email: str = None
    phone_number: str = None

def multiple_contact_resp(primary_candidate):

    secondary_email_dir = set()
    secondary_phone_number_dir = set()
    secondary_contact_id_dir = set()

    primary_email = ""
    primary_phone_number = ""

    for local_contact in primary_candidate:
        if (local_contact.link_preference == "PRIMARY"):
            primary_email = local_contact.email
            primary_phone_number = local_contact.phone_number
        else:
            secondary_email_dir.add(local_contact.email)
            secondary_phone_number_dir.add(local_contact.phone_number)
            secondary_contact_id_dir.add(local_contact.id)

    if (primary_email in secondary_email_dir):
        secondary_email_dir.remove(primary_email)

    if (primary_phone_number in secondary_phone_number_dir):
        secondary_phone_number_dir.remove(primary_phone_number)

    val = {
        "contact": {
            "primaryContatctId": primary_candidate[0].id,
            "emails": [primary_email] + list(secondary_email_dir),
            "phoneNumbers": [primary_phone_number] + list(secondary_phone_number_dir),
            "secondaryContactIds": list(secondary_contact_id_dir)
        }
    }

    return json.dumps(val)

def get_contact(cursor, email, phone_number):
    # find all matching candidates
    query_link = f"select id, linked_id, link_preference, created_at, email, phone_number from contact where phone_number = '{phone_number}' or email = '{email}';"
    cursor.execute(query_link)
    same_contact = cursor.fetchall()


    for local_contact in same_contact:
        local_contact_type = local_contact[2]
        query_link = ""
        if (local_contact_type == "PRIMARY"):
            local_contact_id = local_contact[0]
            query_link = f"select id, linked_id, link_preference, created_at, email, phone_number from contact where linked_id = '{local_contact_id}';"
        else:
            local_contact_primary_id = local_contact[1]
            query_link = f"select id, linked_id, link_preference, created_at, email, phone_number from contact where linked_id = '{local_contact_primary_id}' or id = '{local_contact_primary_id}';"
        
    cursor.execute(query_link)
    same_contact += cursor.fetchall()

    primary_candidate = []
    for local_val in same_contact:
        temp = contact_detail()
        temp.id = local_val[0]
        temp.linked_id = local_val[1]
        temp.link_preference = local_val[2]
        temp.created_at = local_val[3]
        temp.email = local_val[4]
        temp.phone_number = local_val[5]
        primary_candidate.append(temp)

    primary_candidate.sort(key=operator.attrgetter('created_at'))
    return primary_candidate
    
def store_data(conn, email, phone_number):
    created_at = str(datetime.now())
    updated_at = str(datetime.now())
    
    cursor = conn.cursor()
    primary_candidate = get_contact(cursor, email, phone_number)

    # check for same contact set
    for local_contact in primary_candidate:
        if (local_contact.email == email) and (local_contact.phone_number == phone_number):
            return multiple_contact_resp(primary_candidate)

    query_write_local_contact = ""
    if (len(primary_candidate) == 0):
        # new customer
        query_write_local_contact = f"insert into contact(phone_number, email, link_preference, created_at, updated_at) values ( {phone_number}, '{email}', 'PRIMARY', '{created_at}', '{updated_at}')"
    else:
        # old customer
        primary_hash = ""
        if (primary_candidate[0].link_preference == "SECONDARY"):
            primary_hash = primary_candidate[0].linked_id 
        else:
            primary_hash = primary_candidate[0].id

        for i in range(1,len(primary_candidate)):
            if (primary_candidate[i].id != primary_hash) and ((primary_candidate[i].link_preference == "PRIMARY") or (primary_candidate[i].linked_id != primary_hash)):
                query_update = f"update contact set link_preference = 'SECONDARY', linked_id = '{primary_hash}' where id='{primary_candidate[i].id}';"
                cursor.execute(query_update)
                conn.commit()
    
        query_write_local_contact = f"insert into contact(phone_number, email, link_preference, LINKED_ID, created_at, updated_at) values ( {phone_number}, '{email}', 'SECONDARY', '{primary_hash}', '{created_at}', '{updated_at}')"
    
    cursor.execute(query_write_local_contact)
    conn.commit()

    primary_candidate = get_contact(cursor, email, phone_number)
    return multiple_contact_resp(primary_candidate)

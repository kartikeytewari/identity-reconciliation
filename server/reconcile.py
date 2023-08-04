import uuid
import psycopg2
import operator
from datetime import datetime
from dataclasses import dataclass

@dataclass
class contact_detail:
    id: str = None
    linked_id: str = None
    link_preference: str = None
    created_at: datetime = None

def store_data(conn, email, phone_number):
    created_at = str(datetime.now())
    updated_at = str(datetime.now())
    
    # find all matching candidates
    query_link = f"select id, linked_id, link_preference, created_at, email, phone_number from contact where phone_number = '{phone_number}' or email = '{email}';"
    cursor = conn.cursor()
    cursor.execute(query_link)
    same_contact = cursor.fetchall()

    primary_candidate = []
    for local_val in same_contact:
        temp = contact_detail()

        # check for same contact set
        if (local_val[4] == email) and (local_val[5] == phone_number):
            return
            
        temp.id = local_val[0]
        temp.linked_id = local_val[1]
        temp.link_preference = local_val[2]
        temp.created_at = local_val[3]
        primary_candidate.append(temp)

    primary_candidate.sort(key=operator.attrgetter('created_at'))
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
            if (primary_candidate[i].link_preference != "SECONDARY") or (primary_candidate[i].linked_id != primary_hash):
                query_update = f"update contact set link_preference = 'SECONDARY', linked_id = '{primary_hash}' where id='{primary_candidate[i].id}';"
                cursor.execute(query_update)
                conn.commit()
    
        query_write_local_contact = f"insert into contact(phone_number, email, link_preference, LINKED_ID, created_at, updated_at) values ( {phone_number}, '{email}', 'SECONDARY', '{primary_hash}', '{created_at}', '{updated_at}')"
    
    cursor.execute(query_write_local_contact)
    conn.commit()

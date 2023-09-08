-- install extension for UUID 
create extension pg_trgm;
select * FROM pg_extension;
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- create a table contact 
CREATE TABLE contact (
    ID uuid default uuid_generate_v4(),
    PHONE_NUMBER VARCHAR(10),
    EMAIL VARCHAR(255),
    LINKED_ID uuid DEFAULT NULL,
    LINK_PREFERENCE VARCHAR(20) NOT NULL,
    CREATED_AT TIMESTAMP NOT NULL,
    UPDATED_AT TIMESTAMP NOT NULL,
    DELETED_AT TIMESTAMP DEFAULT NULL,
    PRIMARY KEY (ID)
);

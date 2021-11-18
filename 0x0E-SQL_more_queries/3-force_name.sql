-- Creates the table force_name on your MySQL server.
CREATE TABLE IF NO EXISTS force_name(
    id INT,
    name VARCHAR(256) NOT NULL
    ...
    PRIMARY KEY (id, name)
    );

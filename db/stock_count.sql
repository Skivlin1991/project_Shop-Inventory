DROP TABLE IF EXISTS stock;
DROP TABLE IF EXISTS manufacturer;

CREATE TABLE manufacturers(
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(360),
    last_name VARCHAR(360)
);

CREATE TABLE stock (
   id SERIAL PRIMARY KEY,
   description VARCHAR (360),
   cost INT,
   price INT,
   manufacturer_id INT REFERENCES manufacturer(id) ON DELETE CASCADE
);



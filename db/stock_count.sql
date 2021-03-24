DROP TABLE IF EXISTS stock;
DROP TABLE IF EXISTS manufacturers;

CREATE TABLE manufacturers(
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(360),
    last_name VARCHAR(360)
);

CREATE TABLE stock (
   id SERIAL PRIMARY KEY,
   name VARCHAR(255),
   description VARCHAR (360),
   cost INT,
   price INT,
   in_stock BOOLEAN, 
   manufacturer_id INT REFERENCES manufacturers(id) ON DELETE CASCADE
);




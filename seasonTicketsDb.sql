CREATE TABLE IF NOT EXISTS Season_tickets (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    price FLOAT NOT NULL,
    quantity INTEGER NOT NULL
);

--eisagwgh sth lista gia na thn exoume ws pepathmenh
INSERT INTO Season_tickets (name, price, quantity)
VALUES
    ('basic_card', 300.00, 5000),
    ('medium_card', 450.00, 2000),
    ('vip_card', 1000.00, 500);
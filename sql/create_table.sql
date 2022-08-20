/*
This is the query used to create bitcoin_history table. This table is the one
where data that is get from the API is sent.
*/

CREATE TABLE bitcoin_history 
(
    date_summary DATE PRIMARY KEY NOT NULL,
    opening DECIMAL(14, 8),
    closing DECIMAL(14, 8),
    lowest DECIMAL(14, 8),
    highest DECIMAL(14, 8),
    volume DECIMAL(17, 8),
    quantity DECIMAL(16, 8),
    amount INT(5),
    avg_price DECIMAL(16, 8)
);

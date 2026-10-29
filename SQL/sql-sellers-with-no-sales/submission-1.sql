-- Write your query below
SELECT 
    s.seller_name
FROM
    (SELECT order_id, 
        seller_id 
        FROM orders 
        WHERE sale_date >= to_date('2020-01-01', 'yyy-mm-dd') 
        AND
        sale_date < to_date('2021-01-01', 'yyy-mm-dd') ) o
RIGHT JOIN
seller s
ON o.seller_id = s.seller_id
WHERE
    o.order_id IS NULL
    ORDER BY s.seller_name;

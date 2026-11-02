-- Write your query below
SELECT s.name FROM
sales_person s 
LEFT JOIN
    (SELECT c.name, o.sales_id FROM
        company c LEFT JOIN orders o
        ON c.com_id = o.com_id where c.name = 'CRIMSON') cn
    ON s.sales_id = cn.sales_id
WHERE cn.sales_id IS NULL;
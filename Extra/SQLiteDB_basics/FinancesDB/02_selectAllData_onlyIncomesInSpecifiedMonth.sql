SELECT 
    ft.id,
    ft.amount,
    ft.date,
    ft.note,
    pm.name AS payment_method,
    tt.name AS transaction_type,
    c.name AS category
FROM 
    financial_transaction ft
	JOIN payment_method pm ON ft.payment_method_fk = pm.id
	JOIN transaction_type tt ON ft.transaction_type_fk = tt.id
	JOIN category c ON ft.category_fk = c.id
WHERE 
    1=1
	AND strftime('%Y-%m', ft.date) = '2020-02'
    AND c.id = 1;
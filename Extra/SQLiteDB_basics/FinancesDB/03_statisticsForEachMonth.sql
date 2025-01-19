SELECT 
    strftime('%Y-%m', date) AS month,
    SUM(CASE WHEN tt.id = 1 THEN ft.amount ELSE 0 END) AS total_income,
    SUM(CASE WHEN tt.id = 2 THEN ft.amount ELSE 0 END) AS total_spending,
    SUM(CASE WHEN tt.id = 1 THEN ft.amount ELSE 0 END) - 
    SUM(CASE WHEN tt.id = 2 THEN ft.amount ELSE 0 END) AS balance
FROM 
    financial_transaction ft
	JOIN transaction_type tt ON ft.transaction_type_fk = tt.id
GROUP BY 
    strftime('%Y-%m', date);
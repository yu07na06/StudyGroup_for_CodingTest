-- 코드를 입력하세요
--SELECT DISTINCT cart_id
--FROM cart_products
--WHERE name = 'Yogurt' and cart_id IN(
--    SELECT DISTINCT cart_id
--    FROM cart_products
--    WHERE name = 'Milk'
--)
--ORDER BY cart_id;


SELECT DISTINCT Y.cart_id
FROM (SELECT cart_id FROM cart_products WHERE name = 'Yogurt') Y
JOIN (SELECT cart_id FROM cart_products WHERE name = 'Milk') M
ON Y.cart_id = M.cart_id
ORDER BY cart_id;
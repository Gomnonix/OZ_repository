-- customers 테이블에서 특정 고객을 삭제하세요.
DELETE FROM customers WHERE customer_id = 'OZ';

-- products 테이블에서 특정 제품을 삭제하세요.
DELETE FROM products WHERE product_id = 'car';

-- employees 테이블에서 특정 직원을 삭제하세요.
DELETE FROM employees WHERE user_name = 'OZ';

-- offices 테이블에서 특정 사무실을 삭제하세요.
DELETE FROM offices WHERE office_id = '2030'

-- orders 테이블에서 특정 주문을 삭제하세요.
DELETE FROM orders WHERE order_id = '1'

-- orderdetails 테이블에서 특정 주문 상세를 삭제하세요.
DELETE FROM orderdetails WHERE order_id = '1'

-- payments 테이블에서 특정 지불 내역을 삭제하세요.
DELETE FROM payments WHERE pay_id = "pizza_school"

-- productlines 테이블에서 특정 제품 라인을 삭제하세요.
DELETE FROM productlines WHERE product_id = "sports car"

-- customers 테이블에서 특정 지역의 모든 고객을 삭제하세요.
DELETE FROM customers WHERE customer_area = "seoul"

-- products 테이블에서 특정 카테고리의 모든 제품을 삭제하세요.
DELETE FROM products WHERE category = "food"
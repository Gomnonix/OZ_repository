-- customers 테이블에서 모든 고객 정보를 조회하세요
SELECT * FROM customers;

-- products 테이블에서 모든 제품 목록을 조회하세요.
SELECT name, price FROM products;

-- employees 테이블에서 모든 직원의 이름과 직급을 조회하세요.
SELECT name, position FROM employees

-- offices 테이블에서 모든 사무실의 위치를 조회하세요.
SELECT location FROM offices;

-- orders 테이블에서 최근 10개의 주문을 조회하세요.
SELECT * FROM orders ORDER BY orderList DESC LIMIT 10;

-- orderdetails 테이블에서 특정 주문의 모든 상세 정보를 조회하세요.
SELECT * FROM orderdetails WHERE order_Id = first; 

-- payments 테이블에서 특정 고객의 모든 지불 정보를 조회하세요.
SELECT * FROM payments WHERE customer_Id = 'OZ';

-- productlines 테이블에서 각 제품 라인의 설명을 조회하세요.
SELECT productline, descrip  FROM productlines

-- customers 테이블에서 특정 지역 고객을 조회하세요.
SELECT * FROM customers WHERE Area = 'seoul'

-- products 테이블에서 특정 가격 범위의 제품을 조회하세요.
SELECT * FROM products WHERE price BETWEEN 1000 AND 20000
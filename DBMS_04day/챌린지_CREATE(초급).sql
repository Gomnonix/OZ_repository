-- customers 테비을에 새 고객을 추가하세요
INSERT INTO customers (user_name, age) VALUES('OZ', '28');

-- products 테이블에 새 제품을 추가하세요
INSERT INTO products (product_name, price) VALUES('car', '28000');

-- employees 테이블에 새 직원을 추가하세요
INSERT INTO employees (employee_name, age) VALUES('OZ', '22');

-- offices 테비을에 새 사무실을 추가하세요
INSERT INTO offices (office, location) VALUES('coding', 'seoul');

-- orders 테이블에 새 주문을 추가하세요
INSERT INTO orders (food, beverage) VALUES('buger', 'coke');
-- orderdetails 테이블에 주문 상세 정보를 추가하세요
INSERT INTO orderdetails (order_name, age, address) 
VALUES('OZ', '28', 'seoul');
-- payments 테이블에 지불 정보를 추가하세여
INSERT INTO payments (pay, shop, name) 
VALUES ('20000', 'hair_shop', 'OZ'); 
-- productlines 테이블에 제품 라인을 추가하세요
INSERT INTO productlines (productline,product) 
VALUES('KIA', 'K5');
-- customers 테이블에 다른 지역의 고객을 추가하세요
INSERT INTO customers (customer_name, customer_age, customer_address) 
VALUES('OZ', '28', 'seoul');
-- products 테이블에 다른 카테고리의 제품을 추가하세요
INSERT INTO products (name, price, store) VALUES('Toy_story', '28000', 'Disney');
-- customers 테이블에서 특정 고객의 주소를 갱신하세요.
UPDATE customers SET address = 'seoul' WHERE customer_Id = 'OZ';
-- products 테이블에서 특정 제품의 가격을 갱신하세요.
UPDATE products SET price = 1800 WHERE product_ID = 'car';
     
-- employees 테이블에서 특정 직원의 직급을 갱신하세요.
 UPDATE employees SET position = 'manager' WHERE user_name = 'OZ';
    
-- offices 테이블에서 특정 사무실의 전화번호를 갱신하세요.
 UPDATE offices SET phone_num = '031-731-2123' WHERE office_num = '2030';
    
-- orders 테이블에서 특정 주문의 상태를 갱신하세요.
 UPDATE orders SET status = 'fresh' WHERE order_Id = 1;
    
-- orderdetails 테이블에서 특정 주문 상세의 수량을 갱신하세요.
 UPDATE orderdetails SET quantity = 7 WHERE orderdetail_Id = 'car';
 
-- payments 테이블에서 특정 지불의 금액을 갱신하세요.
 UPDATE payments SET pay = 20000 WHERE customer_id = "OZ";
    
-- productlines 테이블에서 특정 제품 라인의 설명을 갱신하세요.
 UPDATE productlines SET decrip = "sports car" WHERE product_id = 'car'
    
-- customers 테이블에서 특정 고객의 이메일을 갱신하세요.
 UPDATE customers SET email = "OZ@example.com" WHERE customer_id = 'OZ'
    
-- products 테이블에서 여러 제품의 가격을 한 번에 갱신하세요.
 UPDATE products SET price = price * 1.7;
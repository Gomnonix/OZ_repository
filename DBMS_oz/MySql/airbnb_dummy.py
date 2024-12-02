import pymysql
from faker import Faker
import random

#Faker 객체 초기화
fake = Faker()

 
conn = pymysql.connect(
     host='localhost',
     user='root',       
     password='!rldnd12',  
     db='airbnb',       
     charset='utf8mb4',
     cursorclass=pymysql.cursors.DictCursor
 )

# Products 테이블을 위한 더미 데이터 생성
def generate_product_data(n):
    for _ in range(n):
        product_name = fake.name()
        price = random.randint(1000, 20000)
        stock_quantity = random.randint(10, 100)
        create_date = fake.date()
        yield (product_name, price, stock_quantity, create_date)

# Customers 테이블을 위한 더미 데이터 생성
def generate_customer_data(n):
    for _ in range(n):
        customer_name = fake.name()
        email = fake.email()
        address = fake.address()
        create_date = fake.date()
        yield (customer_name, email, address, create_date)

# Orders 테이블을 위한 더미 데이터 생성
def generate_order_data(n, customer_ids):
    for _ in range(n):
        customer_id = random.choice(customer_ids)
        order_date = fake.date()
        total_amount = round(random.uniform(20, 500), 2)
        yield (customer_id, order_date, total_amount)

# 데이터베이스에 데이터 삽입
with conn.cursor() as cursor:
    
    products_sql = "INSERT INTO Products (productName, price, stockQuantity, createDate) VALUES (%s, %s, %s, %s)"
    for data in generate_product_data(10):
        cursor.execute(products_sql, data)
    conn.commit()


    customers_sql = "INSERT INTO Customers (customerName, email, address, createDate) VALUES (%s, %s, %s, %s)"
    for data in generate_customer_data(5):
        cursor.execute(customers_sql, data)
    conn.commit()

    
    cursor.execute("SELECT customerID FROM Customers")
    customer_ids = [row['customerID'] for row in cursor.fetchall()]
    
    orders_sql = "INSERT INTO Orders (customerID, orderDate, totalAmount) VALUES (%s, %s, %s)"
    for data in generate_order_data(10, customer_ids):
        cursor.execute(orders_sql, data)
    conn.commit()

# 데이터베이스 연결 종료
def delete_customer():
    cursor = conn.cursor()
    sql = "DELETE * FROM Products"
    cursor.execute(sql)
    conn.commit()
    cursor.close()

conn.close()

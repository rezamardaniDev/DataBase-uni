from database import db

def add_product():
    product_id = int(input("enter id for product: "))
    product_name = input("enter name for product: ")
    category_id = int(input("enter category id for product: "))
    product_price = int(input("enter price for product: "))
    product_quantity = int(input("enter quantity for product: "))
    
    db.cursor.execute("""
                        INSERT INTO products(product_id,product_name,category_id,price,quantity)
                        VALUES(%s, %s, %s, %s, %s)""",
                        (
                            product_id,
                            product_name,
                            category_id,
                            product_price,
                            product_quantity
                        ))
    db.mydb.commit()
    print("new product added successfully!")
    
    
def add_category():
    category_id = int(input("enter id for category: "))
    category_name = input("enter name for category: ")
    
    db.cursor.execute("""
                        INSERT INTO categories(category_id, category_name)
                        VALUES(%s, %s)""",
                        (
                           category_id,
                           category_name
                        ))
    db.mydb.commit()
    print("new category added successfully!")
    
    
def remove_product():
    product_id = int(input("enter id for remove product: "))
    
    db.cursor.execute("""
                      DELETE FROM products WHERE product_id = (%s)
                      """,
                      (product_id,)
                      )
    db.mydb.commit()
    print("product deleted seccessfully")
    

def remove_category():
    product_id = int(input("enter id for remove category: "))
    
    db.cursor.execute("""
                      DELETE FROM categories WHERE category_id = (%s)
                      """,
                      (product_id,)
                      )
    db.mydb.commit()
    print("category deleted seccessfully")
    
    
def update_product():
    search_id = int(input("enter product id for edit: "))
    
    product_id = int(input("enter new id for product: "))
    product_name = input("enter new name for product: ")
    category_id = int(input("enter new category id for product: "))
    product_price = int(input("enter new price for product: "))
    product_quantity = int(input("enter new quantity for product: "))
    
    db.cursor.execute("""
                      UPDATE products SET
                      product_id = %s,
                      product_name = %s,
                      category_id = %s,
                      price = %s,
                      quantity = %s
                      WHERE product_id = %s
                      """,
                      (
                        product_id,
                        product_name,
                        category_id,
                        product_price,
                        product_quantity,
                        search_id
                      ))
    db.mydb.commit()
    print("product updated successfully")


def update_category():
    search_id = int(input("enter category id for edit: "))
    
    category_id = int(input("enter new id for category: "))
    category_name = input("enter new name for category: ")
    
    db.cursor.execute("""
                    UPDATE categories SET
                    category_id = %s,
                    category_name = %s
                    WHERE product_id = %s """,
                    (
                        category_id,
                        category_name,
                        search_id 
                    ))
    db.mydb.commit()
    print("category updated successfully")
    
    
    
def search_product():
    search_query = input("enter name or category name for search product: ")
    
    db.cursor.execute("""
                      SELECT * 
                      FROM products 
                      JOIN categories ON products.category_id = categories.category_id
                      WHERE product_name = %s OR category_name = %s
                      """,
                      (
                          search_query,
                          search_query
                      ))
    result = db.cursor.fetchall()
    for item in result:
        print(f"id:{item[0]} - name:{item[1]} - category:{item[2]} - price:{item[3]} - quantity:{item[4]}")
    
def search_category():
    search_query = input("enter name or category name for search product: ")
    
    db.cursor.execute("""
                      SELECT * 
                      FROM categories 
                      WHERE category_name = %s
                      """,
                      (
                          search_query,
                      ))
    result = db.cursor.fetchall()
    for item in result:
        print(f"id:{item[0]} - name:{item[1]}")
        

def display_product():
    db.cursor.execute("""
                    SELECT * 
                    FROM products
                    """) 
    result = db.cursor.fetchall()
    for item in result:
        print(f"id:{item[0]} - name:{item[1]} - category:{item[2]} - price:{item[3]} - quantity:{item[4]}")
    

def display_category():
    db.cursor.execute("""
                    SELECT * 
                    FROM categories
                    """) 
    result = db.cursor.fetchall()
    for item in result:
        print(f"id:{item[0]} - name:{item[1]}")
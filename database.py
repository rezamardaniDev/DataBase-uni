import mysql.connector

class Connection:
        def __init__(self) -> None:
            self.mydb = mysql.connector.connect(
                host = "localhost",
                user = 'reza',
                password = 'mardani80',
                database = "shop"
            )
            
            self.cursor = self.mydb.cursor()
            self.create_categories_table()
            self.create_products_table()
            
            
        def show_databasee(self):
                sql = "SHOW DATABASES"
                self.cursor.execute(sql)
                print(self.cursor.fetchall())
                
                
        def show_tables(self):
                sql = "SHOW TABLES"
                self.cursor.execute(sql)
                print(self.cursor.fetchall())
                
        
        def create_categories_table(self):
                sql = """
                        CREATE TABLE IF NOT EXISTS categories (
                        category_id int auto_increment,
                        category_name VARCHAR(255),
                        PRIMARY KEY (category_id)
                );""" 
                self.cursor.execute(sql)
                
                
        def create_products_table(self):
                sql = """
                        CREATE TABLE IF NOT EXISTS products(
                        product_id int auto_increment,
                        product_name VARCHAR(255),
                        category_id int,
                        price int,
                        quantity int,
                        PRIMARY KEY (product_id),
                        FOREIGN KEY (category_id) REFERENCES categories (category_id)
                        
                );"""
                self.cursor.execute(sql)
                            
                
db = Connection()
from sql_connection import get_sql_connection

def get_all_products(connection):
        cur = connection.cursor()
        query = ("SELECT products.product_id, products.name, products.uom_id, products.price_per_unit, uom.uom_name "
                 "FROM grocery_store.products INNER JOIN grocery_store.uom ON products.uom_id = uom.uom_id")

        cur.execute(query)
        response = []
        # Fetch and print the results
        for (product_id, name, uom_id, price_per_unit, uom_name) in cur:
            response.append(
                {
                    'product_id': product_id,
                    'name':name,
                    'uom_id':uom_id,
                    'price_per_unit':price_per_unit,
                    'uom_name':uom_name
                }
            )

        return response
def insert_new_product(connection, product):
        cur = connection.cursor()
        query = ("INSERT INTO products "
                 "(name, uom_id, price_per_unit)"
                 "VALUES (%s, %s, %s)")
        data = (product['product_name'], product['uom_id'], product['price_per_unit'])
        cur.execute(query, data)
        connection.commit()
        return cur.lastrowid

def delete_product(connection, product_id):
    cursor = connection.cursor()
    query = ("DELETE FROM products where product_id=" + str(product_id))
    cursor.execute(query)
    connection.commit()

    return cursor.lastrowid

if __name__=='__main__':
    connection = get_sql_connection()
   # print(insert_new_product(connection,{
     #   'product_name' : 'cabbage',
      #  'uom_id': '1',
    #    'price_per_unit': '150'
  #  }))
    print(delete_product(connection, 8))

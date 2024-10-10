def get_uoms(connection):
    cur = connection.cursor()
    query = ("select * from uom")
    cur.execute(query)
    response = []
    for (uom_id, uom_name) in cur:
        response.append({
            'uom_id': uom_id,
            'uom_name': uom_name
        })
    return response


if __name__ == '__main__':
    from sql_connection import get_sql_connection

    connection = get_sql_connection()
    # print(get_all_products(connection))
    print(get_uoms(connection))
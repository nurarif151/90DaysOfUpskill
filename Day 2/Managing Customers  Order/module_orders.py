def create_order(order_id, customer_name, items):
    # code to create an order
    return {
        'order_id': order_id,
        'customer_name': customer_name,
        'items': items
    }

def retrieve_order(order_id):
    # code to retrieve an order
    return {
        'order_id': order_id,
        'customer_name': 'John Doe',
        'items': ['item1', 'item2']
    }

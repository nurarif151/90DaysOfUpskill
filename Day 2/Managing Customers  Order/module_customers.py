def create_customer(customer_id, customer_name, address):
    # code to create a customer
    return {
        'customer_id': customer_id,
        'customer_name': customer_name,
        'address': address
    }

def retrieve_customer(customer_id):
    # code to retrieve a customer
    return {
        'customer_id': customer_id,
        'customer_name': 'Jane Doe',
        'address': '123 Main St'
    }

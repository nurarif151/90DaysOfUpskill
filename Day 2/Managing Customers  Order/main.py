# import modules
import module_orders
import module_customers

# create an order
new_order = module_orders.create_order(1, 'John Doe', ['item1', 'item2'])
print('New Order:', new_order)

# retrieve an order
retrieved_order = module_orders.retrieve_order(1)
print('Retrieved Order:', retrieved_order)

# create a customer
new_customer = module_customers.create_customer(1, 'Jane Doe', '123 Main St')
print('New Customer:', new_customer)

# retrieve a customer
retrieved_customer = module_customers.retrieve_customer(1)
print('Retrieved Customer:', retrieved_customer)

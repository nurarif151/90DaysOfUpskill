def predict_sales(actual_sales, target_sales):
  sales_difference = actual_sales - target_sales
  if sales_difference > 0:
    print("Sales are higher than target by", sales_difference)
  elif sales_difference == 0:
    print("Sales are equal to target")
  else:
    print("Sales are less than target by", abs(sales_difference))

# Example usage
sales_data = [100, 150, 200, 175, 180, 145]
target_sales = 150
i = 0
while i < len(sales_data):
  actual_sales = sales_data[i]
  predict_sales(actual_sales, target_sales)
  i += 1

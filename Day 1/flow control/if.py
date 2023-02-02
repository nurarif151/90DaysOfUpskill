def predict_sales(actual_sales, target_sales):
  if actual_sales > target_sales:
    print("Sales are higher than target")
  elif actual_sales == target_sales:
    print("Sales are equal to target")
  else:
    print("Sales are less than target")

# Example usage
actual_sales = 200
target_sales = 150
predict_sales(actual_sales, target_sales) # Output: Sales are higher than target

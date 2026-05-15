item = input("Enter item name: ")

price = float(input("Enter item price: "))
quantity = int(input("Enter quantity: "))

total = price * quantity
gst = total * 0.18
final_bill = total + gst

print("\n===== BILL =====")

print("Item Name :", item)
print("Price     :", price)
print("Quantity  :", quantity)
print("GST       :", gst)
print("Final Bill:", final_bill)

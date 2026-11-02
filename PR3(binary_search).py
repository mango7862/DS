
customer_ids = [10, 20, 30, 40, 50, 60, 70]

search_id = int(input("Enter customer account ID to search: "))

low = 0
high = len(customer_ids) - 1
found = False

while low <= high:
    mid = (low + high) // 2

    if customer_ids[mid] == search_id:
        found = True
        break
    elif customer_ids[mid] < search_id:
        low = mid + 1
    else:
        high = mid - 1

if found:
    print("Customer account ID found")
else:
    print("Customer account ID not found")

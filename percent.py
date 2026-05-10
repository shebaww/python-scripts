import math

start_page = int(input("What is your start Page?: "))
current_page = int(input("What is your current Page?: "))
end_page = int(input("What is your end goal Page?: "))

total_page = end_page - start_page
read_amount = current_page - start_page

percent = (read_amount /total_page) * 100

print(f"You have read {percent}%!")

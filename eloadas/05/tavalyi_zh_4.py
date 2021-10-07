call_minutes = []
message_count = []
month_count = 12

for month in range(1,month_count+1):
    print("Month",month,":")
    call_minutes.append(int(input(" How many minutes of calls did you have? ")))
    message_count.append(int(input(" How many SMSs did you send? ")))

print("Tariff fees:")
minute_price = int(input(" How much does a minute of call cost you? "))
message_price = int(input( " How much does an SMS cost you? "))
monthly_base_fee = int(input(" How much is your monthly base fee? "))

total_cost=0
for month in range(month_count):
    month_total_cost = call_minutes[month] * minute_price + message_count[month] * message_price
    if month_total_cost < monthly_base_fee:
        month_total_cost = monthly_base_fee
    total_cost+=month_total_cost

print("Your total bill for calling is: ", total_cost)

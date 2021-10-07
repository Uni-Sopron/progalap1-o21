call_minutes = []
message_count = []
month_count = 2

minute_price = 0
message_price = 0
monthly_base_fee = 0

total_cost = 0


def input_mothly_usage(month):
    print("Month",month,":")
    call_minutes.append(int(input(" How many minutes of calls did you have? ")))
    message_count.append(int(input(" How many SMSs did you send? ")))

def input_tariff_fees():
    global minute_price
    global message_price
    global monthly_base_fee
    print("Tariff fees:")
    minute_price = int(input(" How much does a minute of call cost you? "))
    message_price = int(input( " How much does an SMS cost you? "))
    monthly_base_fee = int(input(" How much is your monthly base fee? "))

def total_cost_calculation():
    global total_cost
    for month in range(month_count):
        month_total_cost = call_minutes[month] * minute_price + message_count[month] * message_price
        if month_total_cost < monthly_base_fee:
            month_total_cost = monthly_base_fee
        total_cost += month_total_cost

for month in range(1,month_count+1):
    input_mothly_usage(month)
input_tariff_fees()
total_cost_calculation()


print("Your total bill for calling is: ", total_cost)

def input_mothly_usage(month):
    print("Month",month,":")
    call_minutes = int(input(" How many minutes of calls did you have? "))
    message_count = int(input(" How many SMSs did you send? "))
    return call_minutes, message_count

def input_annual_usage(month_count):
    call_minutes = []
    message_count = []
    for month in range(1,month_count+1):
        month_call_minutes, month_message_count = input_mothly_usage(month)
        call_minutes.append(month_call_minutes)
        message_count.append(month_message_count)
    return call_minutes, message_count

def input_tariff_fees():
    print("Tariff fees:")
    minute_price = int(input(" How much does a minute of call cost you? "))
    message_price = int(input( " How much does an SMS cost you? "))
    monthly_base_fee = int(input(" How much is your monthly base fee? "))
    return minute_price,message_price,monthly_base_fee

def month_cost_calculation(call_minutes,message_count,minute_price,message_price, monthly_base_fee):
    month_total_cost = call_minutes * minute_price + message_count * message_price
    if month_total_cost < monthly_base_fee:
        month_total_cost = monthly_base_fee

def total_cost_calculation(month_count, call_minutes, message_count,minute_price,message_price, monthly_base_fee):
    total_cost=0
    for month in range(month_count):
        total_cost += month_cost_calculation(call_minutes[month],message_count[month],minute_price,message_price, monthly_base_fee)
    return total_cost


month_count = 2
call_minutes, message_count = input_annual_usage(month_count)
minute_price,  message_price, monthly_base_fee = input_tariff_fees()
total_cost = total_cost_calculation(month_count, call_minutes, message_count,minute_price,message_price, monthly_base_fee)


print("Your total bill for calling is: ", total_cost)

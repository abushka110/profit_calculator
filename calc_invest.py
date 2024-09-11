def calculate_etf_profit(initial_investment, monthly_investment, annual_rate, months_until_start, total_months):
    # Перетворимо річну ставку на місячну
    monthly_rate = annual_rate / 12 / 100
    
    # Майбутня вартість початкового внеску
    future_value_initial = initial_investment * (1 + monthly_rate) ** total_months
    
    # Майбутня вартість щомісячних внесків після затримки
    future_value_contributions = 0
    for month in range(months_until_start, total_months):
        future_value_contributions += monthly_investment * (1 + monthly_rate) ** (total_months - month)
    
    # Загальна майбутня вартість
    future_value = future_value_initial + future_value_contributions
    return future_value
    
def total_investment(initial_investment, monthly_investment, months_until_start, total_months):
    future_value_contributions = initial_investment + (monthly_investment * (total_months - months_until_start))
    return future_value_contributions

# Параметри
initial_investment = 1000  # початковий внесок
monthly_investment = 100   # щомісячний внесок
annual_rate = 7            # очікувана річна дохідність у відсотках
months_until_start = 1     # затримка щомісячних внесків (2 місяці)
total_months = 24    # інвестиції на 10 років (120 місяців)

future_value = calculate_etf_profit(initial_investment, monthly_investment, annual_rate, months_until_start, total_months)
total_investments = total_investment(initial_investment, monthly_investment, months_until_start, total_months)
print(f"Ваш вклад: {total_investments}")
print(f"Приблизна майбутня вартість: {future_value} євро")
print(f"Прибуток: {future_value - total_investments}")
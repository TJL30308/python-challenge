import os 
import csv

with open ('budget_data.csv') as file:
    budget_data = csv.reader(file) # reads CSV file
    next(budget_data, None) # removes header from count

    # create lists and variables to store CSV data
    months = []
    profit = []
    change_profits = []
    previous_profit = 0

    for row in budget_data:
        
        months.append(row[0]) # adds months to list
        profit.append(int(row[1])) # adds profits to list
        current_profit = int(row[1]) # set current profit
        change_profit = int(current_profit - previous_profit) # calculate change in profit
        change_profits.append(change_profit) # add change to list
        previous_profit = int(row[1]) # set previous profit

    months_count = int(len(months)) # counts items in months list
    total_profit = sum(profit) # sums all items in profits list
    average_profit_change = round((int(profit[-1]) - int(profit[0])) / (months_count - 1) , 2) # calculates average profit change
    max_profit_change = max(change_profits) # find max profit change
    min_profit_change = min(change_profits) # find min profit change
    max_month = months[change_profits.index(max(change_profits))] # find max profit change month
    min_month = months[change_profits.index(min(change_profits))] # find min profit change month

print("Financial Analysis")
print("------------------------")
print("Total Months : " + str(months_count))
print('Total: $' + str(total_profit))
print('Average Change: $' + str(average_profit_change))
print('Greatest Increase in Profits: ' + str(max_month) + " ($" + str(max_profit_change) + ")")
print('Greatest Decrease in Profits: ' + str(min_month) + " ($" + str(min_profit_change) + ")")

pybank_results = 'pybank_results.txt'

with open(pybank_results, 'w') as file_object:
    file_object.write("Financial Analysis\n")
    file_object.write("------------------------\n")
    file_object.write('Total Months: '+ str(months_count) + "\n")
    file_object.write('Total: $' + str(total_profit) + "\n")
    file_object.write('Average Change: $' + str(average_profit_change) + "\n")
    file_object.write('Greatest Increase in Profits: ' + str(max_month) + " ($" + str(max_profit_change) + ")" + "\n")
    file_object.write('Greatest Decrease in Profits: ' + str(min_month) + " ($" + str(min_profit_change) + ")" + "\n")
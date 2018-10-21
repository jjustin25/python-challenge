import # import dependencies
import csv 

import os 

# load files 
load_budget = "budget_data_1.csv"
load_budget2="budget_data_2.csv"

#revenue parameters
total_revenue=0
#month parameters
total_months=0

with open(load_budget,newline ="") as budget_data:

   csvreader= csv.DictReader(budget_data)
   for row in csvreader:
       total_months=total_months+1

       total_revenue = total_revenue + int(row["Revenue"])


with open(load_budget2,newline ="") as budget_data_2:

   csvreader= csv.DictReader(budget_data_2)
   for row in csvreader:
       total_months=total_months+1

       total_revenue = total_revenue + int(row["Revenue"])
# Create a dictionary for the budget
budget_dict = {}

with open(load_budget,newline ="") as budget_data:
   csvreader = csv.DictReader(budget_data)
   for row in csvreader:
       budget_dict[row['Date']] = row['Revenue']

       total_months = total_months + 1
       total_revenue = total_revenue + int(row["Revenue"])
       

avg_revenue = total_revenue/total_months
maximum = max(budget_dict, key=budget_dict.get)
minimum = min(budget_dict, key=budget_dict.get)

with open(load_budget,newline ="") as budget_data:
   csvreader= csv.DictReader(budget_data)
   for row in csvreader:
       total_months=total_months+1
       total_revenue = total_revenue + int(row["Revenue"])

avg_revenue = total_revenue/total_months



       
print ("Financial Analysis")
print("___________________")
print ("total months:"+str(total_months))
print ("total revenue: $"+ str(total_revenue))   
print ("Avg monthly revenue: $"+ str(avg_revenue)) 
print ("The greatest increase in revenue: " + maximum +" ($ "+(str(budget_dict[maximum])+")")) 
print ("The greatest decrease in revenue: " + minimum +" ($ "+(str(budget_dict[minimum])+")"))
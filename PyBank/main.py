# Import Dependencies
import csv

file_path = 'Resources/budget_data.csv'

pl_hold = 0
diff_array = []
pl_o = 0
date_array = []
PL_array = []

with open(file_path,'r') as file:

    data = csv.reader(file)
    next(data)
    data = list(data)
    for date, PL in data:
        PL_array.append(int(PL))
        date_array.append(date)
        pl_hold += int(PL)
        if pl_o == 0:
            pl_o = int(PL)
        diff_array.append(int(PL) - pl_o)
        pl_o = int(PL)
    #print(diff_array)
    ave_change = sum(diff_array)/len(diff_array)
    peak_d = max(diff_array)
    trough_d = min(diff_array)
    
    peak_date = date_array[diff_array.index(peak_d)]
    trough_date = date_array[diff_array.index(trough_d)]
    peak_date_change = PL_array[diff_array.index(peak_d)]
    trough_date_change = PL_array[diff_array.index(trough_d)]
    t_months = len(date_array)
    total = sum(PL_array)
    analysis = f"""
            Financial Analysis
            ----------------------------
            Total Months: {t_months}
            Total: {total}
            Average Change: {ave_change}
            Greatest Increase in Profits: {peak_date} (${peak_date_change})
            Greatest Decrease in Profits: {trough_date} (${trough_date_change})
    """
    with open('analysis.txt', 'w') as file:
        file.write(analysis)
        print(analysis)




    

    


import csv

file_path = 'Resources/election_data.csv'
candidates = {}
can_output = []
with open(file_path) as file:

    original_data = csv.reader(file)
    next(original_data)
    # tot_num = len(original_data)
    i = 0
    for ID, county, candidate in original_data:
        i += 1
        # print(ID, candidate)
        if candidate not in candidates:
            candidates[candidate] = 1
        else:
            candidates[candidate] +=1
    cast_votes = i
    
    #print(candidates)
    total_votes = (sum(candidates.values()))

    for key,values in candidates.items():
        perc = format((values/total_votes)*100,'.3f')
        can_output.append((key + ": " + f"{perc}% " + f"({values})"))
        if values == max(candidates.values()):
            winner = key

    analysis = (f"""
    Election Results
    -------------------------
    Total Votes: {total_votes}
    -------------------------
    {can_output[0]}
    {can_output[1]}
    {can_output[2]}
    {can_output[3]}
    -------------------------
    Winner : {winner}
    -------------------------
    """)

    with open('analysis.txt', 'w') as file:
        file.write(analysis)
        print(analysis)



    




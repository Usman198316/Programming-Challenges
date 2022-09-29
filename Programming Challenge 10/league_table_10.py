import csv 
from pathlib import Path 

csv_file = Path("Premier 16-17.csv")

def check_file_exists(csv_file): 
    return csv_file.is_file()
        
def read_csv(csv_file):
    csv_contents = []
    if check_file_exists(csv_file):
        with open(csv_file) as csvfile:
            reader = csv.reader(csvfile, delimiter=",")
            next(reader)                  ###   skip first row (header)
            for row in reader:
                csv_contents.append(row)
    return csv_contents

def process_results(rows):
    dictionary = {}
    referee = {}
    for row in rows:
        
        home = row[1]
        away = row[2]
        homeGoals = row[3]
        awayGoals = row[4]
        winner = row[5]
        ref = row[6]
        homeShots = row[7]
        homeShotsT = row[9]
        awayShots = row[8]
        awayShotsT = row[10]
        homeFouls = row[11]
        awayFouls = row[12]
        homeYellow = row[15]
        awayYellow = row[16]
        homeRed = row[17]
        awayRed = row[18]
        
        if home not in dictionary:
            dictionary[home]= [0,0,0,0,0,0,0]   ##win, draw, lost, gd, points, accuracy, fouls
        if away not in dictionary:
            dictionary[away]= [0,0,0,0,0,0,0]
        if ref not in referee:
            referee[ref] = [0,0]

        #Check for Draw
            
        if winner == "D":
            dictionary[home][4]+= 1 #points
            dictionary[away][4]+= 1
            dictionary[home][1]+= 1 #points
            dictionary[away][1]+= 1
            dictionary[home][3] += int(homeGoals) - int(awayGoals)
            dictionary[away][3] += int(awayGoals) - int(homeGoals)
            dictionary[home][6] += int(homeFouls)
            dictionary[away][6] += int(awayFouls)
            
        elif winner == "A":
            dictionary[away][4]+= 3
            dictionary[away][0]+= 1
            dictionary[home][2] += 1
            dictionary[home][3] += int(homeGoals) - int(awayGoals)
            dictionary[away][3] += int(awayGoals) - int(homeGoals)
            dictionary[home][6] += int(homeFouls)
            dictionary[away][6] += int(awayFouls)
                     

        elif winner == "H":
            dictionary[home][4] += 3
            dictionary[home][0] += 1
            dictionary[away][2] += 1
            dictionary[home][3] += int(homeGoals) - int(awayGoals)
            dictionary[away][3] += int(awayGoals) - int(homeGoals)
            dictionary[home][6] += int(homeFouls)
            dictionary[away][6] += int(awayFouls)

        dictionary[home][5] += ((int(homeShotsT) / int(homeShots)) / 38)
        dictionary[away][5] += ((int(awayShotsT) / int(awayShots)) / 38)
        referee[ref][0] += int(row[15]) + int(row[16]) + int(row[17])*2 + int(row[18])*2
        referee[ref][1] += 1
    maxRefavg = 0
    leastRefavg = 10
    for ref in referee:
        refAvg = referee[ref][0] / referee[ref][1]
        if maxRefavg < refAvg:
            maxRefavg = refAvg
            maxRef = ref
        if leastRefavg > refAvg:
            leastRefavg = refAvg
            leastRef = ref
    print(f"The referee with the highest card average per game was {maxRef}")
    print(f"The referee with the lowest card average per game was {leastRef}")
    
    return(dictionary)
    
        
    

if __name__ == "__main__":
    file_contents = read_csv(csv_file)
    results = process_results(file_contents)
    accMax = 0
    accLeast = 1
    mostFouls = 0
    leastFouls = 1000
    for k, v in sorted(results.items(), key = lambda item: item[1][4], reverse = True):        
         table = (k, v)
         print(table)
         if table[1][5] > accMax:
             accMax = table[1][5]
             accMaxT = table[0]
         if table[1][5] < accLeast:
             accLeast = table[1][5]
             accLeastT = table[0]
         if table[1][6] > mostFouls:
             mostFouls = table[1][6]
             mostFoulsT = table[0]
         if table[1][6] < leastFouls:
             leastFouls = table[1][6]
             leastFoulsT = table[0]
            
         

    print(f"The most accurate team was {accMaxT}")
    print(f"The least accurate team was {accLeastT}")
    print(f"The dirtiest team was {mostFoulsT}")
    print(f"The cleanest team was {leastFoulsT}")   
    
         

    
 

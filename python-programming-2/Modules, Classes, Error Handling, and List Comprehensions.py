## 2. Introduction to the Data ##

import csv
f = open("nfl_suspensions_data.csv" , "r")
nfl_suspensions = list(csv.reader(f))
nfl_suspensions = nfl_suspensions[1:]
years = {}
for row in nfl_suspensions:
    yer = row[5]
    if yer in years:
        years[yer] += 1
    else:
        years[yer] = 1
print(years)        

## 3. Unique Values ##

unique_teams = set([row[1] for row in nfl_suspensions])
unique_games = set([row[2] for row in nfl_suspensions])
    

## 4. Suspension Class ##

class Suspension():
    def __init__(self,sus):
            self.name = sus[0]
            self.team = sus[1]
            self.games = sus[2]
            self.year = sus[5]
            
third_suspension = Suspension(nfl_suspensions[2])
    

## 5. Tweaking the Suspension Class ##

class Suspension():
    def __init__(self,row):
        self.name = row[0]
        self.team = row[1]
        self.games = row[2]
        try:
            self.year = int(row[5])
        except:
            self.year = 0
    
    def get_year(self):
        return(self.year)
        
            
missing_year = Suspension(nfl_suspensions[22])
twenty_third_year = missing_year.get_year()
        
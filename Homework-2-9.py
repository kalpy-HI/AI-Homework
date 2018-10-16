import random
import sys

loc_environment = {'loc_A': random.choice(['Clean', 'Dirty']),
                   'loc_B': random.choice(['Clean', 'Dirty'])}
loc_now = random.choice(['loc_A', 'loc_B']) #for initial

def main():
    Total_score = 0
    for x in range(5):
        str1, score = HappyVacuum(loc_environment, loc_now)
        #print(str1)
        Total_score += score
    print(Total_score)

def HappyVacuum(status, where):
    loc_status = status.get(where)
    global loc_environment
    global loc_now
    if loc_status == 'Dirty':
        loc_environment.update({where: 'Clean'})
        perform = 10
        return 'Suck', perform
    elif where == 'loc_A':
        loc_now = 'loc_B'
        perform = -1
        return 'Right', perform
    elif where == 'loc_B':
        loc_now = 'loc_A'
        perform = -1
        return 'Left', perform

if __name__=='__main__':
    main()

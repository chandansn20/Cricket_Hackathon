#!user/bin/Python3.8

'''
author: Tarun R Jain
github : github.com/lucifertrj
'''

import matplotlib.pyplot as plt
import numpy as np
import random,statistics,sys,time

def totalovers():
    #enter 20 overs as user input
    try:
        while True:
            innings_overs=int(input("Enter number of overs:"))
            if innings_overs!=20:
                print("Its 20-20, Enter again: ")
                continue
            else:
                break
    except Exception as e:
        print("Invlaid Entry Occured",e)

    return innings_overs

def runs():
    #total possibilities in overs 0,1,2,4,6 and Wicket, consider a list runs

    runs = list(range(0,7))
    wicket = 'W'
    runs.append(wicket)
    return runs

def Team1(overs,runs):
    #consider Punjab Kings as team 1 and generate the random overs

    score = 0
    wickets = 0
    run_after_every_over=[]  #runs at end of every over

    for over in range(1,overs+1):
        print("Over:{} || Score:".format(over),end='')
        for run in range(6):
            run=random.choice(runs)
            if run==5 or run==3:
                run=random.randint(0,1)
                score+=run
            elif run == 'W':
                wickets+=1
                if wickets>9:
                    break
            else:
                score = score+run
            print(run,end=' ')

        run_after_every_over.append(score)
        print()

        if wickets>9:
            break

    return(score,wickets,run_after_every_over)

def Team2(overs,runs):
    #consider Team 2 Sunrises Hyderabad

    score2 = 0
    wickets2 = 0
    run_per_over2 = []      #runs scored in each over
    run_after_every_over2 = []    #runs at end of every over

    for over in range(1, overs + 1):
        print("Over:{} || Score:".format(over), end='')
        for run in range(6):
            run = random.choice(runs)
            if run == 5 or run == 3:
                run = random.randint(0, 1)
                score2 += run
            elif run == 'W':
                wickets2 += 1
                if wickets2 > 9:
                    break
            else:
                score2 = score2 + run
            print(run, end=' ')

        run_after_every_over2.append(score2)
        print()
        if wickets2 > 9:
            break

    return (score2, wickets2, run_after_every_over2)


def linegraph(overs,runs_per_over,runs_per_over2):
    plt.plot(np.array(list(range(len(runs_per_over)))), runs_per_over, 'red',label="PBKS", linewidth=5)
    plt.plot(np.array(list(range(len(runs_per_over2)))), runs_per_over2, 'orange',label="SRH", linewidth=5)
    plt.title("Punjab Kings vs Sunrises Hyderabad")
    plt.xlabel("Overs")
    plt.ylabel("Runs")
    plt.legend()
    plt.show()

def predict_score():
    predict_pbks=int(input("Predict Punjab Kings score: "))
    predict_srh=int(input("Predict Sunrises Hyderabad Score: "))
    return predict_pbks,predict_srh

def main():
    over=totalovers()
    run=runs()
    prediction_pbks, prediction_srh = predict_score()
    score,wicket,runs_per_over = Team1(over,run)
    print("{}/{}".format(score,wicket))
    print("Second Innnings Commencing in few sec...")
    time.sleep(1)
    score2,wicket2,runs_per_over2 = Team2(over,run)
    print("{}/{}".format(score2,wicket2))

    linegraph(over,runs_per_over,runs_per_over2)

    if prediction_pbks == score or prediction_pbks in range(score-20,score+20) or prediction_srh == score2 or prediction_srh in range(score2-20,score2+20):
        print("Quite a good prediction")
    elif prediction_pbks>score or prediction_srh>score2:
        print("Your guess is pretty high")
    elif prediction_pbks<score or prediction_srh<score2:
        print("Your guess is low")
    else:
        print("Your guess: Not bad")

if __name__ == '__main__':
    main()
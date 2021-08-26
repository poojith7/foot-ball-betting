import numpy as np
import os
import random
from collections import defaultdict
def riafML():
    Variable_Seed = 70
    gg = False
    random.seed(Variable_Seed)
    np.random.seed(Variable_Seed)
    os.environ['POOJITHSEED'] = str(Variable_Seed)
    ddict = defaultdict(list)
    nik_poo = 7000
    kl = ["DRAW", "DRAW", "HOME", "SKIP"]
    n = input()
    for _ in range(int(n)):
        Division, Time, home_team, away_team, Referee, home_coef, draw_coef, away_coef = input().split()
        flag = 0
        home_coef = float(home_coef)
        draw_coef = float(draw_coef)
        away_coef = float(away_coef)

        # avg = (home_coef + draw_coef + away_coef) / 3
        # if avg >= 4.17:
            # y_pred = np.argmin(np.array([away_coef, draw_coef, home_coef]))

        if home_coef >= (draw_coef  + away_coef):
            # print("HOME")
            # sys.stdout.flush()
            print("HOME", flush=True)
        elif  draw_coef >= (home_coef +away_coef ):
            # print("DRAW")
            # sys.stdout.flush()
            print("DRAW", flush=True)
        elif away_coef >= (draw_coef  +home_coef ):
            # sys.stdout.flush()
            # print("HOME", flush=True)
            print("AWAY", flush=True)

        else:
            # print("DRAW",flush=True)
            # print("AWAY", flush=True)
            # print("HOME", flush=True)
            print(random.choice(kl), flush=True)

        full_time_home,full_time_away,half_time_home,half_time_away,home_shots,away_shots,hs_on_target,as_on_target, home_fouls,away_fouls, home_corners,away_corners,home_yellow_cards,away_yellow_cards,home_red_cards,away_red_cards= input().split()
        try:
            home_goals = int(full_time_home)
        except:
            home_goals = 0
        try:
            away_goals = int(full_time_away)
        except:
            away_goals = 0
        if home_goals == away_goals:
            ddict["DRAW"].append(round(away_coef))
        elif home_goals > away_goals:
            ddict["HOME"].append(round(home_coef))
        else:
            ddict["AWAY"].append(round(draw_coef))

if __name__ == "__main__":
    riafML()

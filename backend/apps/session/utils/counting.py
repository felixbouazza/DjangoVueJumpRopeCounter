import pandas as pd


def counting_jump_on_last_second(point, lastSecondData, jumpCounter):
    lastSecondData.append(point)
    if len(lastSecondData) == 10:
        # print("I analyze")
        condition = False
        df = pd.Series(lastSecondData)
        mean = df.mean()
        for el in df:
            if el > mean and condition == True:
                jumpCounter = jumpCounter + 1
                condition = False
            if el < mean and condition == False:
                condition = True
        lastSecondData.clear()
    return {
        'lastSecondData': lastSecondData,
        'jumpCounter': jumpCounter
    }

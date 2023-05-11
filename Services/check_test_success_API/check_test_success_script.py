import pandas as pd
import datetime as dt


def check_test_success(test_id):
    """
        Load in a CSV file and converting some of the data so it can be used in this script
        Starts by converting the dataframes discovered in pandas into lists, which can be used further down in the script
    """
    data = pd.read_csv("Services\check_test_success_API\_test_data\\"+test_id+ ".csv", sep=';')
    presure = []
    logTimes = []
    stepNos = []

    for x in data['B22']:
        if "," in x:
            myStr = x.replace(",", ".")
            presure.append(float(myStr))
        else:
            presure.append(float(str))

    for x in data['Log Time']:
        dt_obj = dt.datetime.strptime(x, '%d/%m/%Y %H.%M.%S')
        logTimes.append(dt_obj)
        
    for x in data['StepNo']:
        stepNos.append(x)

    test_list = []
    success = 0
    fails = 0

    """
        Main part of the script
        Looks at each data entry for presure, and compares it to the previous data entry, but only for the data entry
        which is part of the step number between 44000 and 45000
        if the difference between the two data points is less than 0.1%, the test is successful
        but if the difference is higher, the test fails and returns test failed
    """
        
    for time,step,pres in zip(logTimes, stepNos, presure):
        if step == 44000 or step == 44500 or step == 45000:
            test_list.append(pres)
            if len(test_list) >= 2:
                pres_diff = test_list[-2] / test_list[-1]
                if pres_diff > 0.99 and pres_diff < 1.01:
                    success = success + 1
                else:
                    fails = fails + 1
                    return ['Test failed'+ ' ' + str(time)]
        else:
            continue
    """
    If the test is successful, the script returns test successful
    """
    
    return ['Test successful']

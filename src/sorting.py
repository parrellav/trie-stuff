import statistics
from src.quickVinny import quick_sort


# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    length = len(expenditure)
    exps_sorted = quick_sort(expenditure.copy(), 0, length - 1)
    median_index = statistics.median(expenditure)
    median_value = expenditure[median_index]
    start = 0
    notifications = 0
    for index in range(d, length):
        small_list = expenditure[start:index]
        for i in small_list:
            if i >= 2 * median_value:
                notifications += 1
        if start == 0:
            start += index
        else:
            start += 1
    return notifications



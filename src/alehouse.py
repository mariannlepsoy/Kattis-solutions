from sys import stdin, stdout

def get_best_timeintervall():
    n, k = stdin.readline().split()
    times = count_guests(int(n), int(k))

    count = 0
    n_friends = 0

    #For each time in times, check if guest is leaving or arriving. 
    #Keep the highest number of count or n_friends to find the highest number of friends we can make.
    for t in times:
        if t[1] == "arrive":
            count += 1
        else:
            count -= 1
        n_friends = max(count, n_friends)

    return n_friends

#Create list of guests arrival and leave times. 
def count_guests(n, k):
    times = []
    for _ in range(n):
        arrive, leave = stdin.readline().split()
        times.append((int(arrive), "arrive"))
        #Increment leave time with k to account for time we spend at bar.
        times.append((int(leave)+k, "leave"))
    times.sort()
    return times

stdout.write(str(get_best_timeintervall()))
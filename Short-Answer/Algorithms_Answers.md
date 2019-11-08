#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) `O(n)` run time. For every n, function will loop n times


b) `log(n) because j approaches `base` of being greater than n at a rate that decreases the gap between j and n by half with every loop


c) `O(n)` because for every n, function recures n times

## Exercise II
------------------------------------------------
def find_f(n):

    f = None

    for i in range(0, n):
        if egg_breaks == False:
            continue
        else:
            f = i
            break

    return f + 1
    # plus one is to shift from 0th floor to 1st floor
-------------------------------------------------

The algorithm has a time complexity of O(n) because at it's worst case, with n being a large number and f being the top floor, it would take n loops to find f. More specifically, O(n-f) time complexity




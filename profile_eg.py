##  Example of profilibf a code
##  http://stackoverflow.com/questions/582336/how-can-you-profile-a-python-script
##
##
def count():
    from math import sqrt
    for x in range(10**5):
        sqrt(x)

import cProfile, pstats
cProfile.run("count()", "{}.profile".format(__file__))
s = pstats.Stats("{}.profile".format(__file__))
s.strip_dirs()
s.sort_stats("time").print_stats(10)



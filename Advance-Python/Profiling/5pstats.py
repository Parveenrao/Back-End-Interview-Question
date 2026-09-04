""" 

=> pstats

    -> pstats is a python built-in module used to read , sort filter and analyze profile data

       produced by cprofile

"""

import cProfile


def square() -> None:
    total = 0
    for i in range(5_000_000):
        total += i * i


def cube() -> None:
    total = 0
    for i in range(3_000_000):
        total += i ** 3


def main() -> None:
    square()
    cube()


profiler = cProfile.Profile()

profiler.enable()

main()

profiler.disable()

profiler.dump_stats("profile.stats")


# read the profile data

import pstats

stats = pstats.Stats("profile.stats")

stats.print_stats

# sorting result , sort by tottime

stats.sort_stats("tottime")

stats.print_stats


# sort by cumtime 

stats.sort_stats("cumtime")

# show only top 10 function

stats.print_stats(10)


# filter by function name

stats.print_stats("train")

# chaining operation 

stats.sort_stats("cumtime").print_stats(10)

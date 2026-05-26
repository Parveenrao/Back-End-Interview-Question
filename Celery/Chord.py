"""
=> Chord 
    
    -> group(parallel taks) + callbacks (after all finish)
    
    Task A -
    Task B -  All three are running parallely + Final task (callback)
    Task C - 

"""


def add(a , b):
    return a + b


def sum_results(results):
    return sum(results)


from celery import chord

result = chord(
    [
        add.s(2, 3),
        add.s(4, 5),
        add.s(6, 7)
    ]
)(sum_results.s())
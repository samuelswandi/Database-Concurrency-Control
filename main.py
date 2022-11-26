from lock import *
from algorithms.simple_locking import simple_locking

def preprocessData():
    # preprocess case
    datas = set()
    queue = []

    # reading case
    case = open("case.txt", "r")
    lines = case.read().split(",")

    print("Original case:", lines)
    print()

    for t in lines:
        queue.append(t)
        command = t[0]
        if command == "C":
            continue
        
        data = t[2]
        datas.add(data)

    # Declare locks for every data
    # Default is XL locks
    locks = []
    for data in datas:
        locks.append(Lock(data))

    # return queue, list of transactions and locks
    return queue, locks

if __name__ == "__main__":
    q, l = preprocessData()
    simple_locking(q,l)
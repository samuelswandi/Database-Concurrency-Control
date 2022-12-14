from collections import deque
import time

class Lock:
    def __init__(self, data, type="XL"):
        """
        owner = which transactions currenly has this locks
        data = what data that this locks give
        """
        self.data = data
        self.owner = "-1"
        self.type = type #XL or SL

    def getData(self):
        return f"{self.type}{self.owner}({self.data})"

    def getReleaseData(self):
        return f"UL{self.owner}({self.data})"

    def grantLock(self, owner) -> bool:
        """
        Grant Locks to owner
        but if locks is XL, then can't give locks
        """
        if owner == self.owner:
            return True
            
        if self.type == "XL" and self.owner != "-1":
            print(f"[Locks {self.data}] locks can't be given to {owner}")
            return False

        print(f"[Locks {self.data}] locks has been given to {owner}")
        self.owner = owner
        return True

    def releaseLock(self):
        """
        Release locks
        """
        print(f"[Locks {self.data}] locks has been released")
        self.owner = "-1"
        return True

def searchForLock(data, locks) -> Lock:
    for lock in locks:
        if lock.data == data:
            return lock

def searchForLocksByOwner(owner, locks):
    allLocks = []
    for lock in locks:
        if lock.owner == owner:
            allLocks.append(lock)

    return allLocks

    
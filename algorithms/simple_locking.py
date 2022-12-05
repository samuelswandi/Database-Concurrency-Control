from lock import *

def simple_locking(q, locks):
    """
    Simple locking using exclusive locks
    """
    copyQ = q
    result = []

    while len(q) > 0:
        curr = q.pop(0)
        currC = curr[0]
        currTx = curr[1]
        print(f"\n[Current Transaction] {curr}")

        # if current command is Commit
        # then release all locks of currTx transactions
        if currC == "C":
            ownersLocks = searchForLocksByOwner(currTx, locks)
            print(f'[Transaction {currTx}] Commit. Releasing all locks for this transaction')
            for lock in ownersLocks:
                result.append(lock.getReleaseData())
                lock.releaseLock()
            result.append(f"C{currTx}")

        # else, create locks for this data
        # iff locks for this data has no owner
        else:
            currLockData = curr[2]
            currLock = searchForLock(currLockData, locks)

            # check if curr data can be lock
            canBeLocked = currLock.grantLock(currTx)

            # if can be locked, then process to lock
            if canBeLocked:
                result.append(currLock.getData())
                result.append(f"{currC}{currTx}({currLockData})")
                print(f'[Transaction {currTx}] command {currC} for {currLockData} ')

            # if cant be locked, then queue all transaction from this transaction
            # until release / commit of the transaction that has the lock
            # and release all lock from this transaction
            else:
                print(f'[Transaction {currTx}] ROLLBACK detected ')
                print(f'[Transaction {currTx}] transaction queued to after commit from {currLock.owner} ')

                # extract new queue 
                newQ = [i for i in q if i[1] != currTx]

                # record current transaction until the last transaction
                currQ = [i for i in copyQ if i[1] == currTx]
                currQ.insert(0, curr)
                
                # put the current transaction to last of the queue
                resultQ = newQ + currQ

                q = resultQ

                # release locks from this transaction
                ownersLocks = searchForLocksByOwner(currTx, locks)
                for lock in ownersLocks:
                    result.append(lock.getReleaseData())
                    lock.releaseLock()

            
    
    print("\nResult", "; ".join(result))
    return ": ".join(result)
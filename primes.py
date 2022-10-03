"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

from multiprocessing.sharedctypes import Value


def primes(number_of_primes):
    if number_of_primes<=0:
        raise(ValueError)
    else:
        list = [2]
        curNum=3

        while len(list)<number_of_primes:
            isPrime=True
            divider=2
            while divider<curNum:
                if curNum%divider==0:
                    isPrime=False
                divider=divider+1
            
            if isPrime:
                list.append(curNum)

            curNum=curNum+1

        return list
        




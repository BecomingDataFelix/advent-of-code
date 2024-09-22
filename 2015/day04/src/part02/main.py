import multiprocessing
import hashlib
from time import time

data = 'iwrupvqb'

def getSmallestHash(numbers):
    for i in numbers:
        hash = hashlib.md5((data + str(i)).encode())
        if str(hash.hexdigest())[:6] == '000000':    
            print(i)
        #print(str(hash.hexdigest())[:6])

if __name__ == '__main__':
    num_range = range(1 , 10000000)
    num_of_cores = multiprocessing.cpu_count() 
    pool = multiprocessing.Pool(processes = num_of_cores)
    
    chunk_size = len(num_range) // num_of_cores
    chunks = [num_range[i : i+chunk_size] for i in range(0, len(num_range), chunk_size)]

    
    results = pool.map(getSmallestHash, chunks)

    print ("cores =" + str(num_of_cores))
    pool.close()
    pool.join()
    

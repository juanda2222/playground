from numpy.random import Generator, PCG64
import multiprocessing
import concurrent.futures
import numpy as np

# to calculate the bernoulli randomness
from scipy.stats import bernoulli

# use this to see the results
import matplotlib.pyplot as plt

#benchmark the multi threading
from time import time

class MultithreadedRNG(object):
    def __init__(self, n, seed=None, number_of_threads=None):
        rg = PCG64(seed)
        if number_of_threads is None:
            number_of_threads = multiprocessing.cpu_count()
        self.number_of_threads = number_of_threads

        self._random_generators = [rg]
        last_rg = rg
        for _ in range(0, number_of_threads-1):
            new_rg = last_rg.jumped()
            self._random_generators.append(new_rg)
            last_rg = new_rg

        self.n = n
        self.executor = concurrent.futures.ThreadPoolExecutor(number_of_threads) # use this  object to multithread
        self.value_array = np.empty(n) # reserve the array memory
        self.step = np.ceil(n / number_of_threads).astype(np.int_) # round up to get the number of steps

    def _thread_fill(self, rg, out, first, last):
        p = 0.3
        
        # x = np.random.randn(N_points) # this uses a normal distribution
        self.value_array[first:last] = bernoulli.rvs(p, size=len(out[first:last]))
        #self.value_array[first:last] = np.random.standard_normal(len(out[first:last]))

    def fill(self):

        futures = {}
        for i in range(self.number_of_threads):
            args = (
                self._thread_fill,
                self._random_generators[i],
                self.value_array,
                i * self.step,
                (i + 1) * self.step
                )
            
            # this is a simple object to signal is complete
            futures[self.executor.submit(*args)] = i

        # wait for all the proccess to finish
        concurrent.futures.wait(futures)

    def __del__(self):
        self.executor.shutdown(False)

if __name__ == "__main__":

    arr_size = 1000000

    # populate using multi thread
    mrng = MultithreadedRNG(arr_size, seed=0)
    multi_thread_time1 = time()
    mrng.fill()
    mrng.__del__()
    print("Multi thread time: ", time() - multi_thread_time1)
    
    # populate using single thread
    single_thread_time1 = time()
    vec = np.random.standard_normal(arr_size)
    print("Single thread time: ", time() - single_thread_time1)

    # see the results
    print("Results: ", mrng.value_array)
    fig, axs = plt.subplots(2, sharex=False)
    axs[0].hist(vec, bins=30)
    axs[0].set_title('Standard distribution')
    axs[1].hist(mrng.value_array, bins=30)
    axs[1].set_title('Bernouli distribution')
    fig.tight_layout()
    plt.show()
"""
Efficiently select the k-smallest element

Author: Christopher Gondek
"""

import random


def randomized_select_loop(data, k):
    """Returns the k-smallest (zero-based) item of a list.
    
    Parameters
    ----------
    data : list
        List of comparable elements.
    k : int
        The k smallest element to return.
        
    Returns
    -------
    data[x]
        The k-smallest element in the list.
    """

    if not 0 <= k < len(data):
        raise ValueError('Error: k out of bounds!')
    while True:
        pivot = random.choice(data)
        pivot_cnt = 0
        lt, gt = [], []
        lt_app = lt.append
        gt_app = gt.append
        for element in data:
            if element < pivot:
                lt_app(element)
            elif element > pivot:
                gt_app(element)
            else:
                pivot_cnt += 1
        l = len(lt)
        if k < l:
            data = lt
        else:
            l += pivot_cnt
            if k < l:
                return pivot
            else:
                data = gt
                k -= l

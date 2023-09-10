from collections import Counter
import heapq

def topKFrequent(nums, k):
    """
    We utilize the Counter from collections to get the frequency of each number.
    Then, we use a heap to get the top k frequent numbers.
    """
    count = Counter(nums)
    return heapq.nlargest(k, count.keys(), key=count.get)

nums = [1,1,1,2,2,3]
print(topKFrequent(nums, 2))  # Outputs: [1,2]

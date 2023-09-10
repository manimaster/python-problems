def findDuplicate(nums):
    """
    This solution uses the Floyd's Tortoise and Hare (Cycle Detection) to detect the loop 
    caused by the duplicate number. Once the loop is detected, we reinitialize one pointer
    to the start and then move both pointers step by step until they meet again, which will 
    be the start of the loop or the duplicate number.
    """
    tortoise = nums[0]
    hare = nums[0]

    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if tortoise == hare:
            break

    hare = nums[0]
    while hare != tortoise:
        hare = nums[hare]
        tortoise = nums[tortoise]

    return hare

nums = [3,1,3,4,2]
print(findDuplicate(nums))  # Outputs: 3

def find_min(nums):
    
    smallest = float("inf")

    for i in nums:

        if i <= smallest:
            smallest = i
        
    return smallest


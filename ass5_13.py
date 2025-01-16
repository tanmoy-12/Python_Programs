def waterTrapped(height):
    n = len(height)
    left = [0] * n
    right = [0] * n
    left[0] = height[0]
    right[n-1] = height[n-1]
    
    # Calculate the maximum water that can be trapped to the left of each index
    for i in range(1, n):
        left[i] = max(left[i-1], height[i])
    
    # Calculate the maximum water that can be trapped to the right of each index
    for i in range(n-2, -1, -1):
        right[i] = max(right[i+1], height[i])
    
    # Calculate the total water that can be trapped
    total = 0
    for i in range(n):
        total += min(left[i], right[i]) - height[i]
    
    return total
height = [0,1,0,2,1,0,1,3,2,1,2,1]

print(waterTrapped(height))
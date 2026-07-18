import random

# Global variable to count comparisons in Divide & Conquer approach
comparison_count = 0 

def min_max_dc(arr, low, high):
    global comparison_count
    
    # Base case: 1 element
    if low == high:
        return arr[low], arr[low]
        
    # Base case: 2 elements
    if high == low + 1:
        comparison_count += 1
        if arr[low] < arr[high]:
            return arr[low], arr[high]
        return arr[high], arr[low]
        
    # Divide step
    mid = (low + high) // 2
    lmin, lmax = min_max_dc(arr, low, mid)
    rmin, rmax = min_max_dc(arr, mid + 1, high)
    
    # Combine step (Conquer)
    comparison_count += 1
    if lmin < rmin:
        overall_min = lmin
    else:
        overall_min = rmin
        
    comparison_count += 1
    if lmax > rmax:
        overall_max = lmax
    else:
        overall_max = rmax
        
    return overall_min, overall_max

def min_max_naive(arr):
    mn = arr[0]
    mx = arr[0]
    comps = 0
    
    for x in arr[1:]:
        comps += 1
        if x < mn: 
            mn = x
        comps += 1
        if x > mx: 
            mx = x
            
    return mn, mx, comps

# --- Part 1: Testing on a Small Sample Array ---
arr = [3, 1, 7, 4, 9, 2, 8, 5, 6, 0]
comparison_count = 0

mn, mx = min_max_dc(arr, 0, len(arr) - 1)
dc_comps = comparison_count
_, _, naive_comps = min_max_naive(arr)

print("Array:", arr)
print("Calculated Min:", mn)
print("Calculated Max:", mx)
print("Divide & Conquer Comparisons:", dc_comps)
print("Naive Linear Comparisons:", naive_comps)
print()

# --- Part 2: Performance Evaluation Table ---
print("Size   |  DC Comps  |  Naive Comps  |  Formula (3n/2 - 2)")
print("-" * 55)

sizes = [10, 100, 1000, 10000]

for size in sizes:
    # Generate random test list of the given size
    test_arr = [random.randint(1, 10000) for _ in range(size)]
    
    # Test Divide and Conquer method
    comparison_count = 0
    min_max_dc(test_arr, 0, len(test_arr) - 1)
    dc = comparison_count
    
    # Test Naive Linear method
    _, _, naive = min_max_naive(test_arr)
    
    # Mathematical bound calculation
    formula = (3 * size) // 2 - 2
    
    print(f"{size:<6} |  {dc:<8}  |  {naive:<11}  |  {formula}")

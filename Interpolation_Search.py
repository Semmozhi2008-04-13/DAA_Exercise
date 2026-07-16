def interpolation_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high and target >= arr[low] and target <= arr[high]:
        if low == high:
            return low if arr[low] == target else -1

        # Calculate estimated position
        pos = low + ((target - arr[low]) * (high - low)) // (arr[high] - arr[low])

        # Trace print statement to make your screenshot look like a proper DAA lab report
        print(f"[Trace] Low: {low}, High: {high}, Probing Index: {pos}, Value: {arr[pos]}")

        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
            
    return -1

# --- Interactive Array Input and Search Execution ---
if __name__ == "__main__":
    print("=== DAA Lab: Interpolation Search ===")
    
    # 1. Accept list from user
    raw_input = input("Enter array numbers (separated by spaces): ")
    
    # Convert input string into a list of integers and sort it
    dataset = sorted([int(num) for num in raw_input.split()])
    print(f"Processed & Sorted Array: {dataset}")
    
    # 2. Accept search target
    target_val = int(input("Enter the target element to search for: "))
    
    # 3. Execute search
    result = interpolation_search(dataset, target_val)
    
    # 4. Output evaluation
    print("\n=== Search Result ===")
    if result != -1:
        print(f"Success! Element {target_val} found at index: {result}")
    else:
        print(f"Element {target_val} does not exist in the array.")

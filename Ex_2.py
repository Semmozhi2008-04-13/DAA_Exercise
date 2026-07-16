import time

# ==========================================
# 1. NAIVE STRING MATCHING
# ==========================================
def naive_search(text, pattern):
    n = len(text)
    m = len(pattern)
    matches = []
    
    # Iterate through all possible windows of the text
    for i in range(n - m + 1):
        if text[i : i + m] == pattern:
            matches.append(i)
            print(f"[Naive] Match found at index {i}")
            
    return matches

# ==========================================
# 2. KMP (KNUTH-MORRIS-PRATT) MATCHING
# ==========================================
def kmp_failure_function(pattern):
    m = len(pattern)
    lps = [0] * m  # Longest Proper Prefix which is also Suffix
    length = 0
    i = 1
    
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        elif length != 0:
            length = lps[length - 1]
        else:
            lps[i] = 0
            i += 1
    return lps

def kmp_search(text, pattern):
    n = len(text)
    m = len(pattern)
    lps = kmp_failure_function(pattern)
    matches = []
    
    i = 0  # Index for text
    j = 0  # Index for pattern
    
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
            
        if j == m:
            match_index = i - j
            matches.append(match_index)
            print(f"[KMP] Match found at index {match_index}")
            j = lps[j - 1]
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
                
    return matches

# ==========================================
# 3. RABIN-KARP STRING MATCHING
# ==========================================
def rabin_karp(text, pattern, q=101):
    n = len(text)
    m = len(pattern)
    d = 256  # Number of characters in the input alphabet
    h = pow(d, m - 1, q)
    p_hash = 0  # Hash value for pattern
    t_hash = 0  # Hash value for first window of text
    matches = []
    
    # Calculate the initial hash value of pattern and first window
    for i in range(m):
        p_hash = (d * p_hash + ord(pattern[i])) % q
        t_hash = (d * t_hash + ord(text[i])) % q
        
    # Slide the pattern over text one by one
    for s in range(n - m + 1):
        # Check if the hash values match
        if p_hash == t_hash:
            # Spurious hit check: Verify character by character
            if text[s : s + m] == pattern:
                matches.append(s)
                print(f"[Rabin-Karp] Match found at index {s}")
                
        # Calculate hash value for next window of text
        if s < n - m:
            t_hash = (d * (t_hash - ord(text[s]) * h) + ord(text[s + m])) % q
            # Convert negative hash value to positive
            if t_hash < 0:
                t_hash = t_hash + q
                
    return matches

# ==========================================
# DRIVER EXECUTION CODE
# ==========================================
if __name__ == "__main__":
    print("=== CS5303 DAA Lab | Ex. No. 2 ===")
    print("Comparative Analysis of String Matching Algorithms\n")
    
    # Take runtime string inputs from user
    text_input = input("Enter the Text: ")
    pattern_input = input("Enter the Pattern to search: ")
    
    print("\n--- Running Search Algorithms ---")
    
    # 1. Naive Search Profiling
    start = time.perf_counter()
    naive_res = naive_search(text_input, pattern_input)
    naive_time = (time.perf_counter() - start) * 1000
    
    # 2. KMP Search Profiling
    start = time.perf_counter()
    kmp_res = kmp_search(text_input, pattern_input)
    kmp_time = (time.perf_counter() - start) * 1000
    
    # 3. Rabin-Karp Search Profiling
    start = time.perf_counter()
    rk_res = rabin_karp(text_input, pattern_input)
    rk_time = (time.perf_counter() - start) * 1000
    
    # Performance Output Table
    print("\n=== Comparative Analysis Report ===")
    print(f"{'Algorithm':<15} | {'Execution Time (ms)':<20} | {'Matches Found'}")
    print("-" * 55)
    print(f"{'Naive':<15} | {naive_time:<20.4f} | {len(naive_res)}")
    print(f"{'KMP':<15} | {kmp_time:<20.4f} | {len(kmp_res)}")
    print(f"{'Rabin-Karp':<15} | {rk_time:<20.4f} | {len(rk_res)}")

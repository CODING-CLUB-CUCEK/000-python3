from itertools import permutations

def print_permutations(s, k):
    # Generate permutations
    perms = permutations(s, k)
    
    # Sort permutations lexicographically
    sorted_perms = sorted(perms)
    
    # Print permutations
    for perm in sorted_perms:
        print(''.join(perm))

# Read input from a single line
if __name__ == '__main__':
    input_str = input()
    string, k = input_str.split()

    # Call the function
    print_permutations(string, int(k))

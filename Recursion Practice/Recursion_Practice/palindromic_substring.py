def isPalindrome(string):
    return string == string[::-1]

def solve(string, new_list_one, new_list_two):
    if len(string) == 0:
        new_list_one.append(new_list_two.copy())  # Using copy to avoid modifying original list
        return
    for i in range(len(string)):
        piece = string[0:i + 1]
        if isPalindrome(piece):
            new_list_two.append(piece)
            remain = string[i + 1:]
            solve(remain, new_list_one, new_list_two)
            new_list_two.pop()  # Use pop to remove the last element

def palindromic_substrings(string):
    palindromic_substrings = []
    solve(string, palindromic_substrings, [])
    return palindromic_substrings

result = palindromic_substrings("aab")
print(result)

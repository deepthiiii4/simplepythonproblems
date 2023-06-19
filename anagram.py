def is_anagram(s1, s2):
    c = 0
    for char in s1:
        if char in s2:
            c = c + 1

    if c == len(s1):
        print("It is an anagram")
    else:
        print("Invalid")

s1 = input("Enter string 1: ")
s2 = input("Enter string 2: ")
is_anagram(s1, s2)

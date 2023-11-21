# Palindrome is "Madam", "Naman"

def palindrome(st):
    sv2= ''
    for i in range(len(st), 0, -1):
        i = i-1
        sv2 = sv2 + st[i]
    if st == sv2:
        print("Yes")
    else:
        print("No")

st = "madam"
palindrome(st)


def palindrome(st):
    sv2 = st[::-1]
    if st == sv2:
        print("Yes")
    else:
        print("No")


st = "madam"
palindrome(st)


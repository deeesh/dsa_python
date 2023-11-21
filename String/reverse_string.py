def reverse_string(str1):
    rev = ''
    for i in str1:
        rev = i + rev
    print(rev)
reverse_string("abcdefg")
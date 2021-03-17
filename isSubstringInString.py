def isSubstring(pattern, original):
    if pattern in original:
        return True
    if pattern not in original:
        return False

print(isSubstring('hij', 'abcdefghijklmnop'))
print(isSubstring('xyz', 'abcdefghijklmnop'))

# 문제
# An anagram of a string is formed by rearranging the letters in the string. For example, the anagrams of aab are aab, aba, and baa.

# A wildcard anagram of a string is an anagram of the string where some of the letters might have been replaced with an asterisk (*). For example, two possible wildcard anagrams of aab are *ab and *b*.

# Given two strings, determine whether the second string is a wildcard anagram of the first string.

# 입력
# The two lines of input will both consist of N (1 ≤ N ≤ 100) characters. Each character in the first line will be a lowercase letter. Each character in the second line will be either a lowercase letter or an asterisk.

# 출력
# Output the character A if the string on the second line is a wildcard anagram of the string on the first line. Otherwise, output the character N.

# 예제 입력 1 
# abba
# baaa
# 예제 출력 1 
# N
# 예제 입력 2 
# cccrocks
# socc*rk*
# 예제 출력 2 
# A


in1 = sorted(' '.join(input()).split())
in2 = sorted(' '.join(input()).split())

for i in in1[:]:
    if in1.count(i) > 0 and in2.count(i) > 0:
        in1.remove(i)
        in2.remove(i)


#print(f"{in1}\n{in2}")

if all(i == '*' for i in in2):
    print('A')
else:
    print('N')
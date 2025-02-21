# Write your solution to exercise 1 here
def counter(str2):
    freq = {}
    for c in str2:
        if c in freq:
            freq[c] += 1
        else:
            freq[c] = 1
    return (freq)
str2 = ""
while True:
    str1 = input("Enter a string: ")
    if str1 == "":
        break
    str2 = str2 + str1

n = int(input("Minimum number of characters: "))
dic =counter(str2)
j = 0
sorted_dic = {k: v for k, v in sorted(dic.items(), key=lambda item: item[1], reverse=True)}
print("Characters in order of occurrence:")
for i in sorted_dic:
    if sorted_dic[i] >= n:
        print(f'Character "{i}" was entered {sorted_dic[i]} times')

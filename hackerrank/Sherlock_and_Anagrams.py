def sherlockAndAnagrams(s):
    answer = 0
    dict_str = {}

    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            sub_str = ''.join(sorted(s[i:j]))
            if sub_str in dict_str.keys():
                answer += dict_str[sub_str]
                dict_str[sub_str] += 1
            else:
                dict_str[sub_str] = 1
    return answer


q = int(input())
for _ in range(q):
    s = input()
    result = sherlockAndAnagrams(s)
    print(result)


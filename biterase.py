memo = {}

def count(s):
    if s == "":
        return 1
    if s in memo:
        return memo[s]
    if len(s) % 2 != 0:
        return 0
    else:
        result = 0
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                result += count(s[:i-1] + s[i+1:])
        memo[s] = result

        return result


if __name__ == "__main__":
    print(count("1100")) # 2
    print(count("1001")) # 1
    print(count("100111"))  # 5
    print(count("11001")) # 0
    print(count("1100110011100111")) # 113925
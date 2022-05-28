
roman = input("Insert a roman number: ")


def roman_to_int(s: str) -> int:
    roman_corespondents = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    # 'for' ignoring last symbol/number, so we need to add it.
    total = roman_corespondents[s[-1]]
    for i in range(1, len(s)):
        # for example XC=90, X=10 < C=100, we need to subtract X from total, then will add C
        if roman_corespondents[s[i - 1]] < roman_corespondents[s[i]]:
            total -= roman_corespondents[s[i - 1]]
        else:
            total += roman_corespondents[s[i - 1]]
        return total


print(roman_to_int(roman))


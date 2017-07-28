nums = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
    100: 'hundred',
    1000: 'thousand'
}

result = 0

for i in range(1, 1001):
    # handle one digit numbers
    if len(str(i)) == 1:
        result += len(str(nums[i]))
    # handle two digit numbers
    elif len(str(i)) == 2:
        try:
            # if the number is simple (in the list)
            result += len(str(nums[i]))
        except:
            # if the number is complex (not in the list)
            result += len(nums[int(str(i)[0]) * 10]) + len(nums[int(str(i)[1])])
    # handle three digit numbers
    elif len(str(i)) == 3:
        try:
            # if the number is simple (in the list)
            result += len("one") + len(str(nums[i]))
        except:
            # if the number is simple (divisible by 100)
            if i % 100 == 0:
                result += len(nums[int(str(i)[0])]) + len(nums[100])
                continue
            # if the number is complex (not in the list)
            # if the second half is simple (in the list)
            try:
                result += len(nums[int(str(i)[0])]) + len(nums[int(str(i)[1:])]) + len(nums[100]) + len("and")
            # if the second half is complex (not in the list)
            except:
                result += len(nums[int(str(i)[0])]) + len(nums[int(str(i)[1]) * 10]) + len(nums[int(str(i)[2])]) + len(nums[100]) + len("and")
    # handle four digit numbers
    elif len(str(i)) == 4:
        result += len("one") + len(str(nums[1000]))

print(result)
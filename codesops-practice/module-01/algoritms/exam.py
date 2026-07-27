# Question 1: Even Numbers at Even Indexes
def getOnlyEvens(arr: list[int]) -> None:
    """Print even numbers located at even indexes."""
    result = []
    for index, num in enumerate(arr):
        if index % 2 == 0 and num % 2 == 0:
            result.append(num)
    print(result)

# Test Cases
getOnlyEvens([1, 2, 3, 6, 4, 8])  # Output: [4]
getOnlyEvens([0, 1, 2, 3, 4])     # Output: [0, 2, 4]

def reverseCompare(num: int) -> None:
    """Compare a number with its reversed digit form."""
    reversed_num = int(str(num)[::-1])
    if num > reversed_num:
        print("Ok")
    else:
        print("Not ok")

# Test Cases
reverseCompare(72)  # Output: Ok
reverseCompare(23)  # Output: Not ok
def reverseCompare(num: int) -> None:
    """Compare a number with its reversed digit form."""
    reversed_num = int(str(num)[::-1])
    if num > reversed_num:
        print("Ok")
    else:
        print("Not ok")

# Test Cases
reverseCompare(72)  # Output: Ok
reverseCompare(23)  # Output: Not ok

# Question 2: Reverse and Compare


def reverseCompare(num: int) -> None:
    """Compare a number with its reversed digit form."""
    reversed_num = int(str(num)[::-1])
    if num > reversed_num:
        print("Ok")
    else:
        print("Not ok")

# Test Cases
reverseCompare(72)  # Output: Ok
reverseCompare(23)  # Output: Not ok


# Question 3: Factorial Calculation

def returnFactorial(n: int) -> int:
    """Calculate and return the factorial of n."""
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Test Cases
print(returnFactorial(5))  # Output: 120
print(returnFactorial(6))  # Output: 720
print(returnFactorial(0))  # Output: 1

# Question 4: Meera Array Check

def checkMeera(arr: list[int]) -> None:
    """Check if an array contains no value that is double another value."""
    num_set = set(arr)
    for n in arr:
        if n == 0:
            if arr.count(0) > 1:
                print("I am NOT a Meera array")
                return
            continue
        if (n * 2) in num_set:
            print("I am NOT a Meera array")
            return
    print("I am a Meera array")

# Test Cases
checkMeera([10, 4, 0, 5])     # Output: I am NOT a Meera array
checkMeera([7, 4, 9])         # Output: I am a Meera array
checkMeera([1, -6, 4, -3])    # Output: I am NOT a Meera array

# Question 5: Dual Array Validation

from collections import Counter

def isDual(arr: list[int]) -> int:
    """Return 1 if every element appears exactly twice, otherwise 0."""
    if not arr or len(arr) % 2 != 0:
        return 0
    counts = Counter(arr)
    for count in counts.values():
        if count != 2:
            return 0
    return 1

# Test Cases
print(isDual([1, 2, 1, 3, 3, 2]))  # Output: 1
print(isDual([2, 5, 2, 5, 5]))     # Output: 0
print(isDual([3, 1, 1, 2, 2]))     # Output: 0

# Question 6: Digital Clock Converter

def digitalClock(seconds: int) -> str:
    """Convert total seconds into HH:MM:SS format."""
    seconds = seconds % 86400
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    return f"{hours:02d}:{minutes:02d}:{secs:02d}"

# Test Cases
print(digitalClock(5025))   # Output: 01:23:45
print(digitalClock(61201))  # Output: 17:00:01
print(digitalClock(87000))  # Output: 00:10:00
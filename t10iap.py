def fibonacci_array(n: int) -> list[int]:
    fibo = [0, 1]
    if n <= 2:
        return fibo[:n]
    def fibonacci(m: int, fibonn: list[int]) -> list[int]:
        if m == 2:
            return fibonn
        next = fibonn[-1] + fibonn[-2]
        fibonn.append(next)
        m -= 1
        return fibonacci(m, fibonn)
    return fibonacci(n, fibo)

#print(fibonacci_array(1))


def fibo_generator(n: int):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

def fibonacci(a: int) -> list[int]:
    return [0] if a == 0 else  list(fibo_generator(a))

#print(fibonacci(10))


def christmas_tree(n: int) -> None:
    for i in range(n):
        stars = '*' * (2 * i + 1)
        space = ' ' * ((2*n - 1 - (2 * i + 1))//2)
        print(space + stars + space)
#print(christmas_tree(5))


def tower_of_hanoi(n: int, source: str, target: str, broker: str) -> None:
    if n == 1:
        print(f'disk 1 from {source} to {target}')
        return None
    tower_of_hanoi(n - 1, source, broker, target)
    print(f"disk {n} from {source} to {target}")
    tower_of_hanoi(n - 1, broker, target, source)
#print(tower_of_hanoi(3, 'a', 'c', 'b'))


def pascal(n: int) -> list[list[int]]:
    pascal = [[1]]
    for i in range(1 , n):
        row = [1]
        for j in range(1, i):
            row.append(pascal[i-1][j] + pascal[i-1][j-1])
        row.append(1)
        pascal.append(row)
    return(pascal)
#print(pascal(5))


def longest_increasing_subarrary(nums: list[int]) -> int:
    dp = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)
#print(longest_increasing_subarrary([10, 9, 2, 5, 3, 7, 101, 18]))  # Output: 4


#czyli jakby sprawdzam czy knkretne partie zaweiraja sie w zbiorze, dzielac to na fragmentu TRUE typowu przykład programowania dynamicznego
def word_break(s: str, word_dict: set) -> bool:
    dp = [False] * (len(s) + 1)
    dp[0] = True
    
    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_dict:
                dp[i] = True
                break
    return dp[-1]
#print(word_break("leetcode", {"code", "leet"}))

k = {"ku", "pa"}
kl = ['ku']
print('tak') if kl[0] in k else print("nie")



def revers_string(s: str) -> str:
    rs = s[::-1]
    return rs
#print(revers_string('take it easy'))

def is_palindrome(s: str) -> bool:
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]
#print(is_palindrome('A man, a plan, a canal: Panama'))

def finding_missing_num(nums: list[int]) -> int:
    correct_sum = (len(nums) + 1) * (len(nums) + 2) // 2
    actual_sum = sum(nums)
    return correct_sum - actual_sum
#print(finding_missing_num([1, 2, 4]))

def sum_of_two_elements_from_array(l: list[int], s: int) -> list[int]:
    d = {}
    for i, v in enumerate(l):
        complement = s - v
        if complement in d:
            return [d[complement], i]
        d[v] = i
    return []
#print(sum_of_two_elements_from_array([2, 7, 11, 15], 9))



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_lists(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode()
    current = dummy

    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    current.next = l1 or l2
    return dummy.next

# l1 = ListNode(1, ListNode(2, ListNode(4)))
# l2 = ListNode(1, ListNode(3, ListNode(4)))

# merged_list_values = []
# current = merge_two_lists(l1, l2)
# while current:
#     merged_list_values.append(current.val)
#     current = current.next
# print(merged_list_values)


def fizz_buzz(n: int) -> list[str]:
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append('FizzBuzz')
        elif i % 3 == 0:
            result.append('Fizz')
        elif i % 5 == 0:
            result.append('Buzz')
        else:
            result.append(str(i))
    return result

# print(fizz_buzz(15))


def find_duplicates(nums: int) -> list[int]:
    set1 = set()
    set2 = set()
    
    for num in nums:
        if num in set1:
            set2.add(num)
        else:
            set1.add(num)
    return list(set2)

# print(find_duplicates([4, 3, 2, 7, 8, 2, 3, 1]))


def is_anagram(s: str, t: str) -> bool:
    s = list(s)
    t = list(t)
    for n in s:
        if n in t:
            t.remove(n)
    if t == []:
        return True
    return False

# print(is_anagram("listen", "silent"))


def max_subarray_value(nums: list[int]) -> int:
    max_current = max_global = nums[0]
    
    for num in nums:
        max_current = max(num, max_current + num)
        max_global = max(max_current, max_global)
    return max_global

#print(max_subarray_value([-2, 1, -3, 8, -1, 2, 1, -5, 4]))

from collections import defaultdict
def group_anagrams(strs: list[str]) -> list[list[str]]:
    anagrams = defaultdict(list)
    
    for s in strs:
        key1 = (sorted(s))
        print(key1)
        key = ''.join(key1)
        anagrams[key].append(s)
    return list(anagrams.values())

print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

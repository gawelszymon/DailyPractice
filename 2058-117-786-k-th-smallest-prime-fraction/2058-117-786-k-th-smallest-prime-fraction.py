class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        low = 0
        high = 1
        while low < high:
            mid = (high - low) / 2 + low
            a = 0
            max_f = 0
            j = 1

            for i in range(len(arr) - 1):
                while j < len(arr) and arr[i] / arr[j] > mid:
                    j += 1

                a += len(arr) - j

                if j < len(arr) and arr[i]/arr[j] > max_f:
                    max_f = arr[i]/arr[j]
                    numerator = arr[i]
                    denominator = arr[j]
            if a == k:
                return [numerator, denominator]
            elif a > k:
                high = mid
            else:
                low = mid

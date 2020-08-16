# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:
#         length = len(digits)
#         if length == 0:
#             return digits
#         digits[-1] += 1
#         for i in range(length-1,-1,-1):
#             if digits[i] % 10 == 0:
#                 digits[i] = 0
#                 if i-1<0:
#                     digits.insert(0,1)
#                 else:
#                     digits[i-1] += 1
#             else:break
#         return digits
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        length = len(digits)
        if length == 0:
            return digits
        for i in range(length-1,-1,-1):
            digits[i]+=1
            digits[i] = digits[i] % 10
            if digits[i] != 0:
                return digits
        digits.insert(0,1)
        return digits
        

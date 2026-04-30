"""
เขียบนโปรแกรมแปลงตัวเลยเป็นตัวเลข roman

[Input]
number: list of numbers

[Output]
roman_text: roman number

[Example 1]
input = 101
output = CI

[Example 2]
input = -1
output = number can not less than 0
"""


class Solution:

    roman_map = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]

    def number_to_roman(self, number: int) -> str:
        if number < 0:
            return "number can not less than 0"
        if number == 0:
            return "nulla"

        result = ""
        for value, symbol in self.roman_map:
            count, number = divmod(number, value)
            result += symbol * count
        return result

# if __name__ == "__main__":
#     sol = Solution()
#     print(sol.number_to_roman(1001))     
#     print(sol.number_to_roman(-1))  
#     print(sol.number_to_roman(0))
#     print(sol.number_to_roman(653))
#     print(sol.number_to_roman(3999))

"""
เขียบนโปรแกรมแปลงตัวเลยเป็นคำอ่านภาษาไทย

[Input]
number: positive number rang from 0 to 10_000_000

[Output]
num_text: string of thai number call

[Example 1]
input = 101
output = หนึ่งร้อยเอ็ด

[Example 2]
input = -1
output = number can not less than 0
"""


class Solution:

    def number_to_thai(self, number: int) -> str:
        if number < 0:
            return "number can not less than 0"
        if number == 0:
            return "ศูนย์"

        result = ""
        units = ["", "สิบ", "ร้อย", "พัน", "หมื่น", "แสน", "ล้าน"]
        digits = ["", "หนึ่ง", "สอง", "สาม", "สี่", "ห้า", "หก", "เจ็ด", "แปด", "เก้า"]
        follow_digits = ["", "เอ็ด", "สอง", "สาม", "สี่", "ห้า", "หก", "เจ็ด", "แปด", "เก้า"]
        lead_digits = ["", "", "ยี่", "สาม", "สี่", "ห้า", "หก", "เจ็ด", "แปด", "เก้า"]

        divisor = 10000000
        while number > 0:
            count, number = divmod(number, divisor)
            #สิบล้าน
            if divisor == 10000000 and count > 0:
                result += lead_digits[count] + units[1]
                # ถ้าหลักล้านเป็น 0 ให้เติมคำว่า ล้าน
                if number // 1000000 == 0:
                    result += units[6]
            #หน่วยล้าน
            if divisor == 1000000 and count > 0:
                    if result not in [""] : # มีหลักสิบให้ใช้ เอ็ด
                        result += follow_digits[count] + units[6]
                    else:
                        result += digits[count] + units[6]
            #แสน
            if divisor == 100000 and count > 0:
                result += digits[count] + units[5]
            #หมื่น
            if divisor == 10000 and count > 0:
                result += digits[count] + units[4]
            #พัน
            if divisor == 1000 and count > 0:
                result += digits[count] + units[3]
            #ร้อย
            if divisor == 100 and count > 0:
                result += digits[count] + units[2]
            #สิบ
            if divisor == 10 and count > 0:
                result += lead_digits[count] + units[1]
            #หน่วย
            if divisor == 1 and count > 0:
                result += follow_digits[count]
            divisor //= 10
            
        return result

# if __name__ == "__main__":
#     sol = Solution()
#     print(sol.number_to_thai(0))     
#     print(sol.number_to_thai(-1))
#     print(sol.number_to_thai(10000000))  
#     print(sol.number_to_thai(11000000))
#     print(sol.number_to_thai(11111111))
#     print(sol.number_to_thai(22222222))
#     print(sol.number_to_thai(20202020))
#     print(sol.number_to_thai(55555555))


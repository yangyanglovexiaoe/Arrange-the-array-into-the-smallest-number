# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        #边界判断
        if len(numbers) <=1:
            numbers = [str(i) for i in numbers]
            return ''.join(numbers)
        #大小比较定义
        str_numbers = [str(i) for i in numbers]
        for i in range(len(numbers)):
            for j in range(i+1, len(numbers)):
                if int(str_numbers[i]+str_numbers[j]) > int(str_numbers[j]+str_numbers[i]):
                    str_numbers[i],str_numbers[j] = str_numbers[j],str_numbers[i]
                    
        #输出拼接的最小数字
        str_final = ''
        for m in range(len(str_numbers)):
            str_final += str_numbers[m]
        return str_final

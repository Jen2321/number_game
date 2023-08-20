# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 21:47:09 2023

@author: USER
"""
# 導入隨機模組
import random


# 產生一個隨機的四位數字
def generate_num():   
    return ''.join(random.sample('0123456789', 4))
    

# 比較猜測數字和隨機數字
def compare_numbers(random_num, guess_num):
    
    A = 0
    B = 0

    for i in range(4):
        if guess_num[i] == random_num[i]:  
            A += 1
        elif guess_num[i] in random_num:    
            B += 1

    return A, B

# 主程式
def main():
    random_num = generate_num()
    # 紀錄猜測的次數
    attempt = 0

    print("歡迎來到猜數字遊戲！")
    print("猜一個四位數字，數字不能重複")

    while True:
        guess_num = input("請輸入你猜測的數字：")

        # 檢查輸入是否符合條件(四位數，且不能重複或為數字以外的文字)
        if len(guess_num) != 4 or len(set(guess_num)) != 4 or not guess_num.isdigit():
            print("請輸入正確的四位數字！")
            continue

        attempt += 1
        A, B = compare_numbers(random_num, guess_num)

        # 判斷是否猜中
        if A == 4:
            print(f"猜中了！正確答案是 {random_num}，你總共猜了 {attempt} 次。")
            break
        else:
            print(f"{A}A{B}B")

# 執行主程式
if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 14:35:27 2016

@author: Hoang.To
"""

class VendingMachine:
    def __init__(self, drinkInfo):
        self.drinkInfo=drinkInfo
    
    def getDrink(self, coin, button):
        for i in self.drinkInfo:
            if i["drink_name"]==button:
                charge=coin-i["price"]
                if charge <0:
                    print("Không đủ tiền rồi, đưa thêm đi")
                else:
                    print("Đồ uống của bạn đây, bạn còn dư: ",str(charge))
                    
        

drinkInfo=[
{"drink_name":"Coke","price":7},
{"drink_name":"Energy","price":10},
{"drink_name":"Water","price":5}
]


machine1=VendingMachine(drinkInfo)



coin=int(input("Nhập số tiền: "))
button=input("Nhập đồ uống bạn muốn mua: ")


machine1.getDrink(coin,button)

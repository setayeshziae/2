secend_time = 0
h = int(input(" please enter hour:"))
m =int(input("please enter minute:"))
s =int(input("please enter second:"))

secend_time = h * 3600
secend_time = (m * 60) + secend_time
secend_time = s + secend_time

print(secend_time)
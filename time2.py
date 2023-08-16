input = int(input(" enter youre time in second:"))
h = input // 3600
m = (input - h * 3600) // 60 
s = (input - ( h * 3600 )- (m * 60))

print(  h, ":", m, ":", s)
print("hour", ":", h, "minute ", ":", m,"second", ":", s)

# 1 Countdown

# def countdown(num):
#     newList = []
#     while num >= 0:
#         newList.append(num)
#         num -= 1
#     return newList

# x = countdown(5)
# print(x)

#---------------------------------------------------------------
# 2 Print and Return

# def printAndReturn(list_1):
#     print(list_1[0])
#     return list_1[1]

# x = printAndReturn([1,2])
# print(x)


#---------------------------------------------------------------
# 3 First Plus Length

# def FirstPlusLength(list_2):
#     add = list_2[0] + len(list_2)
#     return add

# x = FirstPlusLength([1,2,3,4,5])
# print(x)


#---------------------------------------------------------------
# 4 Values Greater than Second

# def ValuesGreaterThanSecond(list_3):
#     newList = []
#     numberElements = 0
#     if len(list_3) < 2:
#         return False
#     else:
#         for i in list_3:
#             if i > list_3[1]:
#                 newList.append(i)
#                 numberElements += 1   
#     print(numberElements)
#     return newList

# x = ValuesGreaterThanSecond([1,2,5,-1,6,20])
# y = ValuesGreaterThanSecond([2])
# print(x)
# print(y)


#---------------------------------------------------------------
# 5 This Length that Value

def ThisLengthThatValue(size, value):
    newLlist = []
    for i in range(size):
        newLlist.append(value)
    return newLlist

x = ThisLengthThatValue(5, 3)
print(x)
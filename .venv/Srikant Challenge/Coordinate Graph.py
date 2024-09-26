# [(x1,y1), (x2,y2), (x3,y3), (x4,y4)..]
# points = eval(input())
# mypos = (0,0)
# for p in points:
#     y = p[1] - p[0]
#     if y>=0:
#         print('Yes')
#         break
#     else:
#         continue
# x, y = list(map(int,input()))
# mypos =[x, y]
# for p in points:
#     mypos[0] = p[0]
#     mypose[1] = p[0/]
#     p[1] = p[1]-abs(mypos(0))
#     if p[1]<mypos[1]:
#         continue
#     else:
#         print('Yes')
#         break

# # Clear Method
# points = eval(input()) #lol
# mc = [0,0]
# for p in points:
#     mc[0] = p[0]
#     mc[1] = -abs(mc[0])
#     if p[1] >= mc[1]:
#         print("Yes")
#         break
#     else:
#         continue

# # Shortest Method
# points = eval(input()) #lol
# for p in points:
#     if p[1] >= -abs(p[0]):
#         print("Yes")
#         break
# else:
#     print("No")

# Even More!!
# Move in that direction where the coin is moving, that is down!
# After reaching the same x as coin, we need to see if it's y is above, equal to us or less than us
# If coin is above us, we can simply move up and coin will move down and we will meet no pressure,if its below we will keep cathing it forever
# it can be caught as x can be achieved after x moves, as x is constant for the coin we can someday reach it, so we are actually dependent on y.
# Since we move first, then coin moves, and coin only moves down, if coin is at our level or just one below our level we can catch it else not
points = eval(input()) #lol
for p in points:
    if p[1]>=-1:
        print("Yes")
        break
else:
    print("No")
# OR
# points = eval(input()) #List of lists having coordinates x and y
# print("Yes" if "Yes" in ["Yes" for point in points if point[1]>=-1] else "No") #Compressed code




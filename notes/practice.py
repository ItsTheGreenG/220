import graphics
import math
#my_point = graphics.Point(50, 70)
#point_a = graphics.Point(70, 90)
#print(point_a.getX())

#win = graphics.GraphWin("CSCI 220", 700, 700)
#middle = graphics.Point(350, 350)
#middle.draw(win)

#my_circle = Circle(middle, 40)

#my_circle.draw(win)
#input('Hit enter to close'

#def sum_diff(x,y):
    #sum_value = x + y
    #diff_value = x-y
    #return sum_value(), diff_value()


#my_sum, my_diff = sum_diff(10,7)
#print(my_sum,my_diff)
#sum_diff()


'''def get_discount(price, sale):
   price = price * (1-sale)
   return price

price = 100
price = get_discount(price, .20)
print(price)'''

def change_point(p, x, y):
   p.move(x,y)

p1 = Point(2,3)
print(p1)
change_point(p1, 100, 200)
print(p1)
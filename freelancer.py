import matplotlib.pyplot as plt



class Snow_person(object):
    def __init__(self,x,y,radius,color,):
        self.x=x
        self.y=y
        self.radius=radius
        self.color=color
        
    def draw(self):
        circ=Circle(self.x,self.y,self.color).draw(self.radius)
        return circ
    def draw_rect(self,width,length):
        rectangle = Rectangle(self.x,self.y,self.color).draw(width,length)
"""  
class Snow_man(Snow_person):
    def __init__(self,):
        a="a"
        
        

class Snow_lady(object):
    def __init__(self,):
        

class Line(object):
    # DOCSTRING NEEDED
    def __init__(self,x,y,color): #x and y forpisiton, "color" is for color of the shape
        
    def __str__(self):
        return self.__name__

    def draw(self):
"""       
class Rectangle(object):
    # DOCSTRING NEEDED
    def __init__(self,x,y,color):
        self.x=x
        self.y=y
        self.color=color
    def __str__(self):
        return self.__name__

    def draw(self,width,length):
        rectangle = plt.Rectangle((self.x,self.y), width, length, fc=self.color)
        plt.gca().add_patch(rectangle)
        plt.axis('scaled')
        

class Circle(object):
    # DOCSTRING NEEDED
    def __init__(self,x,y,color):
        self.x=x
        self.y=y
        self.color=color
        
    def __str__(self):
        return self.__name__
        
    def draw(self,radius):
        
        circle = plt.Circle((self.x,self.y), radius, fc=self.color,fill=False)
        plt.gca().add_patch(circle)

        plt.axis('scaled')
        
"""
class Triangle(object):
    # DOCSTRING NEEDED
    def __init__(self,x,y,color):

    def __str__(self):
        return self.__name__

    def draw(self):

"""
def main():
    #DOSTRING
    '''d=Snow_person(4,4,1.5,'r'  ,4,6.6,1.1,'r'   ,4,8.3,0.6,'r',\
                  10,4,1.5,'r'  ,10,6.6,1.1,'r'   ,10,8.3,0.6,'r')

'''
    man_1stball=Snow_person(4,4,1.5,'r')
    man1=man_1stball.draw()

    man_2ndball=Snow_person(4,6.6,1.1,'r')
    man2=man_2ndball.draw()

    man_3rdball=Snow_person(4,8.3,0.6,'r')
    man3=man_3rdball.draw()

    woman_1stball=Snow_person(10,4,1.5,'r')
    woman1=woman_1stball.draw()

    woman_2ndball=Snow_person(10,6.6,1.1,'r')
    woman2=woman_2ndball.draw()

    woman_3rdball=Snow_person(10,8.3,0.6,'r')
    woman3=woman_3rdball.draw()

    


    b1=Snow_person(10,3.1,0.2,'r')
    button1_men_1=b1.draw()

    b2=Snow_person(10,4.5,0.2,'r')
    button2_men_1=b2.draw()
    
    b3=Snow_person(10,6,0.17,'r')
    button1_men_2=b3.draw()
    
    b4=Snow_person(10,7,0.17,'r')
    button2_men_2=b4.draw()



    b11=Snow_person(4,3.1,0.2,'r')
    button11_men_1=b11.draw()

    b22=Snow_person(4,4.5,0.2,'r')
    button22_men_1=b22.draw()
    
    b33=Snow_person(4,6,0.17,'r')
    button11_men_2=b33.draw()
    
    b44=Snow_person(4,7,0.17,'r')
    button22_men_2=b44.draw()


    hat_m1=Snow_person(3.5, 8.70,1, 'r')
    hat_m=hat_m1.draw_rect(1,1.35)
    #hat_w1=

    plt.plot(man1,man2,man3,woman1,woman2,woman3)
    plt.plot(button1_men_1,button2_men_1)
    plt.plot(button1_men_2,button2_men_2)

    plt.plot(button11_men_1,button22_men_1)
    plt.plot(button11_men_2,button22_men_2)

    plt.plot(hat_m)
    plt.show()
main()
    

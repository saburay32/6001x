from math import tan, pi                  #importing the necessary functions from the library math

def polysum(n,s):
    '''
    function polysum that takes 2 arguments,
    number of sides polygon:  param n:
    polygon has side length:  param s:
    Function should sum the area and square of the perimeter of the regular polygon.
    The function returns the sum, rounded to 4 decimal places :  return:
    '''

    perimetr = (n*s)**2                   #calculate the perimeter,I square it
    area = ((0.25*n*(s**2))/(tan(pi/n)))  #calculate the perimeter of a polygon
    sum = round((perimetr+area),4)        #sum of the perimeter squared and the area rounded to 4 decimal places
    return sum                            #return answer

                                          # body function in one line:
                                          # return (round(((n*s)**2)+((0.25*n*(s**2))/(tan(pi/n))),4))

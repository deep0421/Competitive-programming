import unittest


def highest_product_of_3(list_of_ints):

    list_of_ints.sort()
    a=list_of_ints
    postive3=a[len(a)-1]*a[len(a)-2]*a[len(a)-3]
    if(a[0]>=0 or a[0]<0 and a[1]>=0):
        z= postive3
    else:
        if(a[0]<0 and a[1]<0):
            negative2_positive1=a[0]*a[1]*a[len(a)-1]
        if(negative2_positive1<postive3):
            z=postive3
        else:z=negative2_positive1

    return z


      
TESTCASES

print(highest_product_of_3([1, 2, 3, 4]))              expected = 24
print(highest_product_of_3([6, 1, 3, 5, 7, 8, 2]))     expected = 336
print(highest_product_of_3([-5, 4, 8, 2, 3]))          expected = 96
print(highest_product_of_3([-10, 1, 3, 2, -10]))       expected = 300
print(highest_product_of_3([-5, -1, -3, -2]))          expected = -6

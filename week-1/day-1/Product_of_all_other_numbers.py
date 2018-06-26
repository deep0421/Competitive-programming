def get_products_of_all_ints_except_at_index(int_list):

   # Make a list with the products
   res = []
   temp = 1
   product = 1
   for i in range(len(int_list)):
       res.append(product)
       product *= int_list[i]
   print(res)
   product = 1
   for i in range(len(int_list)-1,-1,-1):
   	temp = product
   	product *= int_list[i]
   	res[i] *= temp
   print(res)
       

   return res



TESTCASES

print(get_products_of_all_ints_except_at_index([1, 2, 3]))                 expected = [6, 3, 2]
print(get_products_of_all_ints_except_at_index([8, 2, 4, 3, 1, 5]))        expected = [120, 480, 240, 320, 960, 192]
print(get_products_of_all_ints_except_at_index([6, 2, 0, 3]))              expected = [0, 0, 36, 0]
print(get_products_of_all_ints_except_at_index([4, 0, 9, 1, 0]))           expected = [0, 0, 0, 0, 0]
print(get_products_of_all_ints_except_at_index([-3, 8, 4]))                expected = [32, -12, -24]

def highest_product_of_3(list_of_ints):

   
   length = len(list_of_ints)
   if length<3:
       raise Exception("yo")
   sorted_list = sorted(list_of_ints)
   a = sorted_list[length -1] * sorted_list[length -2] * sorted_list[length -3]
   b = sorted_list[length -1] * sorted_list[0] * sorted_list[1]

   if a > b:
   	return a
   else:
   	return b

      
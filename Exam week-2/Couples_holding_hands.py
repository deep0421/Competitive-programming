def minSwapsCouples(row):
        n = len(row)
        for i in range(n):
            row[i] = row[i] // 2
        count = 0
        for i in range(0, n - 1, 2):
            if row[i] != row[i + 1]:
                j = row.index(row[i], i + 1)
                row[i + 1], row[j] = row[j], row[i + 1]
                count += 1
        print(count)
minSwapsCouples([1,3,4,0,2,5]) 
minSwapsCouples([3,2,0,1]) 
minSwapsCouples([3,30,50,90,16,91,65,18,61,58]) 
minSwapsCouples([55,37,19,46,66,32,07,81,33,76,00,28,92,26,99,06,56,29,17,52,90,79,91,83,12,4
0,82,84,02,21,11,68,98,34,73,10,57,58,64,36]) 
minSwapsCouples([1,0]) 
minSwapsCouples([50,23,76,19,16,70,35,68,41,49,99,71,59,95,89,33,22,07,54,83,24,0,
18,64,11,14,77,26,42,21,82,1,97,52,65,79,37,62,60,91,98,4,88,36,51,20,85,90,2
9,84,93,13,80,6,55,48,2,40,46,81,30,3,94,38,27,31,53,86,32,96,8,58,73,5] ) 

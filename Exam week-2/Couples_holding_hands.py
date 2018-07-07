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
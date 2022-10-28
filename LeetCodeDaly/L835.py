def largest_overlap(img1,img2):
    n = len(img1)
    a,b = 0,0
    for a in range(n):
        for b in range(n):
            count = 0
            for i in range(n):
                for j in range(n):
                    if i+a < n and j+b < n:
                        if img1[i][j] == img2[i+a][j+b] == 1:
                            count += 1
            print(count)

img1 = [[1,1,0],
        [0,1,0],
        [0,1,0]]

img2 = [[0,0,0],
        [0,1,1],
        [0,0,1]]
print(largest_overlap(img1,img2))
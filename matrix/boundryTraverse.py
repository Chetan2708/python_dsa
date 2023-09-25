def traverse(arr):

    N = len(arr);
    M = len(arr[0]);
    for i in range(M):
        print(arr[0][i], end = " ");

    for i in range(1, N):
        print(arr[i][M - 1], end = " ");
 

    if (N > 1):
 
        for i in range(M - 2, -1, -1):
            print(arr[N - 1][i], end = " ");
 

    if (M > 1):
 
      
        for i in range(N - 2, 0, -1):
            print(arr[i][0], end = " ");
    

matrix = [[1,2,3,4],
          [5,6,7,8],
          [9,10,11,12],
          [13,14,15,16]]

traverse(matrix)

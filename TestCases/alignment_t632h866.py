import sys

def opt(Matrix,Matrix2,S,T): #find the min score and tie breaker for method
    for i in range(1,len(Matrix)):
        for j in range(1,len(Matrix[i])):
            top = 1 + Matrix[i-1][j]#top
            left = 1 + Matrix[i][j-1]#left
            diagonal =  Matrix[i-1][j-1] if S[i-1]==T[j-1] else Matrix[i-1][j-1]+1#diagonal
            data = {'d':diagonal, 'l':left, 't':top}
            cur_min = data["d"]
            cur_min2 = next(iter(data))
            for key, value in data.items():
                if value < cur_min:
                    if(data["l"]!=data["t"]):
                        cur_min = value
                        cur_min2 = key
                    elif(data["l"]==data["t"]):
                        cur_min = data["l"]
                        cur_min2 = 'l'
            Matrix[i][j] = cur_min
            Matrix2[i][j] = cur_min2

def output(Matrix,Matrix2,S,T):#print the output
    array = []
    array2 = []
    a = len(S)
    b = len(T)
    x = len(S)
    y = len(T)
    count = 0
    while(isinstance(Matrix2[a][b],int)==False):
        if Matrix2[a][b] == 'd':
            array.insert(0,S[x-1])
            array2.insert(0,T[y-1])
            a -= 1
            b -= 1
            x -= 1
            y -= 1
        elif Matrix2[a][b] == 'l':
            array.insert(0,'-')
            array2.insert(0,T[y-1])
            b -=1
            y -=1
        elif Matrix2[a][b] == 't':
            array.insert(0,S[x-1])
            array2.insert(0,'-')
            a-=1
            x-=1
    if(x!=0):
        while x!=0:
            array.insert(0,S[x-1])
            array2.insert(0,'-')
            a-=1
            x-=1
    if(y!=0):
        while y!=0:
            array.insert(0,'-')
            array2.insert(0,T[y-1])
            b -=1
            y-=1
        
    array = ''.join(array)
    array2 = ''.join(array2)
    for i in range(len(array)):
        if array[i]!=array2[i]:
            count+=1
    print(count)
    print(array)
    print(array2)

my_file = open( sys.argv[ 1 ], 'r' )
S = my_file.readline() #read first string
S = S.strip("\n")
T = my_file.readline() #read second string
T = T.strip("\n")
Matrix = [[0] * (len(T)+1) for i in range(len(S)+1)] #matrix to record number
Matrix2 = [[0] * (len(T)+1) for i in range(len(S)+1)] #matrix to record method


for i in range(len(Matrix)):
    for j in range(len(Matrix[i])):
        Matrix[0][j] = j
        Matrix[i][0] = i
        Matrix2[0][j] = j
        Matrix2[i][0] = i
opt(Matrix,Matrix2,S,T)
output(Matrix,Matrix2,S,T)
1. Important conecepts and syntaxes to learn

    -Learn how to use name,*line
    -learn how to use score=list(map(float,line)
    -Never use loops to manip number,just use inbuilt


2. Calculate diagnals of matrix
       -2 loops for i & j termintate with n 
       -if (i == J):
            principal diagnol
        -if (i = n-j-1):
            reverse diagnol
            
3. Right half stairs
    - for i in range(0, n):
        print(' ' * (n  - i) + '#' * i)
            
            
       
4. When you have to print 4/5 on min and max,sort and print sum 🤯
    - arr = sorted(arr)
    print(sum(arr[:-1]),sum(arr[1:]))


5. Split number into digits
    
    -my_int = 13579

    my_list = [int(x) for x in str(my_int)]

    print(my_list)  # 👉️ [1, 3, 5, 7, 9]
    
    
6. Reverse int
    -rev=(str(x)[::-1]) 

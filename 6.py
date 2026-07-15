from datetime import datetime
n = 100


"""
    Base
"""
start = datetime.now()

sum_of_square = 0
square_of_sum = 0
for i in range(n+1):
    sum_of_square += i**2
    square_of_sum += i

end = datetime.now()

print(square_of_sum**2 - sum_of_square, "Time: {}".format((end-start).total_seconds() * 1000))



"""
    Optimization: 
    - 1 + 2+ .. n = (n+1)*n//2
    - Assume 1**2 + 2**2 + ... + n**2 = a*n**3 + b*n**2 + c*n + d
    - With n from 1 to 4:
        a + b + c + d = 1
        8a + 4b + 2c + d = 5
        27a + 9b + 3c + d = 14
        64a + 16b + 4c + d = 30

        => a = 1/3
           b = 1/2
           c = 1/6
           d = 0

    - Prove:
        Assume formula above true with n, need to prove true with (n+1):
        1 + 4 + ... + (n+1)**2                = 1/3(n+1)**3 + 1/2(n+1)**2 + 1/6(n+1)
        1/3n**3 + 1/2n**2 + 1/6n + (n+1)**2   = 1/3(n+1)**3 + 1/2(n+1)**2 + 1/6(n+1)
                                              = 1/3n**3 + n**2 + n + 1/3 + 1/2*n**2 + n + 1/2 + 1/6*n + 1/6 
                                              = 1/3n**3 + 1/2n**2 + 1/2n + (n**2 + n + 1/3 + n + 1/6)
                                              = 1/3n**3 + 1/2n**2 + 1/2n + (n**2 + 2n + 1)
                                              = 1/3n**3 + 1/2n**2 + 1/2n + (n+1)**2

"""
start = datetime.now()

ans = (n*(n+1)//2)**2 - (1/6 * n**3 + 1/2*n**2 + 1/6*n)  
end = datetime.now()

print(square_of_sum**2 - sum_of_square, "Time: {}".format((end-start).total_seconds()* 1000))

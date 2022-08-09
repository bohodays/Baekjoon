# 1945 간단한 소인수분해
# 2020-08-09


T = int(input())

for tc in range(1, T+1):

    N = int(input())

    a = b = c = d = e = 0

    while N % 2 == 0:
        N //= 2
        a += 1
        continue


    while N % 3 == 0:
        N //= 3
        b += 1
        continue


    while N % 5 == 0:
        N //= 5
        c += 1
        continue


    while N % 7 == 0:
        N //= 7
        d += 1
        continue


    while N % 11 == 0:
        N //= 11
        e += 1
        continue
    
    print('#{} {} {} {} {} {}'.format(tc, a, b, c, d, e))
def maior_primo(k):
    i = 2
    j = 4
    l = 6
    while i < k:
        if k % i == 0  or  k % j == 0  or  k % l == 0:
            k = k - 1
            éPrimo(k)
        else:
            i = i+1
            if i == k:
                k = k - 1
                éPrimo(k)
            else:
                é_primo = True
                return k

def éPrimo(n):
    i = 2
    j = 4
    l = 6
    while i < n:
        if n % i != 0  or  n % j != 0  or  n % l != 0:
            return n
        else:
            i = i+1
            if i != n:
                return n

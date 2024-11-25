def numeros_primos(n):
    primos = []
    
    def eh_primo(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    for i in range(2, n + 1):
        if eh_primo(i):
            primos.append(i)
    
    return primos

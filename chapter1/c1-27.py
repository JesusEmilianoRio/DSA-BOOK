def factors(n):
    k = 1
    small_factors = []
    
    # Recolectar factores hasta la raíz cuadrada
    while k * k <= n:
        if n % k == 0:
            small_factors.append(k)
        k += 1
    
    # Yield todos los factores en orden
    yield from small_factors
    yield from (n // factor for factor in reversed(small_factors) 
                if n // factor != factor)
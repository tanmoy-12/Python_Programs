def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_sums(limit):
    """Print prime numbers that can be expressed as the sum of other prime numbers."""
    primes = [i for i in range(2, limit) if is_prime(i)]  # Generate all primes below the limit
    result = []
    
    for prime in primes:
        total = 0
        for p in primes:
            total += p
            if total == prime:  # Match found
                result.append(prime)
                break
            if total > prime:  # Exceeded the number
                break
    
    print(f"Prime numbers expressed as the sum of other primes up to {limit}: {result}")

# Example usage
prime_sums(50)

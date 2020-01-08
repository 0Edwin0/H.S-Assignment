# Python 3.7

#  Finding N-th Prime no.

def is_prime(number):
    '''
    Returns boolen value whether the 
    number is prime or not.
    '''
    for d in range(2, number):
        if number % d == 0:
            return False
    return True

def nth_prime(nth):
    '''
    Return the N-th prime number.
    '''

    if nth >= 1 and type(nth)==int:
        num = 2
        count = 0

        while True:
            if is_prime(num):
                count += 1
            if count == nth:
                return num
            else:
                num += 1
        
    else:
        raise ValueError('nth int() should be greater than or equal to 1.')
    return
    
if __name__ == "__main__":
    print('Finding N-th Prime no.\n')
    try:
        nthPrimePos = int(input("Enter a number for n-th prime no.: "))
        prime_no = nth_prime(nthPrimePos)
        print('[{}] Prime No.: {}'.format(nthPrimePos,prime_no))
    except Exception as e :
        print('Error occured : {}'.format(e))
    input('Enter any key')


# Python 3.7

# Finding sum of the squares of all
# natural numbers from 1 to N.

# def sum_naturalSquareNo(limit):
#     '''
#     returns sum of square of n natural numbers.

#     (using loop)
#     '''

#     if limit >= 1:
#         sum = 0
#         for n in range(1, limit+1):
#             sum += n**2
#         return sum
#     else:
#         raise ValueError('limit should be greater than or equal to 1.')
#     return

def sum_naturalSquareNo1(limit):
    '''
    returns sum of square of n natural numbers.

    (using formula sn=(n(n+1)(2n+1))/6 )
    '''
    if limit >= 1:
        s = int((limit*(limit+1)*((limit*2)+1))/6)
        return s
    else:
        raise ValueError('limit should be greater than or equal to 1.')
    return

if __name__ == "__main__":
    try:
        limit_no = int(input("Enter limit: "))
        sum_square = sum_naturalSquareNo1(limit_no)
        print(sum_square)
    except Exception as e:
        print('Error occured : {}'.format(e))
    input('Enter any key')

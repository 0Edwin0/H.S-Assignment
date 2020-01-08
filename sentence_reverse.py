# Python 3.7

# Reverse the whole string without reversing
# the individual words in it.

def strReverse(string, sep='.'):
    '''
    Return reversed string without reversing 
    individual words in it.

    string : (str) value for reversing.

    sep : (str) The delimiter according which to
    split the string into words. `.` (the default value) 
    means split according to any dot.

    '''
    
    list_str = string.split(sep)
    rev_list = list_str[::-1]
    if sep:
        v = sep
    else:
        v = ' '
    new_string = v.join(rev_list)
    return new_string

if __name__ == '__main__':
    print("Reverse the whole string without reversing the individual words in it.\n")
    try:
        string = input('Enter String : ')
        new_str = strReverse(string)
        print('Reversed String:', new_str)
    except Exception as e :
        print('Error occured : {}'.format(e))
    input('Enter any key')

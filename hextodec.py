# hexadecimal to decimal

hexa = input('Enter a hexadecimal that you would like to convert to decimal form: ')
def hextodec (hexadecimal):
    decimal = int(hexadecimal, 16)
    return decimal
print(hexa, "converted into decimal form is",hextodec(hexa))


# another way to solve it using .strip and .ord

def main():
    # ask for user input
    hex =  input('Enter a hex number: ').strip()
    # convert lowercase to uppercase
    decimal = hex_to_dec(hex.upper()) # optional
    if decimal == None:
        print('Incorrect hex number has been provided')
    else:
        print('The decimal value for hex provided is:', decimal)

def hex_to_dec(hex):
    decimal_value = 0 # initialization
    for i in range(len(hex)):
        ch = hex[i]
        if ('A' <= ch <= 'F' or '0' <= ch <= '9'):
            decimal_value = decimal_value * 16 + hex_char_to_decimal(ch)
        else:
            return('Sorry, cannot convert this input.')
    return(decimal_value)
def hex_char_to_decimal(ch):
    if ('A' <= ch <= 'F'):
        return(10 + ord(ch) - ord('A'))
    else:
        return(ord(ch) - ord('0'))

main()
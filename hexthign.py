digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'.upper()
asknumstring = input("Welcome to whatever this is maybe its a calculator idk \n Please enter the number you would like to convert: ").upper()
askoriginalbase = int(input("Please enter the numbers current base (2-36): "))
if askoriginalbase < 2 or askoriginalbase > 36:
    print("Error: gotta be between 2 and 36.")
    exit()
    
asktargetbase = int(input("Please enter the numbers target base (2-36): "))
if asktargetbase < 2 or asktargetbase > 36:
    print("oops you gotta have it be between 2 and 36.")
    exit()

def to_decimal(number_string, original_base):
    total_value = 0
    power = 0
    for char in number_string[::-1]:
        digits.index(char)
        total_value += digits.index(char) * (original_base ** power)
        power += 1
    return total_value
def from_decimal(decimal_number, target_base):
    result_string = ''
    while decimal_number > 0:
        remainder = decimal_number % target_base
        decimal_number //= target_base
        char_to_add = digits[remainder]
        result_string = char_to_add + result_string
    return result_string
decimal_value = to_decimal(asknumstring, askoriginalbase)
converted_value = from_decimal(decimal_value, asktargetbase)
print(f"The number \"{asknumstring}\" is \"{converted_value}\" in base-{asktargetbase}.")



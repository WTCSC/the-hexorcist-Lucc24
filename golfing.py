digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'.upper()
def to_decimal(number_string, original_base):
    total_value = 0
    for power, char in enumerate(number_string[::-1]):
        total_value += digits.index(char) * (original_base ** power)
    return total_value
def from_decimal(decimal_number, target_base):
    if decimal_number == 0:
        return '0'
    result_string = ''
    while decimal_number > 0:
        result_string = digits[decimal_number % target_base] + result_string
        decimal_number //= target_base
    return result_string
if __name__ == "__main__":
    asknumstring = input("Welcome to whatever this is maybe its a calculator idk \n Please enter the number you would like to convert: ").upper()
    askoriginalbase = int(input("Please enter the numbers current base (2-36): "))
    asktargetbase = int(input("Please enter the numbers target base (2-36): "))
    converted_value = from_decimal(to_decimal(asknumstring, askoriginalbase), asktargetbase)
    print(f"The number \"{asknumstring}\" is \"{converted_value}\" in base-{asktargetbase}.")



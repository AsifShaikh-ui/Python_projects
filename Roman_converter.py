roman_map = {
    'I' : 1,
    'V' : 5,
    'X' : 10,
    'L' : 50,
    'C' : 100,
    'D' : 500,
    'M' : 1000
}

value_map = [(1000,'M'),(900,'CM'),(500,'D'),(400,'CD'),(100,'C'),(90,'XC'),(50,'L'),(40,'XL'),(10,'X'),(9,'IX'),(5,'V'),(4,'IV'),(1,'I')]

def roman_to_dec(roman):

    roman = roman.upper()
    total = 0

    for i in range(len(roman)):
        if roman[i] not in roman_map:
            return None
        
        value = roman_map[roman[i]]

        if i+1 < len(roman) and value < roman_map.get(roman[i+1]):
            total -= value
        else:
            total += value
    
    return total

def dec_to_roman(number):
    if number <= 0 or number > 3000:
        return None
    
    result = ""

    for value , symbol in value_map:
        while number >= value:
            result += symbol
            number -= value
    
    return result
            
def main():
    print("\n-------Roman Converter-----")
    print("1. Roman to Decimal")
    print("2. Decimal to Roman")

    choice = input("Choose what to you want to convert (1/2): ")

    if choice == "1":
        user = input("Enter the roman number: ")
        answer = roman_to_dec(user)
        print(f"Decimal Value : {answer}")
    
    elif choice == "2":
        user = int(input("Enter Decimal number (1-3000): "))
        answer = dec_to_roman(user)
        print(f"Roman numeral: {answer}")
    
    else:
        print("❌Invalid Choice")


main()
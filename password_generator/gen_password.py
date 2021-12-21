import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def get_password(let_count,sym_count,num_count):
    '''
    To generate a random password with the specified count of:
    1. letters
    2. symbols
    3. numbers
    '''
    password_list = random.choices(letters, k=let_count)
    password_list.extend(random.choices(symbols, k=sym_count))
    password_list.extend(random.choices(numbers, k=num_count))
    random.shuffle(password_list)
    return "".join(password_list)


if __name__ == "__main__":
    print("Welcome to the PyPassword Generator!")
    nr_letters = int(input("How many letters would you like in your password?\n"))
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))
    print(get_password(let_count=nr_numbers,sym_count=nr_symbols,nr_num=nr_numbers))
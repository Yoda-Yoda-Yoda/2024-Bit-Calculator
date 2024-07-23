# Generates headings (eg: ---- Heading ----)
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


# Displays instructions
def instructions():
    statement_generator("Instructions", "-")

    print('''
Instructions go here
- instruction 1
- instruction 2
- etc
    ''')


# asks the users for file type (integer / text / xxx)
def get_filetype():

    while True:
        response = input("File type: ").lower()

        # check for 'i' or the exit code
        if response == "xxx" or response == "i":
            return response

        # check if it's a integer
        elif response in ['integer', 'int']:
            return "integer"

        # check for an image...
        elif response in ['image', 'picture', 'img', 'p']:
            return "image"

        # check for text
        elif response in ["text", 'txt', 't']:
            return "text"

        # if the response is invalid output an error
        else:
            print("Please enter a valid file type")


# Ask user for width and loop until they
# Enter a nuber that is more than zero
def int_check(question, low):

    error = "Please enter number that is more than zero\n"

    while True:
        try:
            # ask the user for a number
            response = int(input(question))

            # check that the number is more than zero
            if response >= low:
                return response

            else:
                print(error)
        except ValueError:
            print(error)


# calculates how many bits are needed to represent and integer
def image_calc():
    # Get the image dimensions
    width = int_check("Width: ", 1)
    height = int_check("Height: ", 1)

    # calculate the number of pixels and multiply by 24 to get the number of bits
    num_pixels = width * height
    num_bits = num_pixels * 24

    # Set up answer and return it
    answer = f"Number of pixels:  {width} x {height} = {num_pixels} " \
             f"\nNumber of bits: {num_pixels} x 24 = {num_bits}"

    return answer


# calculates how many bits are needed to represent and integer
def integer_calc():
    # Ask the user to enter an integer (more than / equal to 0)
    integer = int_check("Integer:  ", 0)

    # convert the integer to binary and work out the number of bits needed
    raw_binary = bin(integer)

    # remove the leading '0b' from the raw binary conversion
    binary = raw_binary[2:]
    num_bits = len(binary)

    # Set up answer and return it
    answer = f"{integer} in binary is {binary}.  We need {num_bits} to represent it"

    return answer


# Calculates number of bits needed to represent text in ascii
def calc_text_bits():

    # Get text from user
    response = input("Enter some text: ")

    # Calculate bits needed
    num_chars = len(response)
    num_bits = num_chars * 8

    # Set up answer and return it
    answer = (f"{response} has {num_chars} characters.   " 
              f"\nWe need {num_chars} x 8 bits to represent it "
              f"\nwhich is {num_bits} bits")

    return answer


# Main routine goes here

# Display instructions if requested
want_instructions = input("Press <enter> to read the instructions "
                          "or any key to continue")
if want_instructions == "":
    instructions()


while True:
    file_type = get_filetype()

    if file_type == "xxx":
        break

    # if user chose 'i' ask if they want an image / integer

    if file_type == 'i':
        want_image = input("Press <enter> for and integer or any key for and image.  ")
        if want_image == "":
            file_type = "integer"
        else:
            file_type = "image"

    if file_type == "image":
        image_ans = image_calc()
        print(image_ans)
    elif file_type == "integer":
        image_ans = integer_calc()
        print(image_ans)
    else:
        text_ans = calc_text_bits()
        print(text_ans)

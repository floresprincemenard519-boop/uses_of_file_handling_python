while True:
    text_to_input = input("Enter what you want to write (Enter 'quit' to exit): ")
    if text_to_input == "quit":
        break

def write_to_file(file_name, text):
    with open(file_name, "a") as file:
        file.write(text)

write_to_file("mylife.txt", text_to_input)
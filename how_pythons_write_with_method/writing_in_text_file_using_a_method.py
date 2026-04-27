def write_to_file(file_name):
    while True:
        text_to_input = input("Enter what you want to write (Enter 'quit' to exit): ")
        if text_to_input == "quit":
            break
        with open(file_name, "a") as file:
            file.write(text_to_input + "\n")
        
               
    

write_to_file("mylife.txt")
class Writer:
    def __init__(self, file_name):
        self.file_name = file_name

    def write_to_file(self):
        with open(self.file_name, "a") as file:
            while True:
                text_to_input = input("Enter what you want to write (Enter 'quit' to exit): ")
                if text_to_input == "quit":
                    break
                file.write(text_to_input + "\n")
            

class FileManager:
    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.mode = mode
        self.file = None

    def __enter__(self):
        print("Start!")
        self.file = open(self.file_name, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("End!")
        self.file.close()


with FileManager("myFile.txt", "w") as file:
    file.write("Hello")

print(file.closed)
class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def write_data(self, text):
        with open(self.filename, "w") as file:
            file.write(text)

    def read_data(self):
        with open(self.filename, "r") as file:
            return file.read()


fm = FileManager("info.txt")

fm.write_data("This file is handled using OOP\nPython is awesome")

print(fm.read_data())

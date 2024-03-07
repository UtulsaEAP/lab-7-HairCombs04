"""
Name: Bradyn Combs
Lab Time: 3/7/24 2:00 PM
"""

def fileNameChange():
    #type your code here
    input_file = input()
    try:
        with open(input_file, 'r') as file:
            for line in file:
                line = line.strip()
                modified_line = line.replace("_photo.jpg", "_info.txt")
                print(modified_line)
    except FileNotFoundError:
        return
    return
if __name__ == '__main__':
    fileNameChange()
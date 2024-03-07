"""
Name: Bradyn Combs
Lab Time: 3/7/24 2:00 PM
"""

def wordInRange():
    #Type your code here
    file_name = input()
    lower_bound = input()
    upper_bound = input()
    with open(file_name, 'r') as file:
        lines = file.readlines()
    for line in lines:
        string = line.strip()
        if lower_bound <= string <= upper_bound:
            print(string, '- in range')
        else:
            print(string, '- not in range')
    return
if __name__ == '__main__':
    wordInRange()
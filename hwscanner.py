import re

#my edited Char_Range from Ned Batchelder in https://stackoverflow.com/questions/7001144/range-over-character-in-python 
def char_range(c1: str, c2: str):
    """
    returns the characters from `c1` to `c2`, inclusive.
    Ex. char_range('a', 'd') returns 'abcd'
    """
    ret = ''
    for c in range(ord(c1), ord(c2)+1):
        ret+= chr(c)
    return ret


def read_hw():
    '''
    Iterates through each line of hw.txt, splitting the line into 3 parts: "1) 1.12.2 d, e, f" becomes ['1)','1.12.2','d, e, f'].
    The intent of this is to separate the problems ( 'd, e, f' ) from the section ( '1.12.2' ). 
    Skipping any empty lines, the program replaces any commas and spaces with '', turning 'd, e, f' to 'def'
    If it finds a '-', indicating a letter range, ex. a-c, read_hw() calls char_range(a,c) to produce 'abc'
    
    Now since the problem 'd, e, f' is simplified to 'def', the mutated list is appended to line_list, and at the very end after many iterations, is returned. 
    '''
    line_list = []
    with open('hw.txt','r') as hw:
        ret = ''
        for line in hw:
            line = line.strip().split(' ',2)
            if line != ['']:
                if len(line) == 3:
                    line[2] = re.sub(r'[, .]','',line[2])
                    if '-' in line[2]:
                        line[2] = char_range(line[2][0], line[2][-1])
                #print(line)
                line_list.append(line)
            #ret+=line[2]
    return line_list

def ask(line_list: [list]):
    '''
    Recieving a list of lists of problem numbers, section numbers, and problems,
    ask iterates through each line in the list, asking the user for the last problem letter in the respective section, skipping sections that assign all problems by leaving the problem area empty.
    ex. 1) 4.1.1
    With no d, e, f   etc.

    It will reprompt until the input is valid.

    If g is the last problem in 1.12.2, this function turns the 'def' from read_hw() and turns it into 'abcg' , ommiting all characters 'def' within
        the range of a-g.
    It arranges the output to look nice, with the unassigned problems printed outside the function as "1.12.2: a, b, c, g" for each line. d, e and f were assigned and are not in the resulting string.
    If all problems for a section were assigned, ask puts none, "ex: 2.1.6: none" and prints that outside the function.

    While inside, it just adds these terms to a string, prepping the print later in the if __name__ == '__main__':
    '''
    ret = ''
    for line in line_list:
        
        if len(line) == 3:
            while True:
                last = input(f'{line[1]}: ')
                #print(f'last: {last}, line[2][-1]: {line[2][-1]}')
                if last >= line[2][-1] and last.isalpha() and last.islower and len(last) == 1:
                    break
                elif not last.isalpha() or not last.islower or len(last) != 1:
                    print(f'input \'{last}\', is not a lowercase singular alphabet.')
                else:
                    print("Too High, Try Again")
            
            chars = char_range('a', last)

            for assigned in line[2]:
                chars = chars.replace(assigned, '')
            line[2] = ', '.join(chars)
            ret+=f'{line[1]}: {line[2]}\n'
        else:
            ret+=f'{line[1]}: none\n'

    return ret


if __name__ == '__main__':
    print('Enter the last problem for each exercise.\n')
    line_list = read_hw()
    book = ask(line_list)
    print('\n<><><> Problems Not Assigned:')
    print(book)
    input("Enter anything to exit ")
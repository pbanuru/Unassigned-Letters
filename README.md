## Unassigned Problems:

This program ([hwscanner.py](https://github.com/pbanuru/Unassigned-Letters/blob/main/hwscanner.py)) looks at each line in a text file ([hw.txt)](https://github.com/pbanuru/Unassigned-Letters/blob/main/hw.txt), and finds the letters not assigned to the section associated for that line.

It was designed to be used with zyBooks.
Given a text file containing the following:

    1) 4.1.1
    2) 4.1.3
    3) 4.1.5 c,d,g,k
    4) 4.1.6 a, c
    5) 4.2.2
    6) 4.2.4 c, d
    7) 4.3.2 d, g, k, j
    8) 4.3.4 d, g
    9) 4.3.6
    10) 4.4.1
    11) 4.4.2 b, e, g
    12) 4.5.1
    13) 4.5.2
    14) 4.5.5
    15) 4.5.7
    16) 4.6.1
    17) 4.6.5

[hwscanner.py](https://github.com/pbanuru/Unassigned-Letters/blob/main/hwscanner.py) sees section 4.1.1 and knows that all problems were assigned, and prints "4.1.1: none"
All problems are assigned when there are no problems written besides the section.

It sees 4.1.5 and "c, d, g, k" It asks the user for the last letter of that section, which is "l,"
and prints "4.1.5: a, b, e, f, h, i, j, l"

Note, the print is the section and the range of letters from a-l, excluding c, d, g, and k. It excludes the assigned letters.

It continues to ask for all sections that are not "all assigned"

At the end, this is the output:
![Output: ](https://github.com/pbanuru/Unassigned-Letters/blob/main/example.png)

You can change the ([hw.txt)](https://github.com/pbanuru/Unassigned-Letters/blob/main/hw.txt) to match your needs, as long as it is in the proper form: 
something section letters

It can handle letter ranges in the letters section. a-c will automatically be translated to abc

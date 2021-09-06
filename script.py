# heyo
# don't be stupid
# love you

import random

# Question banks in form of [Question]: [Answer]
Ch1 = {
    "What important concept was attributed to Ada Lovelace?": "The program loop",
    "What important pastry helped move your job up in the queue in second generation software, and what third generation software development make that pastry unnecessary?": "Donuts and time-sharing",
    "What features of transistors made them superior for computers, compared with vacuum tubes?": "They were cheaper, smaller, and cooler then tubes and lasted longer.",
    "What logical elements did Charles Sanders Peirce realize electrical switches could emulate in 1880?": "Boolean algebra",
    "Who is the father of modern computers?": "Alan Turing",
    "What important concept is attributed to John von Neumann?": "The stored program concept",
    "Which of the following is NOT an innovation that belongs to the Fourth Generation of Computing?": "World Wide Web",
    "Who was the first programmer?": "Ada Lovelace",
    "Which of the following is NOT an innovation that belongs to the Third Generation of Computing?": "Graphical User Interfaces",
    "Which of the following is NOT an innovation that belongs to the First Generation of Computing?": "Rotating Drum Storage",
    "Which of the following is NOT an innovation that belongs to the Second Generation of Computing?": "Von Neumann Architecture",
    "Name the 4 important elements of Babbage's Analytical Engine that are components of today's computers.": "An input device, memory, a central processing unit, and an output device.",
    "Who is the father of the computer?": "Charles Babbage",
    "Who is responsible for coming up with the concepts of a compiler and debugging?": "Grace Hopper",
    "Which of the following is NOT an innovation that belongs to the Fifth Generation of Computing?": "Internet",
    "The Jacquard loom is important in the history of computing for what innovation?": "Reusable cards with holes held information",
    "Leibniz built on Pascal's work by creating the Leibniz Wheel. This device was capable of what kind of calculations, in addition to the ones Pascal's could do?": "Multiplication and division",
    "The Apple computer became very popular. What was its largest market, and what software made it interesting to the market?": "The business market and the program VisiCalc",
    "in 1642 Pascal created a mechanical device with gears and levers. The device was capable of what kinds of calculation?": "Addition and subtraction"
}

# Add chapters here in form String: Dict
allChap = {"Ch1": Ch1}

def menuSelect():
    select = ''
    while select != '0' and select != '1' and select != '2':
        select = input()
        if select != '0' and select != '1' and select != '2':
            print('nope')
    print('cool')
    return select

# returns list with chaps
def selectChapters():
    print("what chapter (in form 'Ch#')")
    go = True
    chaps = []
    while go:
        select = ""
        while select not in allChap.keys():
            select = input().lower().capitalize()
            if select not in allChap:
                print('nope')
        chaps.append(select)
        print('cool')
        print("uno mas? (y/n)")
        more = ''
        while more != "y" and more != 'n':
            more = input().lower()
            if more != "y" and more != 'n':
                print('nope')
        print("aight")
        if more == 'n':
            go = False

    return chaps

def test(chaps):
    questionBank = {}
    print("Press enter to see answer/next question, q to quit")
    for chap in chaps:
        questionBank.update(allChap[chap])
    while 1:
        q = random.choice(list(questionBank.keys()))
        print(f"\n\n{q}")
        select = ' '
        while select != 'q' and select != '':
            select = input()
        if select == 'q':
            print('adios')
            exit()
        print(f"{questionBank[q]}")
        while select != 'q' and select != '':
            select = input()
        if select == 'q':
            print('adios')
            exit()


def main():
    print("Hello there.\nGeneral Kenobi!")
    print("...")
    print("Okay...")
    print("umm")
    print("select something, i guess")
    print("0 quit\n1 test all\n2 select chapters")
    selection = menuSelect()
    chaps = allChap.keys()
    if selection == "0":
        print('adios')
        exit()
    if selection == "2":
        chaps = selectChapters()
    test(chaps)
    
    

if __name__ == "__main__":
	main()
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
    "Which of the following is NOT an innovation that belongs to the Fourth Generation of Computing? {www, gui, microprecessors, internet}": "World Wide Web",
    "Who was the first programmer?": "Ada Lovelace",
    "Which of the following is NOT an innovation that belongs to the Third Generation of Computing? {Integrated Circuits, time-sharing, operating systems, GUI}": "Graphical User Interfaces",
    "Which of the following is NOT an innovation that belongs to the First Generation of Computing? {Von neumann Architecture, rotating drum storage, vacuum tubes, punch cards}": "Rotating Drum Storage",
    "Which of the following is NOT an innovation that belongs to the Second Generation of Computing? {Transistors, rotating drum storage, von neumann Architecture, magnetic core memory}": "Von Neumann Architecture",
    "Name the 4 important elements of Babbage's Analytical Engine that are components of today's computers.": "An input device, memory, a central processing unit, and an output device.",
    "Who is the father of the computer?": "Charles Babbage",
    "Who is responsible for coming up with the concepts of a compiler and debugging?": "Grace Hopper",
    "Which of the following is NOT an innovation that belongs to the Fifth Generation of Computing? {networks, www, internet, parallel computing}": "Internet",
    "The Jacquard loom is important in the history of computing for what innovation?": "Reusable cards with holes held information",
    "Leibniz built on Pascal's work by creating the Leibniz Wheel. This device was capable of what kind of calculations, in addition to the ones Pascal's could do?": "Multiplication and division",
    "The Apple computer became very popular. What was its largest market, and what software made it interesting to the market?": "The business market and the program VisiCalc",
    "in 1642 Pascal created a mechanical device with gears and levers. The device was capable of what kinds of calculation?": "Addition and subtraction"
}
Modulator
Ch14 = {
    "Which of the following converts source code into computer language and result in an executable file? {IDE, interpreter, compiler, algorithm}": "Compiler",
    "What is the computer science term for a logically ordered set of statements used to solve a problem?": "algorithm",
    "What is a name used to identify a specific location and value in memory?": "Variable",
    "Pseudocode should be written after the source code to ensure that the program was written correctly.": "False",
    "The only language computers can understand consists of 1s and 0s.": "True",
    "Which of the following translates a program statements, one by one, into a language the computer can understand? {IDE, interpreter, compiler, algorithm}": "Interpreter",
    "What is a readable description of an algorithm written in human language called?": "pseudocode"
}

Ch3 = {
    "Which of the following is NOT a bus signal group? {Data, fetch, address, control}": "Fetch",
    "Complete the truth table for an AND Gate.": "11=1; 01=0; 00=0; 10=0",
    "What are most computers today based on?": "Von Neumann Architecture",
    "High-speed [?] is used to speed processing in a computer system.": "cache memory",
    "The [?] contains instruction and data that provides the startup program for a computer.": "BIOS",
    "What are the 4 basic functions implemented in the CPU?": "Adding, decoding, shifting, and storing",
    "A [?] is computer terminology for a set of sires and protocols designed to facilitate data transfer.": "bus",
    "Which of the following is NOT a part of a transistor? {Collector, base, modulator, emmiter}": "Modulator",
    "Most computers these days use the [?] bus": "PCI",
    "Complete the truth table for an OR gate": "00=0; 10=1; 11=1; 01=1",
    "Which type of memory can't be easily written to?": "ROM",
    "Which type of I/O processing is most efficient?": "Interrupt"
}

Ch3 = {
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": ""
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

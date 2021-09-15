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
    "Pseudocode should be written after the source code to ensure that the program was written correctly. T/F": "False",
    "The only language computers can understand consists of 1s and 0s. T/F": "True",
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

Ch4 = {
    "Bandwidth is the speed of a transmission, measured in bytes per second. T/F": "False",
    "Which OSI level is responsible for physical addressing, data error notification, ordered delivery of frames and flow control? {Presentaion, Network, Application, Data-link, Physical, Session, transport}": "Data-link",
    "What does TDM stand for?": "Time-division multiplexing",
    "Which networking hardware is used for connecting networks of different types?": "Gateway",
    "Which networking hardware is used for allowing only specific network traffic through, based on destination address?": "Bridge",
    "Which topology became popular due to the Internet and home networking?": "Star",
    "Which OSI level is responsible for assigning addresses to messages and provides connectivity and path selection? {Presentaion, Network, Application, Data-link, Physical, Session, transport}": "Network",
    "DSL is a combination of what two types of multiplexing? ": "FDM and TDM",
    "Which type of guided medium is the least susceptible to attenuation and inductance?": "Fiber-optic cable",
    "Which OSI level is responsible for guaranteed delivery of datagrams, fault detection, error recovery, and flow control? {Presentaion, Network, Application, Data-link, Physical, Session, transport}": "Transport",
    "Which OSI level is responsible for establishing, maintaining, and terminating the communication session between applications? {Presentaion, Network, Application, Data-link, Physical, Session, transport}": "Session",
    "Which of the following is NOT a LAN typology?": "Coaxial",
    "What does FDM stand for?": "Frequency-division multiplexing",
    "What is a circuit board that connects a network to the system bus and converts a computer's binary information into a format suitable for the transmission medium called?": "NIC",
    "Which networking hardware is used for directing network traffic, based on its logical address?": "Router",
    "Which networking hardware functions as a multiport signal amplifier?": "Hub",
    "Which networking hardware is used for amplifying signals on long cables between nodes?": "Repeater",
    "What is fiber-optic cable made out of?": "Glass",
    "Which OSI level is responsible for formatting data and character format translation? {Presentaion, Network, Application, Data-link, Physical, Session, transport}": "Presentation",
    "Which OSI level is responsible for giving applications access to the network? {Presentaion, Network, Application, Data-link, Physical, Session, transport}": "Application",
    "Which OSI level is responsible for electrical, mechanical, procedural, and functional specifications? {Presentaion, Network, Application, Data-link, Physical, Session, transport}": "Physical",
    "What factor reduces the strength of an electrical signal as it travels along a transmission medium?": "Attenuation",
    "Modems convert binary digits into sounds by modulating tones. T/F": "True",
    "How does a WLAN differ from a LAN?": "It uses unguided media"
}

Ch5 = {
    "Which of the following protocols is responsible for sending email? {FTP, SMTP, DHCP, TCP/IP, HTTP}": "SMTP",
    "Which network device is used to resolve domain names into IP addresses?": "DNS servers",
    "What does NBP stand for?": "National Backbone Provider",
    "Which of the following protocols maintains port information? {FTP, SMTP, DHCP, TCP/IP, HTTP}": "TCP/IP",
    "Which of the following protocols is responsible for assigning IP addresses to services? {FTP, SMTP, DHCP, TCP/IP, HTTP}": "DHCP",
    "What is the standard port number for HTTP?": "80",
    "Which of the following protocols is responsible for sending and receiving data on the web? {FTP, SMTP, DHCP, TCP/IP, HTTP}": "HTTP",
    "Which of the following protocols is responsible for reliable file transfer between computers? {FTP, SMTP, DHCP, TCP/IP, HTTP}": "FTP",
    "The internet is a collection of LANS and WLANS. T/F": "False",
    "The Internet is owned by:": "No one",
    "Why are we switching from IPv4 to IPv6?": "It has more addresses",
    "Which of the following protocols managers sequencing data packets? {FTP, SMTP, DHCP, TCP/IP, HTTP}": "TCP/IP",
    "What prevents TCP/IP packets from bouncing from router to router forever?": "TTL",
    "Which of the following protocols is responsible for reliable delivery of data between computers? {FTP, SMTP, DHCP, TCP/IP, HTTP}": "TCP/IP",
    "What is the language of the World Wide Web?": "HTML",
    "What are switching centers maintained by Internet providers called?": "Point of presence"
}

Ch6 = {
    "What does Third Normal Form state?": "No nonkey columns depend on another non key column",
    "By default, data returned by the SQL SELECT statement is in descending order. T/F": "False",
    "What uniquely identifies a row in a table?": "Primary Key",
    "What is the set of possible value for a column called?": "Domain",
    "What does First Normal Form state?": "Eliminate Repeated Fields",
    "A database is divided into tables. T/F": "True",
    "What does Second Normal Form state?": "Every column that's not part of the primary key is fully dependent on the primary key",
    "Organize the steps for making a database.": "Investigate and define, make a master column list, create the tables, work on relationships, analyze the desing, re-evaluate"
}

Ch7 = {
    "How many different number of states can be represented with 4 binary digits?": "16",
    "What is the binary equivalent of the decimal number 114?": "0111 0010",
    "What is the two's complement of the binary number 1001 0001?": "0110 1111",
    "What is the hexadecimal equivalent of the decimal number 214?": "D6",
    "What is the binary result of adding the binary numbers 0111 + 0011?": "1010",
    "What is the decimal equivalent of the binary number 1010 1111?": "175",
    "What is the hexadecimal equivalent of the binary number 1101 0101?": "D5",
    "What is the binary result of subtracting the binary numbers 1001 - 0101?": "0100",
    "What color is represented if all the pixel bits are set to 0?": "Black"
}

Ch8 = {
    "Which sorting algorithm is this: Grabs a set of values then uses insertion sort on the set. Grabs a larger set of data on each pass, until the list is sorted. {Selection, Bubble, Insertion, Quicksort, Merge, Shell}": "Shell Sort",
    "What is the height of the binary tree? {7<4<2<1}": "3",
    "How many comparisons does it take to get to 14? {7<11<13<14}": "7",
    "An array with 5 elements has memory locations of 1 through 5. T/F": "False",
    "What does LIFO stand for?": "Last in First out",
    "Which sorting algorithm is this: Compares every two elements and swaps as needed, then merges the lists of two into lists of four, etc... until the last two lists are merged into the final sorted list. {Selection, Bubble, Insertion, Quicksort, Merge, Shell}": "Merge",
    "What does FIFO stand for? ": "First in First out",
    "Which sorting algorithm is this: Works by taking elements from the list one by one and inserting them in their correct position into a new sorted list. {Selection, Bubble, Insertion, Quicksort, Merge, Shell}": "Insertion",
    "A queue uses a FIFO structure. T/F": "True",
    "Which sorting algorithm is this: Finds the minimum value, swaps it with the value in the first position, and then repeats these steps for the remainder of the list. {Selection, Bubble, Insertion, Quicksort, Merge, Shell}": "Selection Sort",
    "Which sorting algorithm is this: Compare the first two elements and swaps them if the first is greater than the second. It continues doing this for each pair of adjacent elements to the end of the data set, then starts again; it continues doing this until no swaps have occurred on the last pass. {Selection, Bubble, Insertion, Quicksort, Merge, Shell}": "Bubble Sort",
    "Which sorting algorithm is this: All elements smaller than a chosen pivot are moves before it and all greater elements are moved after it. {Selection, Bubble, Insertion, Quicksort, Merge, Shell}": "Quicksort",
    "A stack uses a LIFO structure. T/F": "True"
}
Ch9 = {
    "What needs to be done to a disk before you can use it?": "Partitioned and formatted",
    "The process of [] arranges the disk's surface into addressable areas and sets up the disk's basic directory tree structure.": "formatting",
    "Command-line and GUI are the two basic types of user interfaces in an operating system. T/F": "True",
    "What is the Linux command for creating a folder?": "mkdir",
    "The operating system is the first program loaded into memory when a computer is started. T/F": "True",
    "What is the core program of an operating system called?": "Kernel",
    "What is the Linux command for copying a file or folder?": "cp",
    "Multitasking operating systems can service many different things at once. What are those things called?": "Program tasks",
    "The [] portion of an operating system remains in memory the entire time the computer is on.": "kernel",
    "What is the Linux command for renaming a file or folder?": "mv",
    "Select all the main functions of an operating system.": "provide security, provide UI, manage resources, manage processes",
    "An operating system method of allowing multiple processes to share the CPU is called what?": "Time Slicing",
    "What is the Linux command for moving a file or folder?": "mv",
    "What is the Linux command for deleting a file or folder?": "rm",
    "What is the main level of a disk called?": "root",
    "What is the Linux command for listing the contents of a folder?": "ls"
}

Ch10 = {
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

Ch11 = {
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

Ch12 = {
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
allChap = {"Ch1": Ch1, "Ch14": Ch14, "Ch2": Ch2, "Ch3": Ch3, "Ch4": Ch4, "Ch5": Ch5, "Ch6": Ch6, "Ch7": Ch7, "Ch8": Ch8}

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

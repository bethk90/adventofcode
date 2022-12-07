"""
Your subroutine needs to identify the first position where the four most recently received characters were all different

Specifically, it needs to report the number of characters from the beginning of the buffer to the end of the first such
four-character marker.

How many characters need to be processed before the first start-of-packet marker is detected?

"""


def find_marker(text):
    for i in range(len(text)):
        packet = [x for x in text[i:i+4]]
        if len(set(packet)) == 4:
            return i + 4


day_six_input = open('daysix.txt').read()
(print(find_marker(day_six_input)))


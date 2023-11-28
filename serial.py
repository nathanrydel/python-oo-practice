class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start=0):
        """constructor function to create a new SerialGenerator instance"""

        self.start = start
        self.next = start

    def __repr__(self):
        return f"<SerialGenerator start={self.start} next_serial={self.next}>"

    # TODO: may have a better way to implement this - keep the start val group
    # with other numbers - relationship between the start val and next
    def generate(self):
        """generate and return a new serial number"""

        self.next += 1
        return self.next - 1
        # if self.count == 0:
        #     self.count += 1
        #     return self.start
        # else:
        #     self.count += 1
        #     self.next_serial += 1
        #     return self.next_serial

    def reset(self):
        """reset the serial number to the starting value"""

        self.next = self.start

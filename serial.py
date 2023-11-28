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
        self.next_serial = start

    # FIXME: never generates the starting serial
    def generate(self):
        """generate and return a new serial number"""
        self.next_serial += 1
        return self.next_serial

    def reset(self):
        """reset the serial generation to the starting value"""
        self.next_serial = self.start

"""Iterating over the weekdays."""

class WeekdayIterator(object):

    def __init__(self):
        self.i = 0
        self.weekdays = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")

    def __iter__(self):
        """# If this object were a container, then this method would return the iterator over the
        elements of the container."""
        return self

    def __next__(self):
        """Returns the next weekday"""
        if self.i == 7:
            raise StopIteration
        else:
            weekday = self.weekdays[self.i]
            self.i += 1
            return weekday


for w in WeekdayIterator():
    print(w)




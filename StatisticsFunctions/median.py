from MathOperations.addition import Addition
from MathOperations.division import Division

class Median:
    @staticmethod
    def median(data):
        n = len(data)
        s = sorted(data)
        return (sum(s[n//2-1:n//2+1])/2.0, s[n//2])[n % 2] if n else None
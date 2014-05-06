class RegexpADP():
    """Implement regexp functionality without using re module"""

    def __init__(self, pattern):
        self.pattern = pattern

    """ Essentially this function walks two patterns side-by-side and compares them.
        The testString is the string we are testing against the patternString.
        We walk the patterns backward so that we can account for * and ? operators (both
        are effectively look-behind operators) in a single pass"""
    def match(self, testString):

        # Our return value
        retval = []

        # print "\ntesting {} againts {}".format(testString, self.pattern)
        # A match can start anywhere within our testString. So we actually do n separate passes
        # for a string of length n, the i-th pass staring at the n-i index.
        for i in reversed(range(0, len(testString))):
            candidate = ''
            patternIncrement = 0
            testIncrement = 0

            # This is where our comparison begins
            for j in range(0, len(self.pattern)):
                testIndex = i - j - testIncrement
                patternIndex = len(self.pattern) - 1 - j - patternIncrement

                # In the case where our pattern is longer than our test string, we should fail
                if(testIndex == 0 and patternIndex > 0):
                    candidate = ''

                # We also bounce before we hit out-of-bounds indices
                elif(testIndex >= 0):
                    testChar = testString[testIndex]
                    patternChar = self.pattern[patternIndex]

                    # The hopeful case: we match and we append our testChar to our candidate match
                    if(self.naturalMatch(testChar, patternChar)):
                        candidate = testChar + candidate
                        continue

                    # With the star or question-mark match, we have a slightly different method
                    elif(patternChar == '*' or patternChar == '?'):

                        # grab the character to the left of the star.
                        # We are alowed to match zero or more of these
                        repeatableChar = self.pattern[patternIndex-1]

                        # Increment our pattern marker (move it left one) to account for the "matched" character
                        patternIncrement += 1

                        # Our string counter will need to account for the * character as well
                        testIncrement -= 1

                        # Loop along out test string and add all consecutive characters matching
                        # our "matched" character
                        k = 0
                        while(self.naturalMatch(testString[testIndex-k], repeatableChar)):
                            testIncrement += 1
                            k += 1
                            candidate = testChar + candidate
                            # If we have a question mark, we bounce after one uteration
                            if(patternChar == '?'):
                                break

                        # A formality
                        continue

                    else:
                        candidate = ''
                        break
            if(len(candidate)):
                # print "appending candidate {}".format(candidate)
                retval.insert(0, candidate)
        return retval

    def naturalMatch(self, testChar, patternChar):
        return (testChar == patternChar or patternChar == '.')

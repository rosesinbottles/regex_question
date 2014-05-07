class RegexpADP():
    """Implement regexp functionality without using re module"""

    def __init__(self, pattern):
        self.pattern = pattern

    """ Essentially this function walks two patterns side-by-side and compares them.
        The testString is the string we are testing against the patternString.
        We walk the patterns backward so that we can account for * and ? operators (both
        are effectively look-behind operators) in a single pass"""
    def match(self, testString):
        retval = []
        # A match can start anywhere within our testString. So we actually do n separate passes
        # for a string of length n, the i-th pass staring at the n-i index.
        for i in reversed(range(0, len(testString))):
            candidate = ''
            patternIncrement = 0
            testIncrement = 0
            questionMatched = False

            for j in range(0, len(self.pattern)):
                testIndex = i - j - testIncrement
                patternIndex = len(self.pattern) - 1 - j - patternIncrement

                if(testIndex == 0 and patternIndex > 0):
                    candidate = ''

                elif(testIndex >= 0):
                    testChar = testString[testIndex]
                    patternChar = self.pattern[patternIndex]

                    if(self.naturalMatch(testChar, patternChar)):
                        candidate = testChar + candidate
                        questionMatched = False
                        continue

                    elif(questionMatched):
                        testIncrement -= 1
                        questionMatched = False
                        continue

                    # With the star or question-mark match, we have a slightly different method
                    elif(patternChar == '*' or patternChar == '?'):

                        repeatableChar = self.pattern[patternIndex-1]
                        patternIncrement += 1
                        testIncrement -= 1
                        k = 0
                        while(self.naturalMatch(testString[testIndex-k], repeatableChar)):
                            testIncrement += 1
                            k += 1
                            candidate = testChar + candidate
                            if(patternChar == '?'):
                                questionMatched = True
                                break

                        continue

                    else:
                        candidate = ''
                        break
            if(len(candidate)):
                retval.insert(0, candidate)
        return retval

    def naturalMatch(self, testChar, patternChar):
        return (testChar == patternChar or patternChar == '.')

class RegexpADP():
    """Implement regexp functionality without using re module"""

    def __init__(self, pattern):
        self.pattern = pattern

    def match(self, testString):
        retval = []
        # we can start anywhere in our comparison string (at least until we
        # implement ^) so we'll make a separate pass starting at each
        # position in our test string
        for i, c in enumerate(testString):
            # want to be sure our whole regexp fits
            candidate = ''
            for j, d in enumerate(self.pattern):
                if(i+j < len(testString) and (d == testString[i+j] or d == '.')):
                    candidate += testString[i+j]
                    continue
                else:
                    candidate = ''
                    break
            if(len(candidate)):
                retval.append(candidate)
        return retval

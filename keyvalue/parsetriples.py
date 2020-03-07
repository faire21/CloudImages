import re

class ParseTriples():

    def __init__(self,filename):
        super().__init__()
        self._filename = filename
        self._file = open(self._filename,"r",errors='ignore')

    def getNext(self):
        if(self.closed):
            print('closed')
            return None

        line = self.readline()
        while((isinstance(line,str)) and line.startswith("#")):
            line = self.readline()
        if '?width=300' in line:
            line = self.readline()

        if(not line):
            return None

        m = re.match('<(.+)>\s*<(.+)>\s*[<"](.+)[>"]',line.strip())
        if(m):
            return m.group(1),m.group(2),m.group(3)
        else:
            return




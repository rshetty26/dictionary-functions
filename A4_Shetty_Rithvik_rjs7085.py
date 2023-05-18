
class MyDict:
    def __init__(self):
        x=[]
        currentline = []
        infile = open("data-file.txt", 'r')
        for line in infile:
            currentline = line.split(", ")
            x = x + [currentline]
        infile.close()
        self.lst = x

    def clear(self):
        self.lst = [[]]
    
    def copy(self):
        newlist = self.lst

    def get(self, identifier):
        for x in range(0, len(self.lst)):
            if (self.lst[x][0] == identifier):
                return self.lst[x]

    def items(self):
        return self.lst

    def identifier(self):
        returnlist = []
        for x in range(0, len(self.lst)):
            returnlist = returnlist + [self.lst[x][0]]
        return returnlist

    def pop(self, identifier):
        newlist = []
        found = -1
        value = []
        for x in range(0, len(self.lst)):
            if (self.lst[x][0] == identifier):
                value = self.lst[x]
                found = 1
            else:
                newlist = newlist + [self.lst[x]]
        if (found != -1):
            self.lst = newlist
            return value
        else:
            return "Identifier not found"
        
    def popitem(self):
        newlist = []
        for x in range(0, len(self.lst)-1):
            newlist = newlist + [self.lst[x]]
        self.lst = newlist

    def update (self, newitem):
        self.lst = self.lst + [newitem]
    
    def values(self): 
        for rows in self.lst:
            for item in rows:
                print(item)


'''
md = MyDict()
print(md.items())
print()

print(md.get('456-89-7853'))
print()

print(md.identifier())
print()

print(md.pop('456-89-7853'))
print()

md.update(['264-90-4525', 'DOB:13 Dec 2003', 'Full-Name:Timothy Alfred Turner'])
print(md.items())
print(md.identifier())
print()

md.popitem()
print(md.identifier())
print()

md.values()
'''

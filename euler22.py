
def euler22():
    
    with open('data/p022_names.txt') as fp:
        names = fp.read().split(',')
        names = [name.strip('"') for name in names]
    
    names.sort()

    def name_score(name):
        return sum(ord(c) - 64 for c in name)

    return sum((i+1)*name_score(name) for i,name in enumerate(names))
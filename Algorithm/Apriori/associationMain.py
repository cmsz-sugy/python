#conding:utf-8


import associationRule1
def read_file(raw_file):
    """read file"""

    return [sorted(list(set(e.split()))) for e in
            open(raw_file).read().strip().split('\n')]


def main():
    sentences = read_file('test.txt')
    assrules = associationRule1.associationRule(sentences)
    assrules.apriori()
    assrules.generateRules()


if __name__ == "__main__":
    main()
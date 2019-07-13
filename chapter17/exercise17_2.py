class Kangaroo:
    """A class describing a kangaroo

    attributes: pouch_contents
    """
    def __init__(self, name, contents=None):
        """Initializing a Kangaroo object.

        pouch_contents: list of objects of any type
        """
        self.name = name
        if contents is None:
            contents = []
        self.pouch_contents = contents

    def __str__(self):
        s = self.name + ' contains:\n'
        for item in self.pouch_contents:
            s = s + '\t' + object.__str__(item) + '\n'
        return s

    def put_in_pouch(self, item):
        """Adding an object of any type to the pouch

        """
        self.pouch_contents.append(item)

def main():
    kanga = Kangaroo('Kanga')
    roo = Kangaroo('Roo')
    kanga.put_in_pouch('Mitroglou')
    kanga.put_in_pouch('Gkekas')
    kanga.put_in_pouch('Byntra')
    kanga.put_in_pouch(roo)
    print(kanga)
    print(roo)

if __name__ == '__main__':
    main()

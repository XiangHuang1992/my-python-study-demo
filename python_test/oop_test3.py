class NewAddBookEntry:
    'new address book entry class'
    def __init__(self, nm, ph):
        self.name = Name(nm)
        self.phone = Phone(ph)

        print('created instance for:', self.name)

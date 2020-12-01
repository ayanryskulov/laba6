import pickle

class PhoneNumber:
    def __init__(self, name, nubmer):
        self.name = name
        self.nubmer = nubmer

class Main:
    def short(self, contacts):
        result = []
        for contact in contacts:
            if contact.name[0] == 'J' or contact.name[0] == 'K':
                result.append(contact)
        return result
    def serialization(self, contacts):
        with open('phone.pkl', 'wb') as f:
            pickle.dump(contacts, f)
    def main(self):
        contacts = [PhoneNumber('Kate', '4321'),
                    PhoneNumber('Mike', '5432'),
                    PhoneNumber('John', '6543'),
                    PhoneNumber('Alex', '7654')]
        self.serialization(self.short(contacts))

if __name__== "__main__":
    main = Main()
    main.main()
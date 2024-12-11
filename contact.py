contacts={} # dictionary


def add_contact(name,number):
    contacts[name]=number      # Element hinzufügen [key]=value (appen)

def show_all():
    for c in contacts:
        print(c, contacts[c]) # key: value -> Max:01773423423

def find(name):
    return contacts[name]

def upate_contact(name,number):
    contacts[name]=number      # der vorhandene Name (Key) wird überschrieben -> key ist immer eindeutig (nur einmal)


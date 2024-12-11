contacts={} # dictionary

''' add Contact to Contacts'''
def add_contact(name,number):
    contacts[name]=number      # Element hinzufügen [key]=value (appen)

''' print all contacts'''
def show_all():
    for c in contacts:
        print(c, contacts[c]) # key: value -> Max:01773423423

'''find Number from Name'''
def find(name):
    return contacts[name]

'''give a new Number'''
def upate_contact(name,number):
    contacts[name]=number      # der vorhandene Name (Key) wird überschrieben -> key ist immer eindeutig (nur einmal)


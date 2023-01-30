from Person import Person


def list_to_dict():
    #Nous avons deux listes, il suffit de les convertir en dictionnaire Python
    list_key : list = ['clef_un', 'clef_deux', 'clef_trois']
    list_value : list = ['value_un', 'valeu_deux', 'value_trois']

    #return dict(zip(list_key, list_value))

    new_dict: dict = {}
    if len(list_key) == len(list_value):
        for index, value in enumerate(list_key):
            new_dict[value]=list_value[index]
        return new_dict
    else:
        print("Two lists have different length")
        return new_dict

def fusion_dict():
    #Il faut fusionner deux dictionnaire en un
    dict_un : dict = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
    dict_deux : dict = {'Fourty': 40, 'Fifty': 50}
    return dict_un | dict_deux

def display_key_values():
    #Vous devez afficher les clefs du dictionnaires ainsi que ses valeurs
    # Si une valeur vaux 0, il faut afficher "absence de données"
    dict_sample : dict = {'Ten': 0,
                          'Twenty': 20,
                          'Thirty': 60,
                          'Fourty': 15,
                          'Fifty': 50}
    for number_in_letters in dict_sample:
        if dict_sample[number_in_letters] == 0:
            print("key : ", number_in_letters, " value : absence de données")
        else:
            print("key : ",number_in_letters, " value : ", dict_sample[number_in_letters])

def display_key(key : str):
    #l'utilisateur vous donne a donné une clef au préalable, vous devez afficher sa valeur
    dict_sample : dict = {'nom' : 'toto',
                          'prenom': 'tarte',
                          'age': 20}
    return dict_sample[key]

def rename_key_dict(new_key : str, old_key : str):
    #Vous devez remplacer le nom de la clef od_key à new_key
    sample_dict : dict = {
        "name": "Kelly",
        "age": 25,
        "salary": 8000,
        "city": "New york"
    }
    sample_dict[new_key] = sample_dict.pop(old_key)
    return sample_dict

def division(numerator : int, denumerator : int):
#Réaliser une division avec une gestion d'erreur
    if denumerator == 0:
        return "Impossible"
    else:
        return numerator/denumerator


def moyenne_note():
#demandez à l'utilisateur des notes, si la notes est inférieur à 0 ou superieur à 20
    #indiquez lui que la note n'est pas correcte.
    #Vous devez mettre en place une gestion d'erreur afin d'éviter que l'utiliasteur saisi des str
    entered_str = input("Please enter notes separated by spaces : ")
    notes_list = entered_str.split()
    return notes_list


if __name__ == "__main__":
    person: Person = Person('Toto', 'Tata')
    person_un: Person = Person('Manu', 'Club')
    print(person.imc())
    print(person.nom)
    print(fusion_dict())
    display_key_values()
    print(display_key("age"))
    print(rename_key_dict("gorod","city"))
    print(division(3,0))
    print(moyenne_note())
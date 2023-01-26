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


if __name__ == "__main__":
    print(list_to_dict())
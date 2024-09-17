import os

TARGET_DIR = input("Передайте путь до папки:")

listdir = os.listdir(TARGET_DIR)

conversion = {
        'А': 'A',
        'Б': 'B',
        'В': 'V',
        'Г': 'G',
        'Д': 'D',
        'Е': 'E',
        'Ё': 'Jo',
        'Ж': 'Zh',
        'З': 'Z',
        'И': 'I',
        'Й': 'J',
        'К': 'K',
        'Л': 'L',
        'М': 'M',
        'Н': 'N',
        'О': 'O',
        'П': 'P',
        'Р': 'R',
        'С': 'S',
        'Т': 'T',
        'У': 'U',
        'Ф': 'F',
        'Х': 'H',
        'Ц': 'Ts',
        'Ч': 'Ch',
        'Ш': 'Sh',
        'Щ': 'Shh',
        'Ъ': "'",
        'Ы': 'Y',
        'Ь': "'",
        'Э': 'E',
        'Ю': 'J',
        'Я': 'Ja',
        }


for filename in listdir :
        new_filename = ""
        for letter in filename:
                if letter.upper() in conversion:
                        new_letter = conversion.get(letter.upper())
                        if letter.islower():
                                new_filename += new_letter.lower()
                        else:
                                new_filename += new_letter
                else:
                        new_filename += letter
                        print("SORRY. Mapping for " + letter + " not exist")

        print("Yahoo! New name: " + new_filename)
        os.rename(os.path.join(TARGET_DIR, filename), os.path.join(TARGET_DIR, new_filename))

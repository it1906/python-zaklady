import json
import csv


def textfile_read(path, encoding='utf-8'):
    try:
        with open(path, encoding=encoding) as file:
            data = file.read()
            print("Soubor otevřen.")
    except FileNotFoundError as error:
        return f'Soubor nebyl otevřen: {error}'
    except Exception as error:
        return f'Došlo k obecné výjimce: {error}'
    else:
        print("Vše je v pořádku")
    finally:
        print("Soubor uzavřen.")
        file.close()
    return data

def textfile_write(path, data = '', encoding='utf-8'):
    try:
        with open(path, mode = 'w', encoding=encoding) as file:
            file.write(data)
    except FileNotFoundError as error:
        print(f'Soubor nebyl otevřen: {error}')
        return False
    except Exception as error:
        print(f'Došlo k obecné výjimce: {error}')
        return False
    finally:
        file.close()
    return True
# txt = textfile_read('./python.txt')
# print(textfile_write('./novy.txt',txt))

def jsonfile_read(path, encoding='utf-8'):
    try:
        with open(path, encoding=encoding) as file:
            data = json.load(file)
    except FileNotFoundError as error:
        return f'Soubor nebyl otevřen: {error}'
    except Exception as error:
        return f'Došlo k obecné výjimce: {error}'
    finally:
        file.close()
    return data

def jsonfile_write(path, data = '', encoding='utf-8'):
    try:
        with open(path, mode = 'w', encoding=encoding) as file:
            json.dump(data, file)
    except FileNotFoundError as error:
        print(f'Soubor nebyl otevřen: {error}')
        return False
    except Exception as error:
        print(f'Došlo k obecné výjimce: {error}')
        return False
    finally:
        file.close()
    return True
# jsondata = jsonfile_read('./klient.json')
# print(jsonfile_write('./novy_json.txt', jsondata))

def csvfile_read(path, encoding='windows-1250'):
    try:
        with open(path, encoding=encoding, newline='\n') as file:
            reader = csv.DictReader(file, delimiter = ';', quotechar= '"')
            dict_list = []
            for row in reader:
                dict_list.append(row)
    except FileNotFoundError as error:
        return f'Soubor nebyl otevřen: {error}'
    except Exception as error:
        return f'Došlo k obecné výjimce: {error}'
    finally:
        file.close()
    return dict_list

def csvfile_write(path, data = '', encoding='windows-1250'):
    rows = csv_data
    try:
        with open(path, mode = 'w', encoding=encoding) as file:
            csv_writer = csv.DictWriter(file, ['Kodknihy', 'Titul', 'Popis', 'RokVydani', 'Cena', 'Typ'])
            csv_writer.writeheader()
            csv_writer.writerows(rows)
    except FileNotFoundError as error:
        print(f'Soubor nebyl otevřen: {error}')
        return False
    except Exception as error:
        print(f'Došlo k obecné výjimce: {error}')
        return False
    finally:
        file.close()
    return True
csv_data= csvfile_read('./kniha.csv', encoding='windows-1250')
print(csvfile_write('./novy_csv.txt', csv_data))
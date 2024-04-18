import os

class Filework():

    @staticmethod
    def read(filename):
        if not isinstance(filename, str):
            print("Имя файла должно быть строкой")
            return
        
        if not os.path.isfile(filename):
            print(f"Файл {filename} не существует")
            return
        
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                output = file.read()
                print(output)

        except PermissionError:
            print(f"Недостаточно прав для чтения файла {filename}")

        except IsADirectoryError:
            print(f"{filename} является директорией, а не файлом")

        except Exception as e:
            print(f"Произошла ошибка при чтении файла {filename}: {e}")


    @staticmethod
    def write(filename, text):
        if not isinstance(filename, str):
            print("Имя файла должно быть строкой")
            return
        
        if not isinstance(text, str):
            print("Текст должен быть строкой")
            return
        
        if not os.path.isfile(filename):
            print(f"Файл {filename} не существует")
            return
        
        try:
            with open(filename, 'a', encoding='utf-8') as file:
                file.write(f'{text}\n')

        except PermissionError:
            print(f"Недостаточно прав для записи в файл {filename}")

        except IsADirectoryError:
            print(f"{filename} является директорией, а не файлом")

        except Exception as e:
            print(f"Произошла ошибка при записи в файл {filename}: {e}")


    @staticmethod
    def clear(filename):
        if not isinstance(filename, str):
            print("Имя файла должно быть строкой")
            return
        
        if not os.path.isfile(filename):
            print(f"Файл {filename} не существует")
            return
        
        try:
            with open(filename, 'w') as file:
                file.write('')

        except PermissionError:
            print(f"Недостаточно прав для очистки файла {filename}")

        except IsADirectoryError:
            print(f"{filename} является директорией, а не файлом")

        except Exception as e:
            print(f"Произошла ошибка при очистке файла {filename}: {e}")

    @staticmethod
    def copy(src_filename, dest_filename):
        if not isinstance(src_filename, str):
            print("Имя исходного файла должно быть строкой")
            return
        
        if not isinstance(dest_filename, str):
            print("Имя целевого файла должно быть строкой")
            return
        
        if not os.path.isfile(src_filename):
            print(f"Файл {src_filename} не существует")
            return
        
        if os.path.isdir(dest_filename):
            print(f"{dest_filename} является директорией, а не файлом")
            return
        
        try:
            with open(src_filename, 'r', encoding='utf-8') as src_file:
                content = src_file.read()

            with open(dest_filename, 'w', encoding='utf-8') as dest_file:
                dest_file.write(content)

        except PermissionError:
            print(f"Недостаточно прав для копирования файла {src_filename}")

        except IsADirectoryError:
            print(f"{src_filename} или {dest_filename} является директорией, а не файлом")
            
        except Exception as e:
            print(f"Произошла ошибка при копировании файла {src_filename}: {e}")

file = Filework()

# file.read('text.txt')
# file.write('text.txt', 'Python')
file.copy('text.txt', 'new_text.txt')
# file.clear('new_text.txt')
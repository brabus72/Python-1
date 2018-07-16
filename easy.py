# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os
import sys


def mk_dir(path):
    try:
        os.mkdir(path)
        print('Директория успешно создана')
    except FileExistsError:
        print('Директория уже существует')
    except PermissionError:
        print('Недостаточно прав для создания директории')


def rm_dir(path):
    try:
        os.removedirs(path)
        print('Директория успешно удалена')
    except FileNotFoundError:
        print('Директория для удаления не найдена.')
    except PermissionError:
        print('Недостаточно прав для удаления директории')


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
def list_dir():
    print([i for i in os.listdir() if os.path.isdir(i)])


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
def create_file_copy():
    filename = sys.argv[0]

    with open(filename, 'rb') as f:
        name, extension = filename.split('.')
        with open(name + '_copy.' + extension, 'wb') as destination_f:
            destination_f.write(f.read())


if __name__ == "__main__":
    dir_path = 'dir_{}'
    [mk_dir(dir_path.format(i)) for i in range(1, 10)]
    [rm_dir(dir_path.format(i)) for i in range(1, 10)]

    list_dir()
    create_file_copy()

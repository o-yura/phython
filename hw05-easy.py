# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os

for i in range(1, 10):
    dirname = 'dir_' + str(i)
    os.mkdir(dirname)

for i in range(1, 10):
    dirname = 'dir_' + str(i)
    os.rmdir(dirname)

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

for name in os.listdir():
    if os.path.isdir(name):
        print(name)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

from shutil import copyfile

a3_name = (__file__)
a3_copy = a3_name + '_bkp'
copyfile(a3_name, a3_copy)

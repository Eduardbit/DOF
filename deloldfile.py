import os
import datetime
import sys
import colorama

colorama.init(autoreset=True)
CG = colorama.Fore.GREEN
CR = colorama.Fore.RED
CY = colorama.Fore.YELLOW
CW = colorama.Fore.WHITE
SB = colorama.Style.BRIGHT

command = ''


def header():
    os.system('cls')
    print(SB + '*' * 30)
    print(SB + CG + ' ' * 10 + 'DelOldFiles')
    print(SB + '*' * 30 + '\n')


def main_list_command():
    print(SB + CG + '-Команды:')
    print(SB + CY + '\n 1. ' + CW + 'Изменение количества дней, старше которого удаляются файлы')
    print(SB + CY + ' 2. ' + CW + 'Удалять ли файлы за последний день каждого месяца')
    print(SB + CY + ' 3. ' + CW + 'Добавление директории')
    print(SB + CY + ' 4. ' + CW + 'Удаление директории')
    print(SB + CY + ' 5. ' + CW + 'Список ключей')
    print(SB + CY + ' 0. ' + CW + 'Выход\n')


def create_setting_file():
    print(SB + CG + '-Создан новый файл с настройками!')
    print(SB + '\n По умолчанию удаляются файлы старше 360 дней.')
    print(SB + ' Файлы за последний день каждого месяца не удаляются.\n')
    f = open('settings.dat', 'w', encoding='utf-8-sig')
    f.write('360\n')
    f.close()
    current_settings()


def current_settings():
    f = open('settings.dat', 'r', encoding='utf-8-sig')
    setting_str = f.readlines()
    dir_count = 0
    print(SB + CG + '-Текущие настройки:')
    print(SB + CY + '\n OldDays = ' + CW + setting_str[0])
    print(SB + CG + '-Список директорий:')
    if len(setting_str) == 1:
        print(SB + CR + '\n Список директорий пуст')
    else:
        for i in setting_str[1:len(setting_str)]:
            print(SB + ' ' + str(dir_count) + '. ' + CY + i)
            dir_count += 1
    f.close()


header()
main_list_command()
if not os.path.exists('settings.dat'):
    create_setting_file()
else:
    current_settings()
while command != '0':
    command = input(SB + CG + '\n-Введите номер команды: ' + CW)
    if command.strip() == '1':
        f = open('settings.dat', 'r', encoding='utf-8-sig')
        setting_str = f.readlines()
        header()
        print(SB + CG + '-Изменение количества дней, старше которого удаляются файлы')
        print(SB + CG + '-Текущее значение:')
        print(SB + CY + '\n OldDays = ' + CW + setting_str[0])
        f.close()
# list_args = sys.argv
# if len(list_args) > 1:
#     if list_args[1].strip() == '-adddir':
#         dir_path = ''
#         print(SB + CY + '\n-Режим добавления директорий. Для выхода введите "exit"!')
#         while dir_path.lower() != 'exit':
#             dir_path = input('\n Добавление новой директории: ')
#             if dir_path != 'exit':
#                 if os.path.isdir(dir_path):
#                     f = open('settings.dat', 'a', encoding='utf-8-sig')
#                     f.write(dir_path + '\n')
#                     f.close()
#                     print(SB + CG + ' Директория добавлена!')
#                 else:
#                     print(SB + CR + ' Ошибка! Такой директории не существует!')

# main_dir = 'C:\\'
# list_file = os.listdir(main_dir)
# for i in list_file:
#     if os.path.isfile(main_dir + i):
#         file_stat = os.stat(main_dir + i)
#         file_date = datetime.datetime.fromtimestamp(file_stat.st_atime)
#         date_today = datetime.datetime.today()
#         if (date_today - file_date).days > 360:
#             print(i)
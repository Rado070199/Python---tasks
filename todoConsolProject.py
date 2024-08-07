'''
Aplikacja konsolowa - lista to do pozwala dodawać zadania do listy zadań które sa przechowywane w pliku csv.
'''
import logging
import traceback
import csv

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler('application.log'),
        logging.StreamHandler()
    ]
)
def show_tasks():
    try:
        with open('zadania.csv', 'r', newline='', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            return list(csv_reader)
    except Exception as e:
        logging.error(f'Comunicat: {e}')
        logging.error("Traceback:\n%s", traceback.format_exc())
        exit()
    
def add_task(name):
    try:
        list = show_tasks()
        max_id = 0
        
        for task in list:
            task_id = int(task['ID'])
            if task_id > max_id:
                max_id = task_id
    
        new_task = {'ID': f'{max_id+1}', 'Zadanie': f'{name}', 'Status': 'N'}
        list.append(new_task)
        return list

    except Exception as e:
        logging.error(f'Comunicat: {e}')
        logging.error("Traceback:\n%s", traceback.format_exc())
        exit()

def save_file(list):
    try:
        with open('zadania.csv', 'w', newline='', encoding='utf-8') as file:
            fieldnames = ['ID', 'Zadanie', 'Status']
            write = csv.DictWriter(file, fieldnames=fieldnames)           
            write.writeheader()
            write.writerows(list)
    except Exception as e:
        logging.error(f'Comunicat: {e}')
        logging.error("Traceback:\n%s", traceback.format_exc())
        exit()

def main():
    try:
        while True:
            print('-----------------------MENU-------------------------')
            print('1. Wyświetl zadania.')
            print('2. Dodaj zadanie.')
            print('5. Zamknij aplikacje.')
            print('----------------------------------------------------')
            operacja = input('Jaki rodzaj operacji chcesz wykonać (1/2/3/4/5): ')
            
            value = int(operacja)
            
            match value:
                case 1:
                    print('')
                    print('----------------------Lista zadań-------------------------')
                    list = show_tasks()
                    for element in list:
                        print(element)
                    print('----------------------------------------------------------')
                    print('')
                case 2:
                    textNewTask = input('Podaj treść nowego zadania: ')
                    save_file(add_task(textNewTask))
                case 5:
                    exit()
                case _:
                    print("Taka opcja nie istnieje !")
    except Exception as e:
        logging.error(f'Comunicat: {e}')
        logging.error("Traceback:\n%s", traceback.format_exc())
        exit()
            
if __name__ == "__main__":
    main()
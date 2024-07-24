import os

def add_expense(expenses):
    name = input('Введите названия расхода: ')
    amount = float(input('Введите сумму расхода: '))
    expenses.append((name, amount))
    print('Запись добавлена!')

def displey(expenses):
    if not expenses:
        print('Нет записей о расходах!')
        return
    for i, (name, amount) in enumerate(expenses, 1):
        print(f'{i}. {name}: {amount} $')

def delete_expense(expenses):
    displey(expenses)
    if not expenses:
        return

    index = int(input('Введите номер записи который вы хотите удалить: ')) - 1
    if 0 <= index < len(expenses):
        delete_expense = expenses.pop(index)
        print(f"Запись '{delete_expense[0]}' удалена успешно!")
    else:
        print('Неверный номер записи!')

def total_expense(expenses):
    total = sum(amount for _, amount in expenses)
    print(f'Общий расход составляет: {total} $')

def load_filename(filename):
    if not os.path.exists(filename):
        return []
    with open(filename, 'r') as file:
        expenses = [line.strip().split(',') for line in file.readlines()]
        return [(name, float(amount)) for name, amount in expenses]

def save_expense(filename, expenses):
    with open(filename, 'w') as file:
        for name, amount in expenses:
            file.write(f'{name}, {amount}\n')

def main():
    filename = 'expenses.txt'
    expenses = load_filename(filename)

    while True:
        print("\nКалькулятор расходов")
        print("1. Добавить запись о расходе")
        print("2. Просмотреть все записи о расходах")
        print("3. Удалить запись о расходе")
        print("4. Подсчитать общий расход")
        print("5. Сохранить и выйти")
        choice = input('Выберите действие: ')

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            displey(expenses)
        elif choice == "3":
            delete_expense(expenses)
        elif choice == "4":
            total_expense(expenses)
        elif choice == "5":
            save_expense(filename, expenses)
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()


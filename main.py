import database


def character_count(voyage):
    count = 0
    for _ in voyage:
        count += 1
    return count


def converting_characters_to_uppercase(symbols, amount_symbols):
    number_symbol_flight = 0
    number_symbol_dictionary = 0
    count = 0
    symbols_in_upper_case = ''

    while True:
        if symbols[number_symbol_flight] in lower_letters:
            if symbols[number_symbol_flight] != lower_letters[number_symbol_dictionary]:
                number_symbol_dictionary += 1
            else:
                symbols_in_upper_case += capital_letters[number_symbol_dictionary]
                number_symbol_flight += 1
                number_symbol_dictionary = 0
                count += 1
        else:
            symbols_in_upper_case += symbols[number_symbol_flight]
            number_symbol_flight += 1
            count += 1
            number_symbol_dictionary = 0
        if count == amount_symbols:
            break
    symbols = symbols_in_upper_case
    return symbols


def string_length_check(voyage, amount_symbols, error_text, invitation_text):
    while True:
        count = 0
        for _ in voyage:
            count += 1
        if count != amount_symbols:
            print(error_text)
            voyage = input(invitation_text)
        else:
            return voyage


lower_letters = 'abcdefghijklmnopqrstuvwxyz'
capital_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

print('Сервис поиска авиабилетов')
while True:
    print('\nГлавное меню:\n\n1 - ввод рейса\n'
          '2 - вывод всех рейсов\n3 - поиск рейса по номеру\n0 - завершение работы\n')

    choice_user = int(input('Введите номер пункта меню: '))
    if choice_user == 1:
        print('\nВведите данные рейса:')
        number_flight = input('XXXX - номер рейса: ')
        string_length_check(number_flight, 4,
                            'Неверный номер рейса. Он должен состоять из четырех символов', 'XXXX - номер рейса: ')
        flight_number_in_upper_case = converting_characters_to_uppercase(number_flight, 4)

        date_voyage = input('ДД/ММ/ГГГГ - дата рейса: ')
        string_length_check(date_voyage, 10,
                            'Некорректный ввод даты. Она должен состоять из десяти символов', 'ДД/ММ/ГГГГ - дата рейса: ')

        time_flying_away = input('ЧЧ:ММ - время вылета: ')
        string_length_check(time_flying_away, 5,
                            'Некорректный ввод времени. Оно должно состоять из пяти символов', 'ЧЧ:ММ - время вылета: ')

        flight_time = input('XX.XX - длительность перелета: ')
        while True:
            character_count_check = character_count(flight_time)
            if flight_time[0] == '-':
                print('Некорректный ввод длительности перелета. Длительность не может быть отрицательным числом')
            elif character_count_check != 5:
                print('Некорректный ввод длительности перелета. Должна быть пара двузначных чисел разделенных точкой')
                flight_time = input('XX.XX - длительность перелета: ')
            elif flight_time[1] == '0' and flight_time[3] == '0':
                print('Некорректный ввод длительности перелета. Длительность не может быть равна нулю')
                flight_time = input('XX.XX - длительность перелета: ')
            else:
                break

        starting_airport = input('XXX - аэропорт вылета: ')
        while True:
            character_count_check = character_count(starting_airport)
            if character_count_check != 3:
                print('Неверный ввод аэропорта вылета. Он должен состоять из трех символов')
                starting_airport = input('XXX - аэропорт вылета: ')
            else:
                break

        starting_airport_in_upper_case = converting_characters_to_uppercase(starting_airport, 3)

        final_airport = input('XXX - аэропорт назначения: ')
        while True:
            character_count_check = character_count(final_airport)
            if character_count_check != 3:
                print('Неверный ввод аэропорта назначения. Он должен состоять из трех символов')
                final_airport = input('XXX - аэропорт назначения: ')
            else:
                break

        final_airport_in_upper_case = converting_characters_to_uppercase(final_airport, 3)

        flight_cost = float(input('.XX - стоимость билета (> 0): '))
        while True:
            if flight_cost < 0:
                print('Некорректный ввод стоимости билета. Стоимость не может быть отрицательным числом')
                flight_cost = float(input('.XX - стоимость билета (> 0): '))
            else:
                break

        information_specific_flight = database.select_flight(number_flight)
        if information_specific_flight:
            for data in information_specific_flight:
                print('\nРейс с таким номером уже существует:')
                print(f'Информация о рейсе: {data[0]} {data[1]} {data[2]} {data[3]} '
                      f'{data[4]} {data[5]} {data[6]}')
        else:
            database.insert_users(flight_number=flight_number_in_upper_case, flight_date=date_voyage,
                                  aircraft_departure_time=time_flying_away, flight_duration=flight_time,
                                  departure_airport=starting_airport_in_upper_case,
                                  destination_airport=final_airport_in_upper_case, ticket_price=flight_cost)
            print(f'\nИнформация о рейсе {flight_number_in_upper_case} {date_voyage} {time_flying_away} {flight_time} '
                  f'{starting_airport_in_upper_case} {final_airport_in_upper_case} {flight_cost}* добавлена')

    elif choice_user == 2:
        flight_info = database.all_flights()
        if not flight_info:
            print('Информация о рейсах отсутствует')
        else:
            for flight in flight_info:
                print(f'Информация о рейсе: {flight[0]} {flight[1]} {flight[2]} {flight[3]} '
                      f'{flight[4]} {flight[5]} {flight[6]}')

    elif choice_user == 3:
        number_flight = input('Введите номер рейса в формате XXXX: ')
        while True:
            character_count_check = character_count(number_flight)
            if character_count_check != 4:
                print('Неверный номер рейса. Он должен состоять из четырех символов')
                number_flight = input('Введите номер рейса в формате XXXX: ')
            else:
                break

        flight_number_in_upper_case = converting_characters_to_uppercase(number_flight, 4)

        information_specific_flight = database.select_flight(number_flight)
        if not information_specific_flight:
            print(f'Рейс {number_flight} не найден')
        else:
            for data in information_specific_flight:
                print(f'Информация о рейсе: {data[0]} {data[1]} {data[2]} {data[3]} '
                      f'{data[4]} {data[5]} {data[6]}')

    elif choice_user == 0:
        break

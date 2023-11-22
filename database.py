import sqlite3


def create_db():
    """
    Метод описывающий создание базы данных и таблицы в ней
    :return: None
    """
    connection = sqlite3.connect("scroll_flights.sqlite3")
    cursor = connection.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS Flights (id INTEGER PRIMARY KEY, flight_number TEXT NOT NULL, flight_date "
        "TEXT NOT NULL, aircraft_departure_time TEXT NOT NULL, flight_duration TEXT NOT NULL, "
        "departure_airport TEXT NOT NULL, destination_airport TEXT NOT NULL, ticket_price INTEGER NOT NULL);")
    connection.commit()
    cursor.close()


def _execute_query(query, select=False):
    """
    Метод описывающий создание курсора который делает запросы и получает их результаты
    :return: Any
    """
    create_db()
    connection = sqlite3.connect("scroll_flights.sqlite3")
    cursor = connection.cursor()
    cursor.execute(query)
    if select:
        records = cursor.fetchall()
        if records is None:
            return False
        else:
            cursor.close()
            return records
    else:
        connection.commit()
    cursor.close()


def insert_users(flight_number: str = None, flight_date: str = None,
                 aircraft_departure_time: str = None, flight_duration: str = None,
                 departure_airport: str = None, destination_airport: str = None,
                 ticket_price: float = 0.0):
    """
    Метод описывающий добавление информации о рейсе в таблицу базы данных
    :return: None
    """
    insert_query = "INSERT INTO Flights (flight_number, flight_date, aircraft_departure_time, flight_duration, " \
                   "departure_airport, destination_airport, ticket_price)" f"VALUES ('{flight_number}', " \
                   f"'{flight_date}', '{aircraft_departure_time}', '{flight_duration}', '{departure_airport}', " \
                   f"'{destination_airport}', '{ticket_price}')"
    _execute_query(insert_query)


def all_flights():
    """
    Метод описывающий список всех рейсов в таблице базы данных
    :return: Any
    """
    select_query = "SELECT flight_number, flight_date, aircraft_departure_time, flight_duration, " \
                   "departure_airport, destination_airport, ticket_price FROM Flights WHERE EXISTS (SELECT * FROM " \
                   "Flights)"

    record = _execute_query(select_query, select=True)
    return record


def select_flight(flight_number: str):
    """
    Метод описывающий конкретный рейс в таблице базы данных
    :return: Any
    """
    select_query = f"SELECT flight_number, flight_date, aircraft_departure_time, flight_duration, " \
                   f"departure_airport, destination_airport, ticket_price " \
                   f"FROM Flights " \
                   f"WHERE flight_number = '{flight_number}'"

    record = _execute_query(select_query, select=True)
    return record


def select_flight_all(id_flight):
    """
    Метод описывающий конкретный рейс в таблице базы данных
    :return: Any
    """
    select_query = f"SELECT flight_number, flight_date, aircraft_departure_time, flight_duration, " \
                   f"departure_airport, destination_airport, ticket_price " \
                   f"FROM Flights " \
                   f"WHERE id = '{id_flight}'"

    record = _execute_query(select_query, select=True)
    return record

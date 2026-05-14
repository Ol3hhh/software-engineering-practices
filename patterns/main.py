from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def request_data(self):
        pass

class RealDatabase(Database):
    def request_data(self):
        print("Otrzymano tajne dane")

class ProxyDatabase(Database):
    def __init__(self, password: str):
        self._password = password
        self._real_db = None  

    def request_data(self):
        if self._password == "1234":
            if self._real_db is None:
                self._real_db = RealDatabase()
            self._real_db.request_data()
        else:
            print("Dostęp zabroniony")

if __name__ == "__main__":
    while True:
        user_input = input("Podaj hasło: ")
            
        proxy = ProxyDatabase(str(user_input))
        proxy.request_data()
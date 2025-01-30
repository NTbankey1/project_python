from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass

class MySQLDatabase(Database):
    def connect(self):
        return "Kết nối MySQL"

    def disconnect(self):
        return "Ngắt kết nối MySQL"

class PostgreSQLDatabase(Database):
    def connect(self):
        return "Kết nối PostgreSQL"

    def disconnect(self):
        return "Ngắt kết nối PostgreSQL"

class SQLiteDatabase(Database):
    def connect(self):
        return "Kết nối SQLite"

    def disconnect(self):
        return "Ngắt kết nối SQLite"

# Sử dụng
db1 = MySQLDatabase()
db2 = PostgreSQLDatabase()
db3 = SQLiteDatabase()

print(db1.connect())  # ✅ Kết nối MySQL
print(db2.connect())  # ✅ Kết nối PostgreSQL
print(db3.connect())  # ✅ Kết nối SQLite

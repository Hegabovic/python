from databaseConnector import DatabaseConnector


class Employee:
    def __init__(self, emp_id, emp_name, emp_is_manager):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_is_manager = emp_is_manager


class EmployeeHandler:

    @staticmethod
    def get_all_employees():
        db = DatabaseConnector('localhost', 'python_lab2', 'hegabovic', 'Hegabo192').establish_connection()
        cursor = db.cursor()
        cursor.execute("select * from employees")
        data_from_db = cursor.fetchall()
        DatabaseConnector.close_connection(cursor, db)
        return data_from_db

    @staticmethod
    def get_employee(emp_id):
        sql = "select * from employees where emp_id= '%s' "
        db = DatabaseConnector('localhost', 'python_lab2', 'hegabovic', 'Hegabo192').establish_connection()
        cursor = db.cursor()
        cursor.execute(sql, (emp_id,))
        data_from_db = cursor.fetchone()
        DatabaseConnector.close_connection(cursor, db)
        return data_from_db

    @staticmethod
    def add_employee(name, is_manager):
        sql = "Insert Into employees(emp_name, emp_is_manager) Values(%s,%s)"
        db = DatabaseConnector('localhost', 'python_lab2', 'hegabovic', 'Hegabo192').establish_connection()
        cursor = db.cursor()
        cursor.execute(sql, (name, is_manager))
        db.commit()
        DatabaseConnector.close_connection(cursor, db)

    @staticmethod
    def delete_employee(emp_id):
        sql = "delete * from employees where emp_id= '%s' "
        db = DatabaseConnector('localhost', 'python_lab2', 'hegabovic', 'Hegabo192').establish_connection()
        cursor = db.cursor()
        cursor.execute(sql, (emp_id,))
        data_from_db = cursor.fetchone()
        DatabaseConnector.close_connection(cursor, db)
        return data_from_db


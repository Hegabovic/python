from Person import Person
import re


class Employee(Person):
    def __init__(self, fullname="", money=0, sleep_mood="", health_rate=0, employee_id=0, email='', work_mood=0,
                 salary=0, is_manager=False):
        super().__init__(fullname, money, sleep_mood, health_rate)
        self.employee_id = employee_id
        self.email = email
        self.work_mood = work_mood
        self.salary = salary
        self.is_manager = is_manager

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary):
        if salary > 1000:
            self._salary = salary
        else:
            print('enter salary above 1000')

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self.check_mail(email)

    @property
    def health_rate(self):
        return self.health_rate

    @health_rate.setter
    def set_health_rate(self, health_rate):
        if health_rate < 100 & health_rate > 0:
            self.set_health_rate(health_rate)

    def send_email(self):
        to = input("enter your receiver email : ")
        sender = input("enter your email : ")
        subject = input("enter email subject : ")
        body_content = input('enter your mail content : ')
        receiver_name = input('enter receiver name : ')
        data = f'to: {to} \n' \
               f'from: {sender}\n' \
               f'subject: {subject}\n\n' \
               f'{body_content}\n\n' \
               f'receiver:{receiver_name}'
        file = open('mail.txt', 'w')
        file.write(data)

    def work(self, hours):
        if hours > 0:
            if hours > 8:
                print('tired employee')
            elif hours < 8:
                print('lazy employee')
            else:
                print('happy employee')
        else:
            print('enter a valid hours')

    def check_mail(self, email):
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if re.search(regex, email):
            self._email = email
        else:
            print('not valid mail')


# x = Employee('abdullah', 2000, 'happy', 40, 10, 'abdallah@gmail.com', 10, 2000, True)
# x.send_email()

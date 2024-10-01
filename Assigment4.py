# # #1.Write a Python program to create a class named Car. Define attributes like brand, model, and year.
# # #Create an object of the class and display the details of the car?
# #
# # class car:
# #    def __init__(self,brand,model,year):
# #     self.brand=brand
# #     self.model=model
# #     self.year=year
# # my_car = car("Tata", "Naxon", 2022)
# #
# # print(f"Car Details: Brand: {my_car.brand}, Model: {my_car.model}, Year: {my_car.year}")
#
# #2. Create a class Student with attributes name, roll_number, and marks.
# # Define a constructor to initialize these attributes and a method display_info() to print the student's details?
#
# # class student:
# #     def __init__(self,name, roll_number, marks):
# #         self.name = name
# #         self.roll_number = roll_number
# #         self.marks = marks
# #
# #     def display_info(self):
# #         print(f" Name:{self.name}, Roll number:{self.roll_number}, Marks:{self.marks}")
# # # Creating an object of the Student class
# #
# # student1 = student("Asim", 1001, 85)
# #
# # # Displaying the student's details
# # student1.display_info()
# # #
#
# #3. Create a class Rectangle with attributes length and breadth. .
# # Include methods to calculate the area and perimeter of the rectangle.
# # Create multiple objects and display the area and perimeter for each?
#
# # class Rectangle:
# #     def __init__(self,length,breadth):
# #         self.length =length
# #         self.breadth =breadth
# #     def calculate_area(self):
# #         return self.length * self.breadth
# #     def calculate_perimeter(self):
# #         return 2*(self.length+self.breadth)
# #
# # rectangle1 = Rectangle(10, 3)
# # rectangle2 = Rectangle(11, 6)
# #     # Displaying area and perimeter for rectangle1
# # print(f"Rectangle 1 - Area: {rectangle1.calculate_area()}, Perimeter: {rectangle1.calculate_perimeter()}")
# #
# #     # Displaying area and perimeter for rectangle2
# # print(f"Rectangle 2 - Area: {rectangle2.calculate_area()}, Perimeter: {rectangle2.calculate_perimeter()}")
#
# #4. Write a class Circle with an attribute radius and methods get_area() and get_circumference().
# # These methods should return the area and circumference of the circle, respectively ?
#
#
# # import math
# # class Circle:
# #     def __init__(self,radius):
# #         self.radius =radius
# #     def get_area(self):
# #         return math.pi*(self.radius**2)
# #     def get_circumference(self):
# #         return 2*math.pi*self.radius
# #
# # if __name__ == "__main__":
# #         circle = Circle(5)
# #         print("Area:", circle.get_area())
# #         print("Circumference:", circle.get_circumference())
#
# # 5. Create Account class with 2 attributes - balance & account no. Create methods for debit, credit & printing the balance.
#
# #
# # class Account:
# #     def __init__(self,account_no,balance=0):
# #         self.account_no=account_no # Account number
# #         self.balance=balance  # Initial balance
# #     def debit(self,amount):
# #         """Withdraw amount from the account, if sufficient balance exists."""
# #         if amount>self.balance:
# #             print("Insufficient balance for debit.")
# #         else:
# #             self.balance-=amount
# #             print(f"Debited {amount}. New balance: {self.balance}")
# #     def credit(self,amount):
# #         """Deposit amount to the account."""
# #         self.balance+=amount
# #         print(f"Credited {amount}. New balance: {self.balance}")
# #
# #     def print_balance(self):
# #         """Print the current balance of the account."""
# #         print(f"Account No: {self.account_no}, Balance: {self.balance}")
# #
# #     # Example usage:
# #
# # if __name__ == "__main__":
# #     account = Account('123456', 1000)
# #     account.print_balance()
# #     account.credit(500)
# #     account.debit(300)
# #     account.debit(1500)
# #     account.print_balance()
#
# #7. Create a class Book with attributes title, author, and price.
# # Write a constructor that allows the user to either initialize all three attributes or just the title and author (in which case the price should be set to a default value).
# # Display the details of the book using an instance method.
# #
# #
# # class Book:
# #     def __init__(self,title, author, price=0.0):
# #
# # # Constructor to initialize title, author, and optionally price (default value: 0.0)
# #        self.title = title
# #        self.author = author
# #        self.price = price
# #     def display_details(self):
# #         # Method to display the details of the book
# #         print(f"Tittle:{self.title}")
# #         print(f"Author:{self.author}")
# #         print(f"Price:{self.price}")
# #         # Example usage:
# #
# #         # Initializing with title and author, price will take the default value (0.0
# #
# # book1 = Book("Harry Potter", "J. K. Rowling")
# # book1.display_details()
# # print()
# #
# # # Initializing with title, author, and price
# # book2 = Book("1997", "J. K. Rowling", 15.99)
# # book2.display_details()
#
#
#
# #6. Create a class Employee with an attribute employee_count (class variable) and a class method increment_employee_count() to increase the count whenever a new employee object is created.
# # Show the updated employee count after creating new objects.
# #
# # class Employee:
# #     # Class variable to keep track of employee count
# #     employee_count = 0
# #
# #     def __init__(self, name):
# #         self.name = name
# #         # Increment employee count when an Employee object is created
# #         Employee.increment_employee_count()
# #
# #     @classmethod
# #     def increment_employee_count(cls):
# #         # Increment the class-level employee_count
# #         cls.employee_count += 1
# #         cls.show_employee_count()
# #
# #     @classmethod
# #     def show_employee_count(cls):
# #         # Display the current employee count
# #         print(f"Updated Employee Count: {cls.employee_count}")
# #
# # # Example usage:
# #
# # # Creating new employee objects
# # employee1 = Employee("Anuj")
# # employee2 = Employee("Navin")
# # employee3 = Employee("Anil")
#
#
# #8. Write a class TemperatureConverter with an instance method celsius_to_fahrenheit(celsius) that takes a temperature in Celsius and returns its Fahrenheit equivalent.
# # Create an object of the class and use the method to convert various temperatures.
# #
# # class TemperatureConverter:
# #     def celsius_to_fahrenheit (self,celsius):
# #         # Formula to convert Celsius to Fahrenheit
# #         fahrenheit =(celsius * 9/5) + 32
# #         return fahrenheit
# #
# # # Example usage:
# #
# # # Create an object of TemperatureConverter
# # converter =TemperatureConverter()
# # temp_in_fahrenheit_1 = converter.celsius_to_fahrenheit(0)  # Freezing point of water
# # temp_in_fahrenheit_2 = converter.celsius_to_fahrenheit(100)  # Boiling point of water
# # temp_in_fahrenheit_3 = converter.celsius_to_fahrenheit(37)  # Human body temperature
# # # Display results
# # print(f"0°C in Fahrenheit: {temp_in_fahrenheit_1}°F")
# # print(f"100°C in Fahrenheit: {temp_in_fahrenheit_2}°F")
# # print(f"37°C in Fahrenheit: {temp_in_fahrenheit_3}°F")
# #
# #
# # 9. Create a class Time with attributes hours and minutes.
# # Add a method add_time() that takes another Time object, adds its values to the current object, and returns a new Time object with the resulting sum.
#
# class Time:
#     def __init__(self,hours,minutes,):
#         self.hours=hours
#         self.minutes=minutes
#     def add_time(self,other_time):
#         # Add the minutes and hours separately
#         total_minutes=self.minutes+other_time.minutes
#         total_hours=self.hours+other_time.hours
# # If total minutes are 60 or more, convert to hours
#         extra_hours=total_minutes//60
#         remaining_minutes = total_minutes % 60
#         # Add extra hours to total hours
#         final_hours = total_hours + extra_hours
# # Return a new Time object with the resulting hours and minutes
#         return Time(final_hours, remaining_minutes)
#
#     def display_time(self):
#             # Display the time in "HH:MM" format
#         print(f"Time: {self.hours} hours and {self.minutes} minutes")
#
#     # Example usage:
#
#     # Create two Time objects
# time1 = Time(2, 50)  # 2 hours and 50 minutes
# time2 = Time(1, 30)  # 1 hour and 30 minutes
#
#     # Add the times
# result_time = time1.add_time(time2)
#
#     # Display the result
# result_time.display_time()  # Output: 4 hours and 20 minutes
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#

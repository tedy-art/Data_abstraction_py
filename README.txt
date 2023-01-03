What is abstraction??
->  abstraction in python is defined as a process of heading complixity by hiding  unnesccessary information from the user,


** How to create abstract class
->  By using abc module
->  abc means abstract base class
->  abc module contains ABC class and by using ABC class we can create abstract class

synatx :- 
    from abc import ABC:

    class class_name(ABC):
        methods
        non abstract methods + abstract methods
    
NOTE :- 
    WE CON NOT CREATE OBJECT OF ABSTRACT CLASS.

** How to create abstract methods..??
->  by using @abstractmethod
->  abstract methods are those which are not having any implementation(pass).

syntax:-

    from abc import ABC:

    class class_name(ABC):
        @abstractmethod
        def method_name(self):
            pass

e.g.

    from abc import ABC, abstractmethod

    class CAR(ABC):
        @abstractmethod
        def engine_cc(self):
            pass

        @abstractmethod
        def mailage(self):
            pass

        @abstractmethod
        def price(self):
            pass

        def no_of_wheels(self):
            print("all cars in this category are 4 wheelers")

    class TATA(CAR):
        def engine_cc(self):
            print("Engin cc is 1200.")

        def mailage(self):
            print("Mailage is 20 km/lts.")

        def price(self):
            print("12 lakhs.")

        def ground_clearance(self):
            print("20 inchs.")

    nexon = TATA()
    nexon.engine_cc()
    nexon.mailage()
    nexon.price()
    nexon.ground_clearance()
    nexon.no_of_wheels()

o/p:

    Engine cc is 1200.
    Mailage is 20 km/lts.
    12 lakhs.
    20 inchs.
    all cars in this category are 4 wheelers


2) Interface
It is abstract class with all abstract methods.
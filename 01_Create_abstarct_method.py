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
        print("Engine cc is 1200.")

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
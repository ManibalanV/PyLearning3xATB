from abc import ABC, abstractmethod
class PyATB(ABC):


    @abstractmethod
    def payFee(self):
        pass

    def enrolled(self):
        print('Enrolled')


class Shubam(PyATB):
    def payFee(self):
        print("Paid")


shubam = Shubam()
shubam.enrolled()

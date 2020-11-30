import pickle

class Array:
    count = 0
    def __init__(self, element):
        self.element = element
        Array.count += 1
    def display_element(self):
        print('Element number:', self.element)
class Main:
    def serialization(self):
        with open('data.pkl', 'wb') as f:
            pickle.dump(Array, f)
        with open('data.pkl', 'rb') as f:
            data_new = pickle.load(f)
        print(data_new)
    def addNum(self, array):
        result = 0
        for element in array:
            result += element.element
        return result
    def subtraction(self, array):
        result = array[0].element * 2
        for element in array:
            result -= element.element
        return result
    def multiplication(self, array):
        result = 1
        for element in array:
            result *= element.element
        return result

    def main(self):
        array = [Array(7),
                 Array(9),
                 Array(11)]
        array[1].display_element()
        print(self.addNum(array))
        print(self.subtraction(array))
        print(self.multiplication(array))
        self.serialization()
if __name__== "__main__":
    main = Main()
    main.main()

class Array:
    count = 0
    def __init__(self, element):
        self.element = element
        Array.count += 1
    def display_element(self):
        print('Element number:', self.element)
class Main:
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
        #print(array[0].element)
if __name__== "__main__":
    main = Main()
    main.main()

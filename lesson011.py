class BMI:
    def calculateBmi(self):
        print("Enter your weight in KG: ")
        self.weight = float(input())
        print("Enter your height in meters: ")
        self.height = float(input())

        self.bmi = self.weight / (self.height * self.height)

        print("Your BMI is: ", self.bmi)

        if self.bmi < 18.5:
            print("You are underweight.")
        elif self.bmi >= 18.5 and self.bmi < 25:
            print("You are healthy.")
        elif self.bmi >= 25 and self.bmi < 30:
            print("You are overweight.")
        elif self.bmi >= 30:
            print("You are obese.")



bmi = BMI()

while True:
    print("1. Calculate Your BMI")
    print("2. Exit")

    choice = int(input())

    if choice == 1:
        bmi.calculateBmi()
    elif choice == 2:
        exit()


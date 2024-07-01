height = input( "Enter your height ")
Weight = input( "Enter your weight ")
height_as_int = int(height)
weight_as_float = float(Weight)
bmi = weight_as_float / height_as_int ** 2
print("Your BMI is " + str(bmi))
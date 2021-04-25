# Alex Harvey, 4/11/2021, file name HealthCalculator.py
# This will ask user for information to use to calculate BMI
# Ask user for input
from decimal import Decimal
print ('Please enter the following values for the user...')
height = int(input('Height in inches: '))
weight = int(input('Weight in pounds: '))
age = int(input('Current age: '))
restingHeart = int(input('Resting hart rate: ')) 
convertHeight = height * .0254
convertWeight = weight * .453592



# show the results displaying BMI and what category they are in
print ('Results...')
bmi = convertWeight / convertHeight ** 2
#print(f'Your BMI is: {bmi:.2f} --')

if bmi <= 18.5:
    print(f'Your BMI is: {bmi:.2f} -- Underweight')
elif bmi >= 18.5 and bmi <= 24.9:
    print(f'Your BMI is: {bmi:.2f} -- Normal weight')
elif bmi >= 25 and bmi <= 29.9:
    print(f'Your BMI is: {bmi:.2f} -- Overweight')
elif bmi >= 30:
    print(f'Your BMI is: {bmi:.2f} -- Obese')
    
print('Exercise Intensity Heart Rates:')
print('Intensity {: >15}' .format ('Max Heart Rate'))
inteRange=Decimal(.96)
intes= Decimal(.50)

for inteRange in range(50,96,5):
    
    max_heart_rate = ((220-age-restingHeart)*intes+restingHeart)
    print(f'{intes: .2f}{" ":>10}{max_heart_rate: .0f}')
    #print(int(((220 - age)- restingHeart) * intes) + restingHeart)
    intes += Decimal(.05)

#Parts 1 and 2

inches = input("What is your Height in Inches");
weight = input("What is your weight in pounds");

inches = int(inches);
weight = int(weight);

def bmi(inches, weight):

    if inches == 0:
       print("Inches Must Not Equal Zero")
    elif inches != 0:
       pbmi = (weight/(inches*inches));
       pbmi=str(pbmi);
       print("Your BMI is: " + pbmi);

bmi(inches, weight);


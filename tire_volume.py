#Work CSE111
#By Hannah Ramirez
#We need to calculate the volume of a car tire 

#ask for the data to the user
width = int(input("Enter the width of the tire in mm (ex 205): "))
aspect_ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))

#Calculate the volume of the tire
volume = (3.14159 * width**2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000000

#Show the result to the user
print(f"The volume of the tire is {volume:.2f} liters.")
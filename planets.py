def weight_on_planets():
   weight = int(input("What do you weigh on earth? "))
   marsweight = weight * 0.38
   jupweight = weight * 2.34
   print("\nOn Mars you would weigh", marsweight, "pounds.\nOn Jupiter you would weigh", jupweight, "pounds.")
   
if __name__ == '__main__':
   weight_on_planets()

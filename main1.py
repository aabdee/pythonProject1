

def main():

   num=int(input("Introdueix un número natural: "))

   while num < 1:
      num=int(input("Error. Vuelve a introducir un valor natural: "))
   i=0
   sum=0

   while sum+i < num:
      sum = sum+i
      print("El número és:",i)
      i+=1
   print("Y la suma total és: ", sum)

if __name__ == '__main__':
   main()


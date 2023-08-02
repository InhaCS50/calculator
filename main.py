while True:
     print("Assalomu aleykum !!")
     print("Calculator app !!")
     # Add Numbers
     print("qo'shish uchun ['add'] ni bosing")
     # Subtract Numbers
     print("ayirish uchun ['subtract'] ni bosing")
     # Multiply Numbers
     print("ko'paytirish uchun ['multiply'] ni bosing")
     # Divide Numbers
     print("bo'lish uchun ['divide'] ni bosing")
     # Quiting Program
     print("chiqish uchun ['quit'] ni bosing")
     user_input = input("yozing: ")
     if user_input == "quit":
          print("chiqish")
          break
     elif user_input == "add":
          num1 = float(input("birinchi raqamni kiriting >> "))
          num2 = float(input("ikkinchi raqamni kiriting >> "))
          result = str(num1 + num2)
          print("javob >>> "+ result)
     elif user_input == "subtract":
          num1 = float(input("birinchi raqamni kiriting >> "))
          num2 = float(input("ikkinchi raqamni kiriting >> "))
          result = str(num1 - num2)
          print("javob >>> "+ result)
     elif user_input == "multiply":
          num1 = float(input("birinchi raqamni kiriting >> "))
          num2 = float(input("ikkinchi raqamni kiriting >> "))
          result = str(num1 * num2)
          print("javob >>> "+ result)
     elif user_input == "divide":
          num1 = float(input("birinchi raqamni kiriting >> "))
          num2 = float(input("ikkinchi raqamni kiriting >> "))
          result = str(num1 / num2)
          print("javob >>> "+ result)
     else: 
          print("xato")

while True:
     print("Assalomu aleykum !!")
     print("Calculator app !!")
     print("qo'shish uchun ['add'] ni bosing")
     print("ayirish uchun ['subtract'] ni bosing")
     print("ko'paytirish uchun ['multiply'] ni bosing")
     print("bo'lish uchun ['divide'] ni bosing")
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

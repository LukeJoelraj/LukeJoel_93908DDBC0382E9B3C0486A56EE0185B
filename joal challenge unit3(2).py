class BankAccount:
  def __init__(r::
rmat(student.name# Program to perform linear search and display the index of target in a list if found
     def linear_search_product(productList, target_product):
       indices=[]
       for i,p in enumerate(productList):
         if p == target_product:
           indices.append(i)
       return indices

     products = ["leather", "jacket", "overcoat", "jean","jacket", "rain coat", "trench coat","fleece","jacket"]
     print(products)
     target1 = "Coat"
     target = input("Enter the target item in the list:")
     result= linear_search_product(products,target)

     print("When Target is found: ")
     print(result)


     print("\nWhen Target is not found: ")

     result1= linear_search_product(products,target1)
     print(result1)student.roll_nu
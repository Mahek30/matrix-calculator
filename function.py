
import numpy as np

#function to take matrix input from the user
def input_matrix (rows, cols,name):
    print(f"Enter the elements for {name} matrix ({rows}x{cols}): ")
    matrix=[]
    for i in range(rows):
          while True:
                try:
                     row_input = input(f"Row {i+1}. (enter {cols} elements): ").split()
                     if len(row_input)!=cols:
                         print("Invalid no. of inputs. Try again.")
                         continue
                     row = list(map(float,row_input)) 
                     matrix.append(row)
                     break
                except ValueError:
                     print("Invalid Input! Please enter only numbers")
    return np.array(matrix)   



def addition(A,B):
     return A+B 
def subtraction(A,B):
    return A-B
def multiply(A,B):
     try:
          return A@B  #or np.dot(A,B)
     except ValueError:
          return "ERROR - Incompatible matrix sizes for multiplication."
def transpose(A):
     return A.T
def inverse(A):
     if np.linalg.det(A)==0:
          return "Matrix is singular (determinant is zero). Inverse not possible."
     try:
          return np.linalg.inv(A)
     except np.linalg.LinAlgError:
          return "ERROR: Matrix not invertible."
def determinant(A):
     try:
          return np.linalg.det(A)
     except np.linalg.LinAlgError:
          return "Error calculating the determinant."

def rank(A):
    return np.linalg.matrix_rank(A)

def eigen(A):
     try:
        value, vectors = np.linalg.eig(A)
        return value, vectors
     except np.linalg.LinAlgError:
          return None, "ERROR: Cannot compute eigenvalues."

          
#Display Menu
def show_menu():
     print("\n Choose the operation: ")
     print("\n 1. Addition [+]")
     print("\n 2. Subtraction [-]")
     print("\n 3. Multiplication [*]")
     print("\n 4. Transpose [']")
     print("\n 5. Inverse Matrix ")
     print("\n 6. Determinant of Matrix ")
     print("\n 7. Rank of a Matrix")
     print("\n 8. Eigen Values & Eigen Vectors.")
     print("\n 9. Enter new values of matrices. ")
     print("\n 0. Exit")

#MAIN CODE ---------------------------------

print ("Matrix Calculator")

#Take first matrix input from user 
rows1 = int(input("Enter the number of rows for first matrix: "))
cols1 = int(input("Enter the number of columns for first matrix: "))
A = input_matrix(rows1,cols1, "first" )

#Take second matrix input from user 
rows2 = int(input("Enter the number of rows for second matrix: "))
cols2 = int(input("Enter the number of columns for second matrix: "))
B = input_matrix(rows2, cols2, "second")



while True:
        show_menu()
        choice = input("\n Enter your choice (operation number): ")

        if choice == "1":
            if A.shape==B.shape:
                print(f"\n Result of addition: \n {addition(A,B)}")
            else:
                print("ERROR: Cannot add matrices with different dimensions")

        elif choice == "2":
            if A.shape==B.shape:
                print(f"\n Result of subtraction: \n {subtraction(A,B)}")
            else:
                print("ERROR: Cannot subtract matrices with different dimensions")

        elif choice == "3":
            if A.shape[1]==B.shape[0]:
                print(f"\n Result of multiplication: \n {multiply(A,B)}")
            else:
                print("ERROR: Cannot multiply - columns of first matrix must be equal to rows in second matrix")
        
        elif choice == "4":
             target = input("\n Transpose of which matrix? (A or B): ").strip().upper()
             if target== "A":
                  print(f"\n Transpose of A is: \n {transpose(A)}")
             elif target =="B":
                  print(f"\n Transpose of B is: \n {transpose(B)}")
             else:
                  print("Not valid choice. Please enter A or B")

        elif choice == "5":
             target = input("\n Inverse of which matrix? (A or B): ").strip().upper()
             if target=="A":
                  if A.shape[0]== A.shape[1]:
                       print(f"\n Inverse of A: \n {inverse(A)}")
                  else:
                       print("Matrix A is not square matrix. Inverse not possible.")
             elif target=="B":
                  if B.shape[0]== B.shape[1]:
                       print(f"\n Inverse of B: \n {inverse(B)}")
                  else:
                       print("Matrix B is not square matrix. Inverse not possible.")
             else:
                  print("Invalid choice. Please enter A or B.")
      
        elif choice == "6":
             target = input("\n Determinant of which matrix? (A or B): ").strip().upper()
             if target == "A":
                    if A.shape[0]== A.shape[1]:
                        print(f"\n Determinant of A: \n {determinant(A)}")
                    else:
                         print("Matrix A is not square matrice. Determinant not possible.")
             elif target=="B":   
                  if B.shape[0]== B.shape[1]: 
                       print(f"\n Determinant of B: \n {determinant(B)}")
                  else:
                        print("Matrix B is not square matrice. Determinant not possible.")
             else:
                 print("Invalid choice. Please enter A or B.")

        elif choice == "7":
             target = input("Rank of which matrix? (A or B): ").strip().upper()
             if target == "A":
                 print(f"\n Rank of A: \n {rank(A)}")
             elif target == "B":
                 print(f"\n Rank of B: \n {rank(B)}")
             else:
                 print("Invalid choice. Enter A or B.")

        elif choice =="8":
             target = input("Eigen value and vector of which matrix? (A or B): ").strip().upper()
             if target == "A":
                  if A.shape[0]== A.shape[1]:
                       value, vector = eigen(A)
                       if value == None:  #to get return error message which is string 
                            print(vector)
                       else:
                            print(f"\n Eigen value of matrix A is:\n {value}")
                            print(f"\n Eigen vector of matrix A is:\n {vector}")
                  else:
                       print("ERROR: It is not a square matrix. Eigen values cannot be calculated.")
             if target == "B":
                  if B.shape[0]== B.shape[1]:
                       value, vector = eigen(B)
                       if value == None:  #to get return error message which is string 
                            print(vector)
                       else:
                            print(f"\n Eigen value of matrix B is:\n {value}")
                            print(f"\n Eigen vector of matrix B is:\n {vector}")
                  else:
                       print("ERROR: It is not a square matrix. Eigen values cannot be calculated.")
                                                       
        elif choice=="9":
             #Take first matrix input from user
             rows1 = int(input("Enter the number of rows for first matrix: "))
             cols1 = int(input("Enter the number of columns for first matrix: "))
             A = input_matrix(rows1,cols1, "first" )

             #Take second matrix input from user 
             rows2 = int(input("Enter the number of rows for second matrix: "))
             cols2 = int(input("Enter the number of columns for second matrix: "))
             B = input_matrix(rows2, cols2, "second")
                      
        elif choice=="0":
            print("Exiting Matrix Calculator.")
            break
        else:
            print("Invalid Choice. Try again.")
 
numbers = [1,2,3,4,5,6,7,8,9,10]

squares= [n*n for n in numbers]
print("Bình phương là: ",squares)

oddnumbers= [s for s in squares if s%2!=0]
print("Số lẻ là: ",oddnumbers)
#Bình phương là:  [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#Số lẻ là:  [1, 9, 25, 49, 81]
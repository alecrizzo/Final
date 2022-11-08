#A = [1,2,3,4,5,6,7,8,9,10]
#length = len(A)
#middle = length//2
#first_half = A[:middle]
#second_half = A[middle:]
#B = []
#B += second_half + first_half
#print(B)

#A = [1,2,3,4,5,6,7,8,9,10]
#B = A[5:] + A[:5]
#print(B)

def foobar(*nums):
    product = 1
    for x in range(len(nums)):
        product *= nums[x]
    return product

a = foobar(2, 3, 4)  # will set a to be 24
b = foobar(2, 3) # will set b to be 6
c = foobar() # will set c to be 1!

print(a)
print(b)
print(c)

def count_parantheses(n, l=0,r=0):
    if l==n and r==n:
        return 1
    total=0
    if l>r:
        total+=count_parantheses(n,l,r+1)
    if l<n:
        total+=count_parantheses(n,l+1,r)
    return total

num=int(input("Enter number fo pairs"))
print(count_parantheses(num))
count_parantheses(6)

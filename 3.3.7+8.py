def get_even_list(a):
    i=1
    n=0
    m=len(a)
    while i<m:
        x=a[n]%2
        if x==1:
            a.pop(n)
            i+=2
            n+=1
        else:
            i+=1
            n+=1
    return a
even_list = get_even_list([1, 2, 5, -10, 9, 6])
print(even_list)
if set(even_list) == set([2, -10, 6]):
    print("Your function is correct")
else:
    print("Ooops, bugs detected")

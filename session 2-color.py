color_list=['Blue', 'Red','Black', 'Pink', 'Brown', 'Yellow']
print("My color list\n{0}".format(color_list))
print("color_list at index 3:{0}".format(color_list[3]))
enter_color=int(input("enter a number from 0-5:"))
print("your color:{0}".format(color_list[enter_color]))
print(color_list)
print("\n".join(color_list))
fav_color=input("what is your favorite color?")
if fav_color not in color_list:
    print("Sorry, I could not find your color")
else:
    x=color_list.index(fav_color)
    print("your color is at index {0} in my list".format(x))

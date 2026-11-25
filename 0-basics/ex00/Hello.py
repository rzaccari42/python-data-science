ft_list = ["Hello"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

# Your code here
ft_list.append("World")

# ft_tuple = ("Hello", "Switzerland!")
ft_tuple1 = ft_tuple[:1]
ft_tuple2 = ("Switzerland!",)
ft_tuple = ft_tuple1 + ft_tuple2

ft_set.remove("tutu!")
ft_set.add("Lausanne!")

ft_dict["Hello"] = "42 Lausanne!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)

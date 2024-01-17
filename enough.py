import random
budget = 10
toys = {"squishy koala": 8, "cheshire cat": 8, "sebastian": 2, "little mermaid": 2, "little pony": 2, "emoji": 2, "lunchbox": 7, "elf bottle": 5, "key chain": 5, "cinema ticket": 7, "snake": 4, "magazine 1": 5, "magazine 2": 5, "magazine 3": 8, "rainbow spring": 2, "dog": 15, "lego": 10, "squirel": 5, "ziena": 5, "dancing candy monkey": 5, "fish": 5, "goody heart": 5, "goody heart 2":5, "big egg": 15, "small egg": 10, "ride 1": 2, "ride 2": 2, "fun fair ride": 5, "fun fair toy": 8, "fun fair toy 2": 8, "pica": 20, "cat": 5, "coloring bag": 1, "coloring bag 2": 1, "coloring pencil case": 1, "blue figgy": 5, "red figgy": 5, "troll candy": 5, "peppa big jelly beans": 3, "dragon candy": 5, "toy house": 10, "archery set": 5, "big mermaid toy": 10, "small mermaid toy": 5, "baloon shark": 3, "baloon mouse": 3, "baloon princes": 3, "baloon dog": 3, "baloon unicorn": 3, "baloon heart": 3, "princes toy": 10, "buble maker": 5, "football": 5, "dvd 1": 2, "dvd 2": 2, "dvd 3": 2 }
toy_number = len(toys)
print("Dad says: I bough my doughter about " + str(toy_number) + " toys ")
index_to_select_random_toy = random.randint(0, toy_number)

print ("Child says: buy me a")
print(list(toys)[index_to_select_random_toy])
x = toys.get(list(toys)[index_to_select_random_toy])
print("Dad says: this toy costs " + str(x) + " GBP")
print("Child says: are you goint to buy it ?")
print("Dad says:")
if x < budget:
    print("yes")
else:
    print("no")
def add_pet_to_list_1(pet, pets=[]):
	pets.append(pet)
	return pets

list_1_with_cat = add_pet_to_list_1("cat")
list_1_with_dog = add_pet_to_list_1("dog")


def add_pet_to_list_2(pet, pets=None):
	if pets is None:
		pets = []
	pets.append(pet)
	return pets

list_2_with_cat = add_pet_to_list_2("cat")
list_2_with_dog = add_pet_to_list_2("dog")


print("#"*50)
print("add_pet_to_list_1")
print(list_1_with_cat)
print(list_1_with_dog) # oops

print("#"*50)
print("add_pet_to_list_2")
print(list_2_with_cat)
print(list_2_with_dog) # oops
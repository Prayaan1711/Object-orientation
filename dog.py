class dog:

    species = "dog"

    def __init__(self,name,furcolor):
        self.name = name
        self.furcolor = furcolor

Husky = dog("Siberian Husky","Black,grey and white")
Golden_Retriever = dog("Golden Retriever", "Golden")

print("Siberian Husky is a {} breed.".format(Husky.species))
print("Golden retriever is a {} breed.".format(Golden_Retriever.species))

print("{} is {} in color.".format(Husky.name,Husky.furcolor))
print("{} is {} in color.".format(Golden_Retriever.name,Golden_Retriever.furcolor))

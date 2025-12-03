"""# fungua file katika mode ya kuandika,kisha tunahifdhi katika object f
f = open ("file.txt", 'w', encoding="utf-8")

# tumia f object ambayo inamethod ya write na ndani yake unaandika kitu ambacho unataka kuandika
f.write("hello, najfunza reading and writting files!")

# funga file baada ya kumaliza kuandiuka
f.close()

"""


"""with open("file.txt", 'w') as file_object:
    file_object.write("Hello, Python ni rahisi na nzuri")
    
file_object.close()

print(file_object.closed)"""


with open("file.txt", 'r') as file_object:
    file_object.read()
    
file_object.close()

print(file_object.closed)
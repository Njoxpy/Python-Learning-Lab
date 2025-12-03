majina_ya_wanafunzi = ['Godbless Nyagawa', 'Elvis Mathew', 'Neicore Adam', 'Ronald Chaula']

maksi_za_wanafunzi = [87, 86, 80, 89]

bulliani = [True, False, True, False]

maksi = [12, 15, [13, 14], 34, [14, 15]]

kumi = [10] * 30
print(kumi)

lst = list()
print(lst)  # Output: []

lst = list("Sema Dunia!")
print(lst)  
# Output: ['S', 'e', 'm', 'a', ' ', 'D', 'u', 'n', 'i', 'a', '!']

numbers = list(range(10))
print(numbers)
# Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# uliza jina la mtumiaji
name = input("Jaza username yako: ")
passowrd = input("Jaza password yako: ")

if len(passowrd) > 6:
    print("Karibu!")
else:
    print("Password haiwezi kuna na herufi ambazo ni chini ya 6")
# Introduction

- Private members, kama ilivyo kwenye upande wa C++ huwa kunakuwa na namna ya kuweza kuwa na public na private method katika program yako, pia kwenye Python ipo ila kuna utofauti kidogo.

## Implementation

- Ili kuweza kutengeneza class ambayo ina private members katika Python inabidi private member awe prefixed na undercsore mbili katika program yako `__`.Mfano:

```py
class MyClass:
    def __init__(self):
        self.__private_member = 42

    def public_method(self):
        print("This is a public method")
        # Accessing the private member within the class is fine
        print("Private member value:", self.__private_member)


# Outside the class
obj = MyClass()

# Accessing the public method
obj.public_method()

# Trying to access the private member directly
print("Trying to access private member outside the class:", obj.__private_member)

```

- Kwenye mfano hapo juu tumetengeneza class inaitwa MyClass ikiwa na contructor na method ya kwanza ni hiyo juu ambapo kuna private method ambayo 
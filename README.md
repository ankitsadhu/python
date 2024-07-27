# Table of Content

1. What is pyproject.toml?
2. 
3. Python Basics
   if __name__ = "__main__"
   the __name__ varible is a built in variable in Python, it represent current module name
   if that script is the main program being executed
   runs only when you directly execute that script

*args & **kwargs
def invite_friends(host_name, *friends):

invite_fiends('Alice', 'John', "Joe")

**kwargs -> accept any no of keyword args, stored as dict, some might chage
def plan_party(host_name, **party_details)

plan_party('Alice', music="Jazz", food="Pizza", decorations="Ballons")

*args -> accept any no of positional arguments, these arguments are collected into Tuple

   What is abstract class in python

```python
   from abc import ABC
   class Fruit(ABC):

      @abstractmethod
      def have_seed(self):
        pass

      @abstractmethod
      def color(self):
       pass

   class Apple(Fruit): #Inherited
    def __init__(self):
      self.seed = True
      self.color = "Red"
   
    def have_seed(self): #Implement method
      return self.seed()

    def color(self)

```

   What is super?

```python
   class Animal:
     def __init__(self, name):
        self.name = name
   class Dog(Animal):
     def __init__(self, name, breed):
       super().__init__(name)
       self.breed = breed
```

   What is __init__ method?

- It is a special method that is automatically called when you create an instance of a class.
- It's primary purpose is to initialize the attributes or properties of an object during object creation.

  ```python
    class Dog:
      # self refers to the instance of the obj being created
      def __init__(self, arg1, arg2):
        #initialization code here
        self.name = name
        self.age = age
  my_dog = Dog('Lee', 3)
  ```

  What is__new__ ?
  __new __ -> creates an instance of the class
  __init__ -> initialises instance of class with values
  __getitem__ -> access an element of an obj

```python
   class MyList:
    def __init__(self):
      self.data = [1,2,3]

    def __getitem__(self, index):
      return self.data[index]

    custom_list = MyList()

    print(custom_list[1])

```

    ```python
      class Language:_instance = None
        def__new__(cls, *args, **kwargs):
          if cls._instance is None:
            print("Creating instance")
            cls._instance = super().__new__(cls)
          return instance

    def__init__(self, lang, year):
          self.lang = lang
          self.year = year

    language = Language('Python', 1991)
    language2 = Language('Java', 1991)
    # check if both same instance
    print(language is languag2)

    ```

    Access Modifer in python
    - public
    - protected
    - private

    class Access:
      def__init__(self, a, b, c):
        self.public = a # Public Attribute
        self._protected = b # It should not be access directly outside the class & its subclass, though it is not stricted by python.
        self.__private = c # Private: Difficult to access outside the class

3. OOPS in python
4. Functional Programing in python
5. Fastapi
6. SQLAlchemy
7. Docker

```python

```

class Node:
    def __init__(self, coefficient, exponent):
        self.coefficient = coefficient
        self.exponent = exponent
        self.next = None

class Polynomial:
    def __init__(self):
        self.head = None

    def insert(self, coefficient, exponent):
        new_node = Node(coefficient, exponent)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current is not None:
            print(f"{current.coefficient}x^{current.exponent}", end="")
            if current.next is not None:
                print(" + ", end="")
            current = current.next
        print("\n")

    def add(self, p):
        result = Polynomial()
        current1 = self.head
        current2 = p.head
        while current1 is not None and current2 is not None:
            if current1.exponent == current2.exponent:
                result.insert(current1.coefficient + current2.coefficient, current1.exponent)
                current1 = current1.next
                current2 = current2.next
            elif current1.exponent > current2.exponent:
                result.insert(current1.coefficient, current1.exponent)
                current1 = current1.next
            else:
                result.insert(current2.coefficient, current2.exponent)
                current2 = current2.next
        while current1 is not None:
            result.insert(current1.coefficient, current1.exponent)
            current1 = current1.next
        while current2 is not None:
            result.insert(current2.coefficient, current2.exponent)
            current2 = current2.next
        return result

    def multiply(self, p):
        result = Polynomial()
        current1 = self.head
        while current1 is not None:
            current2 = p.head
            while current2 is not None:
                coefficient = current1.coefficient * current2.coefficient
                exponent = current1.exponent + current2.exponent
                result.insert(coefficient, exponent)
                current2 = current2.next
            current1 = current1.next
        return result

# Get input from user
p1 = Polynomial()
p2 = Polynomial()

print("chand jomlei aval:")
for i in range(1,2):
    term = input("yek adad bedahid space bezanid yek adad digar dahid")
    if(i==2):
        break
    coefficient, exponent = map(int, term.split())
    p1.insert(coefficient, exponent)

print("chand jomlei dovom:")
for i in range(1,2):
    term = input("yek adad bedahid space bezanid yek adad digar dahid")
    if(i==2):
        break
    coefficient, exponent = map(int, term.split())
    p2.insert(coefficient, exponent)

# Display input polynomials
print("\nFirst polynomial:")
p1.display()

print("Second polynomial:")
p2.display()

# Perform summation and multiplication
p3 = p1.add(p2)
p4 = p1.multiply(p2)

# Display results
print("Sum of polynomials:")
p3.display()

print("Product of polynomials:")
p4.display()

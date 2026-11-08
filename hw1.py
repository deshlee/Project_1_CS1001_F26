"""CSC 1001 - Programming Assignment 1.

Student starter file. Implement the eight required functions below.
The provided data types live in data.py; do not edit data.py.

For EVERY function, replace the TODO documentation with a short comment
explaining its purpose, input(s), and output. You may write helper functions.
"""

import data


# Part 1: vowel_count
def vowel_count(text: str) -> int:
    # TODO: Purpose: describe what this function computes.
    # TODO: Input(s): explain each parameter.
    # TODO: Output: explain what the function returns.
    # TODO: Replace this exception with your implementation.
    word=text.lower()
    number=0
    for char in word:
        if char=="a" or char=="e" or char=="i" or char=="o" or char=="u":
            number+=1
    return number


# Part 2: short_lists
def short_lists(items: list[list[int]]) -> list[list[int]]:
    # TODO: Purpose: describe what this function computes.
    # TODO: Input(s): explain each parameter.
    # TODO: Output: explain what the function returns.
    # TODO: Replace this exception with your implementation.
    another=[]
    for l in items:
        if len(l)==2:
            another.append(l)
    return another


# Part 3: ascending_pairs
def ascending_pairs(items: list[list[int]]) -> list[list[int]]:
    # TODO: Purpose: describe what this function computes.
    # TODO: Input(s): explain each parameter.
    # TODO: Output: explain what the function returns.
    # TODO: Replace this exception with your implementation.
    newList=[]
    for i in items:
        if len(i)==2:
            if i[0]>i[1]:
                value=i.pop(0)
                i.append(value)
                newList.append(i)
            else:
                newList.append(i)
        else:
            newList.append(i)
    return newList


# Part 4: add_prices
def add_prices(first: data.Price, second: data.Price) -> data.Price:
    # TODO: Purpose: describe what this function computes.
    # TODO: Input(s): explain each parameter.
    # TODO: Output: explain what the function returns.
    # TODO: Replace this exception with your implementation.
    totalCents=first.cents+second.cents
    totalDollars=first.dollars+second.dollars
    while totalCents>100:
        totalCents=totalCents-100
        totalDollars+=1
    return data.Price(totalDollars, totalCents)

# Part 5: rectangle_area
def rectangle_area(rectangle: data.Rectangle) -> float:
    # TODO: Purpose: describe what this function computes.
    # TODO: Input(s): explain each parameter.
    # TODO: Output: explain what the function returns.
    # TODO: Replace this exception with your implementation.
    x1=rectangle.top_left.x
    x2=rectangle.bottom_right.x
    y1=rectangle.top_left.y
    y2=rectangle.bottom_right.y
    deltaX=x1-x2
    deltaY=y1-y2
    if deltaX<0:
        deltaX=deltaX*-1
    elif deltaY<0:
        deltaY=deltaY*-1
    return deltaX*deltaY

# Part 6: books_by_author
def books_by_author(author: str, books: list[data.Book]) -> list[data.Book]:
    # TODO: Purpose: describe what this function computes.
    # TODO: Input(s): explain each parameter.
    # TODO: Output: explain what the function returns.
    # TODO: Replace this exception with your implementation.
    listing=[]
    for book in books:
        if author in book.authors:
            listing.append(book)
    return listing


# Part 7: circle_bound
def circle_bound(rectangle: data.Rectangle) -> data.Circle:
    # TODO: Purpose: describe what this function computes.
    # TODO: Input(s): explain each parameter.
    # TODO: Output: explain what the function returns.
    # TODO: Replace this exception with your implementation.
    return data.Circle(data.Point((rectangle.top_left.x+rectangle.bottom_right.x)/2, (rectangle.top_left.y+rectangle.bottom_right.y)/2), ((rectangle.top_left.x-rectangle.bottom_right.x)**2+(rectangle.top_left.y-rectangle.bottom_right.y)**2)**0.5)

# Part 8: below_pay_average
def below_pay_average(employees: list[data.Employee]) -> list[str]:
    # TODO: Purpose: describe what this function computes.
    # TODO: Input(s): explain each parameter.
    # TODO: Output: explain what the function returns.
    # TODO: Replace this exception with your implementation.
    listy=[]
    pay=0
    if len(employees)==0:
        return listy
    for e in employees:
        pay+=e.pay_rate
    pay=pay/len(employees)
    for employee in employees:
        if employee.pay_rate<pay:
            listy.append(employee.name)
    return listy

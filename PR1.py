
books = {
    "Python": 15,
    "Java": 29,
    "C": 43,
    "C++": 57,
    "HTML": 20
}

total = sum(books.values())
average = total / len(books)

print("Average books borrowed:", average)

highest = max(books, key=books.get)
lowest = min(books, key=books.get)

print("Highest borrowed book:", highest)
print("Number of borrowings:", books[highest])

print("Lowest borrowed book:", lowest)
print("Number of borrowings:", books[lowest])

borrowings = [15, 29, 43, 57, 20, 0, 0, 10]

count = borrowings.count(0)

print("Members who have not borrowed books:", count)

most_borrowed = max(books, key=books.get)

print("Most frequently borrowed book:", most_borrowed)
print("Total borrowings:", books[most_borrowed])

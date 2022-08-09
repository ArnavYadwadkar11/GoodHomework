import random
names = ['Mukesh Ambani', 'Arnav', 'Ratan Tata', 'Sundar Pichai', 'Elon Musk', 'Bill Gates', 'Tim Cook', 'Joe Biden', 'Narendra Modi', 'Mark Zuckerberg']
age = ['11', '65', '79', '51', '84', '50', '66', '71', '61', '38']
count = 1
while count <=10:
    print(random.choice(names), end=" ")
    print(random.choice(age))
    count +=1
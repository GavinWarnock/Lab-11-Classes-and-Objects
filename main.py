from person import Person
person_one = Person("Hank", 100)
person_two = Person("Gavin", 200)

funds_to_transfer = person_one.send_funds(50)
person_two.receive_funds(person_one, funds_to_transfer)


    # string concatenation
    # # Suppose we create
creator = "Daniel Wagner"

print("The creator of this is " + creator)
print("The creator of this is {}".format(creator))
print(f"The creator of this is {creator}")

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Person: ")

madlib = f"Travelling is so {adj}! I'm so fascinated by the cultures of our world because \ I love to {verb1}.  Continue to be curious and {verb2} the world, like you are {famous_person:}!"

print(madlib)
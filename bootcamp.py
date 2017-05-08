def make_coffee():
    print "1.Take a cup"
    print "2. Pour coffee into cup"
    print "3. Add ingredients. Here are the available ingredients:\nHot water\nMilk\nCoffee\nSugar"
    ingredients = raw_input("Enter ingredients separated by a space only:")
    print "5. Stir"

    ingredients = ingredients.split()
    return ingredients

coffee = make_coffee()

def serve_coffee(A):
    name = raw_input("What's your name?")
    if "milk" in coffee and "coffee" in coffee:
        print "Here goes your White Coffee, %s" % (name)
    elif "milk" not in coffee and "coffee" in coffee:
        print "Here goes your Black Coffee, %s" % (name)
    else:
        print "You left out coffee in your ingredients!"


print serve_coffee(coffee)


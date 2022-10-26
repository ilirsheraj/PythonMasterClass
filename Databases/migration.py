import duck


flock = duck.Flock()
donald = duck.Duck()
daisy = duck.Duck()
duck3 = duck.Duck()
duck4 = duck.Duck()
duck5 = duck.Duck()
duck6 = duck.Duck()
duck7 = duck.Duck()
percy = duck.Penguin()
# percy = duck.Mallard()

flock.add_duck(donald)
flock.add_duck(daisy)
flock.add_duck(duck3)
flock.add_duck(duck4)
flock.add_duck(percy)
flock.add_duck(duck5)
flock.add_duck(duck6)
flock.add_duck(duck7)

flock.migrate()

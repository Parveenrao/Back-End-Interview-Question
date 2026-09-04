from character import Character

original = Character(
            "Zombie",
            100,
            50,
            ["Bite" , "Scratch"]
)


enemy1 = original.clone()

enemy2 = original.clone()

enemy1.name = "Zombie-1"
enemy2.name = "Zombie-2"

enemy1.skills.append("Posion Bite")

original.display()

enemy1.display()

enemy2.display()
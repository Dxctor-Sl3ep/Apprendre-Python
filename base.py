#Etape 0 : Installer le module python dans les extensions VSCode
#Etape 1 : Afficher dans le terminal 
print("Hello")

#Etape 2 : une fonction
name = "Hush" #str
health = 100 #int 
shield = True #bool
shoot = 15.5 #float

print(name)
print(type(health))
print(type(shoot) == int )

#Etape 3 : Les opérations

health += 20
print(health)
health = health + 20
print(health)
health = health - shoot
print(health)
shoot = shoot * 1.5
print(shoot)
shoot = shoot / 2
print(shoot)
# Opérateurs "avancés"

# // Division euclidienne
# % Modulo
# ** Puissance

print("=" * 30)
 
 
 #Etape 4 : Les listes
weapon = ["Vandal", "Phantom", "Ghost", "Bandit", "Bulldog"]
print(weapon)
print(weapon[2]) # liste commance à 0
print(len(weapon))
print(weapon[-2]) # liste commence à -1
print(weapon[2:5]) # liste de l'index 1 à 5

weapon.append("Spectre")
print(weapon)

print("=" * 30)
#Etapes 5 : Les dictionnaires 
round = {
    "round 1" : "Win",
    "round 2" : "Loose",
    "round 3" : "Win",
    "round 4" : "Win",
    "round 5" : "Win",
}
print(round)
print(round["round 2"])
round["round 6"] = "Win"
print(round)

print("=" * 30)
#Etape 6 : Structure Conditionnelles
health = 100
game_statue = True

#death = health <= 0
death = ((health <= 0) or not game_statue)
print(game_statue)
print(death)

if health <= 0:
    print("Game Over")
elif health <=10 :
    print(f"Low Life at {health}HP")
else :
    print("Hush Alive")

print("=" * 30)
#Etape 7 : le while et le for
for i in weapon :
    print(i)

carres = [x**2 for x in range(1, 6)]
print(carres)

age =int(input("Donne ton age >>>  "))
while age<=18 :
    print("Interdi de jouer")
    age =int(input("Donne ton age  >>>  "))

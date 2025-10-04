import random

names = [
    "Mayor Singh", "Dr. Patel", "Professor Sharma", "Captain Rao", "Actor Verma",
    "Minister Das", "Chef Gupta", "Farmer Kumar", "Detective Bose", "Singer Mehta",
    "Teacher Rani", "Engineer Joshi", "Pilot Nair", "Author Malhotra", "Student Iqbal",
    "Coach Fernandes", "Entrepreneur Kapoor", "Scientist Menon", "Librarian Chawla", "Dancer Roy",
    "Explorer Khan", "Doctor Pillai", "Artist Gill", "Judge Thakur", "Magician Batra"
]

actions = [
    "bans all scooters", "discovers secret tunnel", "wins knitting contest",
    "orders free mangoes for everyone", "paints city hall pink",
    "launches flying rickshaw service", "opens world’s largest tea stall",
    "introduces compulsory napping hours", "claims to talk to pigeons",
    "declares samosa as national treasure", "hosts marathon chess event",
    "starts campaign to hug strangers", "turns library into disco",
    "accidentally buys 1,000 goats", "announces free laddoos on Fridays",
    "creates world’s longest selfie stick", "designs robot that makes chai",
    "organizes midnight cricket league", "starts laughter yoga sessions",
    "changes national anthem to folk song", "opens underwater museum",
    "begins rooftop farming project", "launches festival of balloons",
    "turns buses into karaoke stages", "plans to build chocolate fountain"
]

places = [
    "in Mumbai", "at the old fort", "on Main Street", "inside city hall",
    "at the railway station", "near the beach", "in the jungle park",
    "under the metro bridge", "at the cricket stadium", "on the university campus",
    "at the science museum", "inside the shopping mall", "at the airport",
    "near the bus stop", "on the rooftop garden", "at the carnival",
    "inside the temple courtyard", "on the floating stage", "near the waterfall",
    "at the city zoo", "inside the library", "at the market square",
    "on the bridge over the river", "in the desert camp", "inside the amusement park"
]

while True:
    user = input("you Want to generate txt(yes/no): ")
    if user.lower().strip() == "yes".lower().strip():
        times = int(input("Enter how many times you want to Generate(1-10): "))
        for i in range(0,times):
            name = random.choice(names)
            action = random.choice(actions)
            place = random.choice(places)

            print(f"Breaking News : {name} {action} {place}")
    else:
        print("Thank you")
        break



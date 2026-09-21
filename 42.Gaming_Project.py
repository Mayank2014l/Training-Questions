class GamingTournament:

    class Player:
        def __init__(self, id, name, game, team, status="REGISTERED"):
            self.id = id
            self.name = name
            self.game = game
            self.team = team
            self.status = status

        def player_info(self):
            return f"ID: {self.id} | Name: {self.name} | Game: {self.game} | Team: {self.team} | Status: {self.status}"

    def __init__(self):
        self.players = []

    def add_player(self):
        id = int(input("Enter Player ID: "))
        name = input("Enter Player Name: ")
        game = input("Enter Game Name: ")
        team = input("Enter Team Name: ")

        p = self.Player(id, name, game, team)
        self.players.append(p)

        print("Player added successfully.")

    def show_players(self):
        if len(self.players) == 0:
            print("No players registered yet.")
        else:
            print("Players List")
            for p in self.players:
                print(p.player_info())
            print()

    def update_status(self):
        id = int(input("Enter Player ID: "))
        for p in self.players:
            if p.id == id:

                if p.status == "REGISTERED":
                    p.status = "PLAYING"

                elif p.status == "PLAYING":
                    p.status = "ELIMINATED"

                else:
                    print("Player is already eliminated.")
                    return

                print("Status updated successfully.")
                return
        print("Player ID not found.")

    def search_player(self):
        id = int(input("Enter Player ID: "))
        for p in self.players:
            if p.id == id:
                print(p.player_info())
                return

        print("Player ID not found.")

game = GamingTournament()

while True:
    print("a. Add Player")
    print("b. View Players")
    print("c. Update Player Status")
    print("d. Search Player")
    print("e. Exit")

    ch = input("Enter choice: ")

    if ch == "a":
        game.add_player()

    elif ch == "b":
        game.show_players()

    elif ch == "c":
        game.update_status()

    elif ch == "d":
        game.search_player()

    elif ch == "e":
        print("Exiting...")
        break

    else:
        print("Invalid Choice!")
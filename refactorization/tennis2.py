class TennisGame2:
    def __init__(self, player1_name: str, player2_name: str):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.p1points = 0
        self.p2points = 0

    def won_point(self, player_name: str):
        """
        funkcja wyłowana z zęwnątrz, dodaje punkt dla przekazanego przez argument gracza
        """
        if player_name == self.player1_name:
            self.p1points += 1
        else:
            self.p2points += 1



    def __get_result(self, points: int) -> str:
        """
        zwraca wynik str na podstawie punktów, jeśli point not in (0,1,2,3) -> return "Deuce"
        """
        return {
                0: "Love",
                1: "Fifteen",
                2: "Thirty",
                3: "Forty",
            }.get(points, "Deuce")

    def score(self) -> str:
        """
        funkcja wyłowana z zęwnątrz, zapewnia logikę gry i zwraca wynik całej gry
        """
        if self.p1points == self.p2points and self.p1points < 3:
            return self.__get_result(self.p1points) + "-All"
        
        elif self.p1points == self.p2points and self.p1points > 2:
            return "Deuce"
        
        elif (
            self.p1points >= 4
            and self.p2points >= 0
            and (self.p1points - self.p2points) >= 2
        ):
            return f"Win for {self.player1_name}"
        
        elif (
            self.p2points >= 4
            and self.p1points >= 0
            and (self.p2points - self.p1points) >= 2
        ):
            return f"Win for {self.player2_name}"


        elif self.p1points > 0 and self.p2points == 0:
            return self.__get_result(self.p1points) + "-Love"

        elif self.p1points > self.p2points and self.p2points >= 3:
            return f"Advantage {self.player1_name}"

        elif self.p2points > self.p1points and self.p1points >= 3:
            return f"Advantage {self.player2_name}"

        else:
            return self.__get_result(self.p1points) + "-" + self.__get_result(self.p2points)

        

        


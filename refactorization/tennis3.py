class TennisGame3:
    def __init__(self, player1_name: str, player2_name: str):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_points = 0
        self.player2_points = 0

    def won_point(self, n):
        """
        funkcja wyłowana z zęwnątrz, dodaje punkt dla przekazanego przez argument gracza
        """
        if n == self.player1_name:
            self.player1_points += 1
        else:
            self.player2_points += 1

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

    def score(self):
        """
        funkcja wyłowana z zęwnątrz, zapewnia logikę gry i zwraca wynik całej gry
        """
        if (self.player1_points < 4 and self.player2_points < 4) and (self.player1_points + self.player2_points < 6):
            if self.player1_points == self.player2_points:
                return self.__get_result(self.player1_points) + "-All"
            return self.__get_result(self.player1_points) + "-" + self.__get_result(self.player2_points)
        
        else:
            if self.player1_points == self.player2_points:
                return "Deuce"


            if self.player1_points > self.player2_points:
                player_name = self.player1_name
            else:
                player_name = self.player2_name



            return (
                "Advantage " + player_name
                if ((self.player1_points - self.player2_points) in (-1, 1))
                else "Win for " + player_name
            )

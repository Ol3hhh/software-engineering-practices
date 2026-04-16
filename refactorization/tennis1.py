class TennisGame1:
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


    def __win_or_advantage(self, points: int) -> str:
        """
        zwraca win albo advantage dla gracza na podstawie punktów
        """
        if points == 1:
            return f"Advantage {self.player1_name}"
        elif points == -1:
            return f"Advantage {self.player2_name}"
        elif points >= 2:
            return f"Win for {self.player1_name}"
        else:
            return f"Win for {self.player2_name}"

    def score(self) -> str:
        """
        funkcja wyłowana z zęwnątrz, zapewnia logikę gry i zwraca wynik całej gry
        """
        if self.p1points == self.p2points:
            if self.p1points not in (0, 1, 2):
                return "Deuce"
            return self.__get_result(self.p1points) + "-All"
        
        elif self.p1points >= 4 or self.p2points >= 4:
            return self.__win_or_advantage(self.p1points - self.p2points)
            
        else:
            return self.__get_result(self.p1points) + "-" + self.__get_result(self.p2points)
                

class Node:
    def __init__(self,coefficient,exponent) :
        self.coefficient=coefficient
        self.exponent=exponent
        self.next=None


class PLL:
    def __init__(self) -> None:
        self.head=None
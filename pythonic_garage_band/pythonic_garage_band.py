class Musician:
    def play_solo(self):
        pass

class Guitarist(Musician):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"My name is {self.name} and I play guitar"

    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"

    def get_instrument(self):
        return "guitar"
    def play_solo(self):
        return "face melting guitar solo"


class Drummer(Musician):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"My name is {self.name} and I play drums"

    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"

    def get_instrument(self):
        return "drums"
    def play_solo(self):
        return "rattle boom crash"


class Bassist(Musician):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"My name is {self.name} and I play bass"

    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"

    def get_instrument(self):
        return "bass"
    def play_solo(self):
        return "bom bom buh bom"


class Band:
    instances = []
    def __init__(self, name, members=[]):
        self.name = name
        self.members = members 
        Band.instances.append(self)

    @classmethod
    def to_list(cls):
        return cls.instances

    def add_member(self, member):
        self.members.append(member)

    def play_solos(self):
        solos = []
        for member in self.members:
            solo = member.play_solo()
            solos.append(solo)
        return solos
    
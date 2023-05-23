class Musician:
    """
    A base class representing a musician.
    """

    def play_solo(self):
        """
        Play a solo.

        This method should be overridden by subclasses.
        """
        pass


class Guitarist(Musician):
    """
    A class representing a guitarist.

    Attributes:
        name (str): The name of the guitarist.
    """

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"My name is {self.name} and I play guitar"

    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"

    def get_instrument(self):
        """
        Get the instrument played by the guitarist.

        Returns:
            str: The instrument (guitar).
        """
        return "guitar"

    def play_solo(self):
        """
        Play a face-melting guitar solo.

        Returns:
            str: The guitar solo.
        """
        return "face melting guitar solo"


class Drummer(Musician):
    """
    A class representing a drummer.

    Attributes:
        name (str): The name of the drummer.
    """

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"My name is {self.name} and I play drums"

    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"

    def get_instrument(self):
        """
        Get the instrument played by the drummer.

        Returns:
            str: The instrument (drums).
        """
        return "drums"

    def play_solo(self):
        """
        Play a rattle boom crash drum solo.

        Returns:
            str: The drum solo.
        """
        return "rattle boom crash"


class Bassist(Musician):
    """
    A class representing a bassist.

    Attributes:
        name (str): The name of the bassist.
    """

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"My name is {self.name} and I play bass"

    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"

    def get_instrument(self):
        """
        Get the instrument played by the bassist.

        Returns:
            str: The instrument (bass).
        """
        return "bass"

    def play_solo(self):
        """
        Play a bom bom buh bom bass solo.

        Returns:
            str: The bass solo.
        """
        return "bom bom buh bom"


class Band:
    """
    A class representing a band.

    Attributes:
        name (str): The name of the band.
        members (list): A list of members in the band.
    """

    instances = []

    def __init__(self, name, members=None):
        self.name = name
        self.members = members or []
        Band.instances.append(self)

    @classmethod
    def to_list(cls):
        """
        Get a list of all band instances.

        Returns:
            list: A list of band instances.
        """
        return cls.instances

    def add_member(self, member):
        """
        Add a member to the band.

        Args:
            member (Musician): The musician to add to the band.
        """
        self.members.append(member)

    def play_solos(self):
        """
        Play solos for each band member.

        Returns:
            list: A list of solos played by each band member.
        """
        solos = []
        for member in self.members:
            solo = member.play_solo()
            solos.append(solo)
        return solos
    
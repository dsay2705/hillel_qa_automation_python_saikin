class Romb:
    def __init__(self, side_a, angle_a=None, angle_b=None):
        if angle_a is None and angle_b is None:
            raise ValueError("At least one angle must be provided")

        if angle_a is None:
            angle_a = 180 - angle_b
        elif angle_b is None:
            angle_b = 180 - angle_a

        self.side_a = side_a
        self.angle_a = angle_a
        self.angle_b = angle_b

    def __setattr__(self, name, value):

        if name == "side_a":
            if value <= 0:
                raise ValueError(f"The '{name}' must be greater than 0")

        elif name in ("angle_a", "angle_b"):
            if not (0 < value < 180):
                raise ValueError(f"The '{name}' must be between 0 and 180")

            other_name = "angle_b" if name == "angle_a" else "angle_a"
            other_value = getattr(self, other_name, None)

            if other_value is not None and value + other_value != 180:
                raise ValueError("Sum of angles must be 180")

        super().__setattr__(name, value)

    def display_info(self):
        print(f"Side a: {self.side_a}")
        print(f"Angle a: {self.angle_a}")
        print(f"Angle b: {self.angle_b}")


my_romb = Romb(5, angle_b=160)
my_romb.display_info()
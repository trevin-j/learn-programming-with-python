# %%
from manim import *

config.media_width = "75%"
config.verbosity = "WARNING"

# %%
# Verifying manim is correctly installed
%%manim -qm --format=gif CircleToSquare 

class CircleToSquare(Scene):
    def construct(self):
        blue_circle = Circle(color=BLUE, fill_opacity=0.5)
        green_square = Square(color=GREEN, fill_opacity=0.8)
        self.play(Create(blue_circle))
        self.wait()
        
        self.play(Transform(blue_circle, green_square))
        self.wait()
        
# %%
%%manim -qm --format=gif VariableDemo

# Visualize what a variable is

class VariableDemo(Scene):
    def construct(self):
        # Say we have a box containing a number
        box = Square(color=BLUE, fill_opacity=0.5)
        self.play(Create(box))

        # And inside this box we have a number
        number = Text("42").scale(2)
        self.play(Create(number))
        self.wait()

        # We can think of this box as a variable because it contains that value
        self.play(box.animate.shift(3*RIGHT), number.animate.shift(3*RIGHT))
        var_text = Text("meaning_of_life = ").scale(1.3).next_to(box, LEFT)
        self.play(Create(var_text))
        self.wait(2)


# %%
%%manim -qm --format=gif VariableUseDemo

class VariableUseDemo(Scene):
    def construct(self):
        # number_of_apples = 16
        box = Square(color=BLUE, fill_opacity=0.5).scale(0.7).shift(3*RIGHT)
        number = Text("16").scale(1.7).shift(3*RIGHT)
        num_apple_text1 = Text("number_of_apples = ").next_to(box, LEFT)
        self.play(Create(num_apple_text1), Create(box), Create(number))
        self.wait()

        # number_of_oranges = number_of_apples
        num_orange_text = Text("number_of_oranges = ")
        num_apple_text2 = Text("number_of_apples")

        self.play(
            box.animate.shift(0.5*UP),
            number.animate.shift(0.5*UP),
            num_apple_text1.animate.shift(0.5*UP)
        )
        self.play(
            Create(num_orange_text.next_to(num_apple_text1, DOWN, buff=0.7).shift(2*LEFT)),
            Create(num_apple_text2.next_to(num_orange_text, RIGHT))
        )
        self.wait(2)

        # number_of_oranges = [16]
        self.play(
            FadeOut(num_apple_text1, shift=DOWN),
            FadeOut(num_apple_text2, shift=DOWN),
            num_orange_text.animate.shift(0.8*UP).shift(RIGHT*1.9),
            box.animate.shift(0.5*DOWN).shift(RIGHT*0.4),
            number.animate.shift(0.5*DOWN).shift(RIGHT*0.4)
        )

        self.wait(2)

# %%

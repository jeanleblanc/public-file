from manim import *

class Sqrt2Irrationality(Scene):
    def construct(self):
        # Title
        title = Text("Proof that √2 is Irrational", font_size=24)
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))

        # Assumption step
        assume = Tex(
            r"Assume $\sqrt{2}$ is rational, ",
            r"i.e., $\sqrt{2} = \frac{a}{b}$",
            r" where $a$ and $b$ are integers with no common factors."
        ).scale(0.7)
        self.play(Write(assume))
        self.wait(2)

        # Squaring both sides
        square_both_sides = Tex(
            r"Squaring both sides, ",
            r"$2 = \frac{a^2}{b^2}$, ",
            r"so $2b^2 = a^2$."
        ).scale(0.7).next_to(assume, DOWN)
        self.play(Write(square_both_sides))
        self.wait(2)

        # Conclusion part 1
        conclusion1 = Tex(
            r"This means $a^2$ is even, ",
            r"which implies $a$ is even."
        ).scale(0.7).next_to(square_both_sides, DOWN)
        self.play(Write(conclusion1))
        self.wait(2)

        # Conclusion part 2
        conclusion2 = Tex(
            r"If $a$ is even, then there exists ",
            r"an integer $k$ such that $a = 2k$."
        ).scale(0.7).next_to(conclusion1, DOWN)
        self.play(Write(conclusion2))
        self.wait(2)

        # Substitute back and conclude
        substitute = Tex(
            r"Substituting back, $2b^2 = (2k)^2 = 4k^2$, ",
            r"so $b^2 = 2k^2$."
        ).scale(0.7).next_to(conclusion2, DOWN)
        self.play(Write(substitute))
        self.wait(2)

        final_conclusion = Tex(
            r"This implies $b^2$ is even, ",
            r"and thus $b$ is even."
        ).scale(0.7).next_to(substitute, DOWN)
        self.play(Write(final_conclusion))
        self.wait(2)

        contradiction = Text(
            "Both a and b cannot be even, contradiction!",
            color=RED
        ).scale(0.7).next_to(final_conclusion, DOWN)
        self.play(Write(contradiction))
        self.wait(2)

        # Ending
        end_text = Text("Thus, √2 is irrational.").scale(0.9).next_to(contradiction, DOWN)
        self.play(Write(end_text))
        self.wait(3)

        # Grouping all and fading out
        all_mobjects = VGroup(assume, square_both_sides, conclusion1, conclusion2, substitute, final_conclusion, contradiction, end_text)
        self.play(FadeOut(all_mobjects))


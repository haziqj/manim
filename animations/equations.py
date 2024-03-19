from manim import *
from manim_revealjs import PresentationScene, COMPLETE_LOOP

config.video_dir = "./videos"
# config.disable_caching = False

config.background_color = WHITE
Tex.set_default(color=BLACK)
MathTex.set_default(color=BLACK)
Text.set_default(color=BLACK)
Square.set_default(color=BLACK)
Circle.set_default(color=BLACK)

class SumOfSquares(PresentationScene):
    def construct(self):
        # eq1 = MathTex("\sum_{i=1}^n (X_i - \mu)^2")
        # eq2 = MathTex("\sum_{i=1}^n (X_i - \mu)^2", "=", "\sum_{i=1}^n (X_i - ", "\mu)^2")
        # eq3 = MathTex("\sum_{i=1}^n (X_i - \mu)^2", "=", "\sum_{i=1}^n (X_i - ", "\\bar{X} + \\bar{X} -", "\mu)^2")
        # 
        # eq3a = MathTex("\sum_{i=1}^n (X_i - \mu)^2", "=", "\sum_{i=1}^n (X_i - \\bar{X} + \\bar{X} - \mu)", "{}^2")
        # eq4  = MathTex("\sum_{i=1}^n (X_i - \mu)^2", "=", "\sum_{i=1}^n (", "(X_i - \\bar{X})^2",  "+", "(\\bar{X} - \mu)^2")
        # 
        # self.play(Write(eq1))
        # self.end_fragment()
        # 
        # self.play(TransformMatchingTex(eq1, eq2))
        # self.end_fragment()
        # 
        # self.play(TransformMatchingTex(eq2, eq3))
        # self.end_fragment()
        # 
        # self.play(TransformMatchingTex(eq3, eq3a))
        # self.end_fragment()

        # Initial and intermediate equations for reference
        equation1 = MathTex(r"(a + b)^2")
        equation2 = MathTex(r"(a + c - c + b)^2")  # Not directly used, for visual reference

        # Final equation split into parts for transformation
        part_common = MathTex(r"(a + c - c + b)^2 =")  # Part that transforms from equation2
        part_new = MathTex(r"(a + c)^2 - 2(a+c)(c+b) + (c+b)^2")  # New part without direct predecessor

        # Positioning the final parts
        equation3 = VGroup(part_common, part_new).arrange(DOWN, aligned_edge=LEFT)
        part_common.align_to(equation1, LEFT)  # Align to where equation2 would transform
        part_new.next_to(part_common, DOWN, aligned_edge=LEFT)

        # Step 1: Display the initial equation
        self.play(Write(equation1))
        self.wait(1)

        # Step 2: Transform to the common part of the final equation, simulating equation2's transformation
        self.play(Transform(equation1, part_common))
        # Simultaneously fade in the new part of the equation
        self.play(FadeIn(part_new, shift=DOWN))
        self.wait(2)

        self.end_fragment()


# \begin{aligned}
# \sum_{i=1}^n (X_i - \mu)^2 &= \sum_{i=1}^n (X_i - \bar X + \bar X - \mu)^2 \\
# &= \sum_{i=1}^n (X_i - \bar X)^2 + 2\sum_{i=1}^n (X_i - \bar X)(\bar X - \mu) + \sum_{i=1}^n (\bar X - \mu)^2 \\
# &= \sum_{i=1}^n (X_i - \bar X)^2 + 2(\bar X - \mu)\sum_{i=1}^n (X_i - \bar X) + (\bar X - \mu)^2 \sum_{i=1}^n 1 \\
# &= \sum_{i=1}^n (X_i - \bar X)^2 + 2(\bar X - \mu)\left\{\sum_{i=1}^n X_i - \sum_{i=1}^n\bar X \right\} + n (\bar X - \mu)^2 \\
# &= \sum_{i=1}^n (X_i - \bar X)^2 + 2(\bar X - \mu)\left\{\frac{n}{n}\sum_{i=1}^n X_i - n\bar X \right\} + n (\bar X - \mu)^2 \\
# &= \sum_{i=1}^n (X_i - \bar X)^2 + 2(\bar X - \mu)\left\{n\bar X - n\bar X \right\} + n (\bar X - \mu)^2 \\
# &= \sum_{i=1}^n (X_i - \bar X)^2 + n (\bar X - \mu)^2
# \end{aligned}

from manim import *

class GearCalculation(Scene):
    def construct(self):
        # Background color
        self.camera.background_color = WHITE
        
        # Title and introduction
        title = Text("Gear Ratio Calculation", font_size=36, color=BLACK).to_edge(UP)
        intro = Text("Let's understand how to reduce a force using gears.", font_size=24, color=BLACK).next_to(title, DOWN, buff=0.5)
        
        self.play(Write(title), FadeIn(intro))
        self.wait(2)
        self.play(FadeOut(intro))
        
        # Gear ratio explanation
        explanation1 = Text("We want to go from 4000 N to 100 N, requiring a ratio of 1:40.", font_size=24, color=BLACK).to_edge(UP)
        self.play(Transform(title, explanation1))
        self.wait(2)
        
        # Stages explanation
        stage_explanation = Text("This is achieved in three stages, each reducing the force by a factor of 1:4.", font_size=24, color=BLACK).move_to(3*UP)
        self.play(Write(stage_explanation))
        self.wait(2)
        
        # Displaying stages
        for i in range(1, 4):
            stage = Text(f"Stage {i}: 10/40 = 1/4", font_size=24, color=BLACK).move_to(0.5*UP)
            self.play(Transform(stage_explanation, stage))
            self.wait(1)
        
        # Total reduction
        total_reduction = Text("Total reduction: (1/4)^3 = 1/64", font_size=24, color=BLACK).move_to(3*UP)
        self.play(Transform(stage_explanation, total_reduction))
        self.wait(2)
        
        # Final force calculation
        final_force = Text("Resulting in a force reduction from 4000 N to 100 N.", font_size=24, color=BLACK).move_to(3*UP)
        self.play(Transform(stage_explanation, final_force))
        self.wait(2)
        
        # Lever explanation
        lever_explanation = Text("A lever action multiplies the force, achieving the desired reduction.", font_size=24, color=BLACK).move_to(3*UP)
        self.play(Transform(stage_explanation, lever_explanation))
        self.wait(2)
        
        # Conclusion
        conclusion = Text("Through this mechanism, gears effectively distribute force.", font_size=24, color=BLACK).to_edge(DOWN)
        self.play(Write(conclusion))
        self.wait(2)
        
        # Clear scene
        self.play(FadeOut(stage_explanation), FadeOut(conclusion), FadeOut(title))
        self.wait(1)


from manim import *

class layoutAlgorithm(Scene):
    def construct(self):
        def up_position1(mobject):
            mobject.next_to(layout1,LEFT,buff=0.5)
        def down_position(mobject):
            mobject.next_to(layout1,DOWN,buff=0.5)
        def left_position1(mobject):
            mobject.next_to(layout1,LEFT,buff=0.5)
        def right_position1(mobject):
            mobject.next_to(rect1,RIGHT,buff=0.5)
            
        # 布局算法 title
        layoutTitle = Text('聚合 LOGO 布局算法')
        self.add(layoutTitle)
        self.wait(2)
        self.play(FadeOut(layoutTitle,shift=DOWN),run_time=0.5)
        
        # 展示第一个布局算法
        layout1 = SVGMobject("material/HLeftLayout.svg",height = 0.4)
        layout1.shift(RIGHT)
        self.add(layout1)
        
        layout1Title = Text('左对齐')
        layout1Title.scale(0.8)
        layout1Title.add_updater(up_position1)
        
        self.add(layout1Title)
        self.play(layout1.animate.shift(UP*2.5))
        
        # 添加容器和 logo
        newSVGTitle1 = Text('创建svg节点')
        newSVGTitle1.scale(0.6)
        newSVGTitle1.add_updater(right_position1)
        newSVGTitle2 = Text('<svg>')
        newSVGTitle2.scale(0.6)
        newSVGTitle2.add_updater(lambda newSVGTitle2: newSVGTitle2.next_to(newSVGTitle1,DOWN,buff=0.2))
        newSVGTitle3 = Text('</svg>')
        newSVGTitle3.scale(0.6)
        newSVGTitle3.add_updater(lambda newSVGTitle3: newSVGTitle3.next_to(newSVGTitle2,DOWN,buff=0.2))
        
        
        rect1 = Rectangle(width=8, height=3, color = WHITE)
        
        self.add(newSVGTitle1)
        self.add(newSVGTitle2)
        self.add(newSVGTitle3)
        self.play(Create(rect1))
        self.wait(0.4)
        
        # 添加 svg 素材
        svgMaterialTitle = Text('svg 素材').move_to([-6,3,0])
        svgMaterialTitle.scale(0.6)
        self.add(svgMaterialTitle)
        alipay = SVGMobject("material/alipayplus.svg",height = 0.4).move_to([-6,2,0])
        self.play(Create(alipay),run_time=0.2)
        alipayHK = SVGMobject("material/AlipayHK.svg",height = 0.4).move_to([-6,1,0])
        self.play(Create(alipayHK),run_time=0.2)
        boost = SVGMobject("material/Boost.svg",height = 0.4).move_to([-6,0,0])
        self.play(Create(boost),run_time=0.2)
        bpi = SVGMobject("material/BPI.svg",height = 0.4).move_to([-6,-1,0])
        self.play(Create(bpi),run_time=0.2)
        dana = SVGMobject("material/DANA.svg",height = 0.4).move_to([-6,-2,0])
        self.play(Create(dana),run_time=0.2)
        
        self.play(FadeOut(svgMaterialTitle))
        
        # placeholder   
        self.wait(10)
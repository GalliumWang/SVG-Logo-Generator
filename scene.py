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
        def logo_position_top(mobject):
            mobject.set_value(alipay.get_top()[1])
        def logo_position_left(mobject):
            mobject.set_value(alipay.get_top()[0])
            
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
        self.play(layout1.animate.shift(UP*3))
        
        # 添加容器和 logo
        newSVGTitle1 = Text('创建svg节点')
        newSVGTitle1.scale(0.6)
        newSVGTitle1.add_updater(lambda newSVGTitle1: newSVGTitle1.next_to(rect1,UP,buff=0.75))
        newSVGTitle2 = Text('<svg>',color=BLUE)
        newSVGTitle2.scale(0.6)
        newSVGTitle2.move_to([5,0.2,0])
        newSVGTitle3 = Text('</svg>',color=BLUE)
        newSVGTitle3.scale(0.6)
        newSVGTitle3.move_to([5.1,-0.2,0])
        
        
        rect1 = Rectangle(width=8, height=1.25, color = WHITE)
        
        self.add(newSVGTitle1)
        self.play(Create(rect1))
        self.add(newSVGTitle2)
        self.add(newSVGTitle3)
        self.wait(0.4)
        
        # 添加 svg 素材
        svgMaterialTitle = Text('svg 素材').move_to([-5.5,3,0])
        svgMaterialTitle.scale(0.6)
        self.add(svgMaterialTitle)
        alipay = SVGMobject("material/alipayplus.svg",width = 1.5).move_to([-5.5,2,0])
        self.play(Create(alipay),run_time=0.2)
        alipayHK = SVGMobject("material/AlipayHK.svg",width = 1.5).move_to([-5.5,1,0])
        self.play(Create(alipayHK),run_time=0.2)
        boost = SVGMobject("material/Boost.svg",width = 1.5).move_to([-5.5,0,0])
        self.play(Create(boost),run_time=0.2)
        bpi = SVGMobject("material/BPI.svg",width = 1.5).move_to([-5.5,-1,0])
        self.play(Create(bpi),run_time=0.2) 
        # dana = SVGMobject("material/DANA.svg",width = 1.5).move_to([-5.5,-2,0])
        # self.play(Create(dana),run_time=0.2)
        self.play(FadeOut(svgMaterialTitle))
        self.wait(0.2)  
        
        # 拼接 svg
        newSVGTitle4 = Text('拼接 svg 素材')
        newSVGTitle4.scale(0.6)
        newSVGTitle4.add_updater(lambda newSVGTitle4: newSVGTitle4.next_to(rect1,UP,buff=0.75)) 
        self.play(Transform(newSVGTitle1,newSVGTitle4))
        # newSVGTitle1.clear_updaters()
        
        newSVGTitle5 = Text('<svg id="alipay">\n</svg>\n<svg id="hk">\n</svg>\n<svg id="boos">\n</svg>\n<svg id="bpi">\n</svg>').move_to([6.3,0,0])
        newSVGTitle5.scale(0.6)
        self.play(FadeIn(newSVGTitle5),newSVGTitle2.animate.shift(UP*1.7),newSVGTitle3.animate.shift(DOWN*1.7),run_time=2)
        self.wait(0.2)
        
        self.play(rect1.animate.shift(LEFT),alipay.animate.move_to([-4.25,0,0]),alipayHK.animate.move_to([-2.75,0,0]),boost.animate.move_to([-1.25,0,0]),bpi.animate.move_to([0.25,0,0]),newSVGTitle2.animate.shift(LEFT),newSVGTitle3.animate.shift(LEFT),newSVGTitle5.animate.shift(LEFT))
        
        # 排布嵌套的 svg
        newSVGTitle6 = Text('排布嵌套的 svg')
        newSVGTitle6.scale(0.6)
        newSVGTitle6.add_updater(lambda newSVGTitle6: newSVGTitle6.next_to(rect1,UP,buff=0.75))
        self.play(Transform(newSVGTitle1,newSVGTitle6))
        
        newSVGTitle7 = Text('<svg id="alipay">\n</svg>').move_to([5.3,0,0])
        newSVGTitle7.scale(0.6)
        self.play(FadeOut(alipayHK),FadeOut(boost),FadeOut(bpi),alipay.animate.move_to([-4.25,0.37,0]),Transform(newSVGTitle5,newSVGTitle7),newSVGTitle2.animate.shift(DOWN*1.2),newSVGTitle3.animate.shift(UP*1.2))
        self.play(rect1.animate.shift(RIGHT),alipay.animate.shift(RIGHT),FadeOut(newSVGTitle2),FadeOut(newSVGTitle3),FadeOut(newSVGTitle5))
        
        label1 = DecimalNumber()
        label1.move_to([1.5,-2,0])
        # label1.scale(0.6)
        label1.add_updater(logo_position_top)
        self.add(label1)
        
        label2 = DecimalNumber()
        label2.move_to([2.65,-2,0])
        # label2.scale(0.6)
        label2.add_updater(logo_position_left)
        self.add(label2)
        
        newSVGTitle8 = Text('<svg transform="translate(            ,                )">').move_to([0,-2,0])
        newSVGTitle8.scale(0.6)
        self.play(Create(newSVGTitle8),run_time=1)
        
        self.play(alipay.animate.move_to([-3.25,0,0]),run_time=3)
        self.play(alipay.animate.move_to([0,0,0]),run_time=5)
        self.play(alipay. animate.move_to([-3.25,0,0]),run_time=3)
        self.wait(5)
        
        # placeholder   
        self.wait(5)
        
class marginRemove(Scene):
    def construct(self):
        # 布局算法 title
        layoutTitle = Text('去除 margin 算法')
        self.add(layoutTitle)
        self.wait(2)
        self.play(FadeOut(layoutTitle,shift=DOWN),run_time=0.5)
        
        
        # 优化前方案
        method1Title = Text('优化前方案').move_to([0,2.5,0])
        self.add(method1Title)
        
        rect1 = Rectangle(width=8, height=1.25, color = WHITE)
        self.play(Create(rect1))
        
        br1 = Brace(rect1,direction=[1, 0, 0])
        self.add(br1)
        label2 = DecimalNumber()
        label2.move_to([5,0,0])
        label2.set_value(rect1.height*100)
        self.play(FadeIn(label2))
        
        alipay = SVGMobject("material/alipayplus.svg",width = 1.5).move_to([-5.5,2,0])
        self.play(Create(alipay),run_time=0.2)
        alipayHK = SVGMobject("material/AlipayHK.svg",width = 1.5).move_to([-5.5,1,0])
        self.play(Create(alipayHK),run_time=0.2)
        boost = SVGMobject("material/Boost.svg",width = 1.5).move_to([-5.5,0,0])
        self.play(Create(boost),run_time=0.2)
        bpi = SVGMobject("material/BPI.svg",width = 1.5).move_to([-5.5,-1,0])
        self.play(Create(bpi),run_time=0.2) 
        
        self.play(alipay.animate.move_to([-3.25,0,0]),alipayHK.animate.move_to([-1.75,0,0]),boost.animate.move_to([-0.25,0,0]),bpi.animate.move_to([1.25,0,0])) 
        
        
        rect2 = Rectangle(width=6, height=0.35, color = RED).move_to([-1,0,0])
        self.play(Create(rect2))
        
        br2 = Brace(rect2,direction=[-1, 0, 0])
        self.add(br2)
        label1 = DecimalNumber()
        label1.move_to([-5.4,0,0])
        label1.add_updater(lambda label1: label1.set_value(rect2.height*100))
        self.play(FadeIn(label1))

        group1 = VGroup(alipay, alipayHK, boost, bpi, rect2)
        
        self.play(group1.animate.shift(RIGHT).scale(1.34))
        self.play(FadeOut(rect1),FadeOut(br1),FadeOut(label2))
        
        rect3 = Rectangle(width=10, height=1, color = BLACK).move_to([0,0.76,0])
        rect3.set_fill(BLACK,1)
        rect4 = Rectangle(width=10, height=1, color = BLACK).move_to([0,-0.76,0])
        rect4.set_fill(BLACK,1)
        self.play(Create(rect3))
        self.play(Create(rect4))
        self.wait(2)
        marginRemove.clear(self)
        self.wait(1)
        
        # 优化后方案
        method1Title = Text('优化方案').move_to([0,2.5,0])
        self.add(method1Title)
        layoutTitle = Text('以左右分散布局为例').move_to([0,1.5,0]).scale(0.7)
        self.add(layoutTitle)
        
        rect1 = Rectangle(width=7, height=0.5, color = WHITE)
        self.play(Create(rect1))
        
        alipay = SVGMobject("material/alipayplus.svg",width = 1).move_to([-5.5,2,0])
        self.play(Create(alipay),run_time=0.2)
        alipayHK = SVGMobject("material/AlipayHK.svg",width = 1).move_to([-5.5,1,0])
        self.play(Create(alipayHK),run_time=0.2)
        boost = SVGMobject("material/Boost.svg",width = 1).move_to([-5.5,0,0])
        self.play(Create(boost),run_time=0.2)
        bpi = SVGMobject("material/BPI.svg",width = 1).move_to([-5.5,-1,0])
        self.play(Create(bpi),run_time=0.2) 
        
        self.play(alipay.animate.move_to([-3,0,0]),boost.animate.move_to([1,0,0]),bpi.animate.move_to([2,0,0]),alipayHK.animate.move_to([3,0,0])) 
        
        
        rect2 = Rectangle(width=0.8, height=0.25, color = RED).move_to([-3,0,0])
        self.play(Create(rect2))

        group1 = VGroup(alipay,rect2)
        self.play(group1.animate.scale(1.75).shift(RIGHT*0.22))
        
        rect3 = Rectangle(width=2.8, height=0.25, color = RED).move_to([2,0,0])
        self.play(Create(rect3))
        group2 = VGroup(alipayHK,boost,bpi,rect3)
        self.play(group2.animate.scale(1.75).shift(LEFT*0.93))
        
        rect4 = Rectangle(width=1, height=1, color = BLACK).move_to([-4,0,0])
        rect4.set_fill(BLACK,1)
        rect5 = Rectangle(width=1, height=1, color = BLACK).move_to([4,0,0])
        rect5.set_fill(BLACK,1)
        rect6 = Rectangle(width=8, height=1, color = BLACK).move_to([0,0.75,0])
        rect6.set_fill(BLACK,1)
        rect7 = Rectangle(width=8, height=1, color = BLACK).move_to([0,-0.75,0])
        rect7.set_fill(BLACK,1)
        line1 = Line([-2,0.21,0], [-1.5,0.21,0]).set_color(WHITE)
        line2 = Line([-2,-0.21,0], [-1.5,-0.21,0]).set_color(WHITE)
        self.play(FadeIn(rect4),FadeIn(rect5),FadeIn(rect6),FadeIn(rect7),FadeIn(line1),FadeIn(line2))
        self.play(FadeOut(rect2,shift=DOWN),FadeOut(rect3,shift=DOWN),FadeOut(rect1))
        marginRemove.clear(self)
        self.wait(1)
        
        # 优化方案特殊情况
        method1Title = Text('优化方案').move_to([0,2.5,0])
        self.add(method1Title)
        layoutTitle = Text('左右分散布局边界判断').move_to([0,1.5,0]).scale(0.7)
        self.add(layoutTitle)
        
        rect1 = Rectangle(width=6.5, height=0.5, color = WHITE)
        rect11 = Rectangle(width=6.5, height=2, color = WHITE)
        self.play(Create(rect1))
        
        alipay = SVGMobject("material/alipayplus.svg",width = 1).move_to([-5.5,2,0])
        self.play(Create(alipay),run_time=0.2)
        alipayHK = SVGMobject("material/AlipayHK.svg",width = 1).move_to([-5.5,1,0])
        self.play(Create(alipayHK),run_time=0.2)
        boost = SVGMobject("material/Boost.svg",width = 1).move_to([-5.5,0,0])
        self.play(Create(boost),run_time=0.2)
        bpi = SVGMobject("material/BPI.svg",width = 1).move_to([-5.5,-1,0])
        self.play(Create(bpi),run_time=0.2) 
        
        self.play(alipay.animate.move_to([-2.75,0,0]),boost.animate.move_to([0.75,0,0]),bpi.animate.move_to([1.75,0,0]),alipayHK.animate.move_to([2.75,0,0])) 
        
        self.play(Transform(rect1,rect11))
        
        
        rect2 = Rectangle(width=0.8, height=0.25, color = RED).move_to([-2.75,0,0])
        self.play(Create(rect2))

        group1 = VGroup(alipay,rect2)
        self.play(group1.animate.scale(1.75).shift(RIGHT*0.22))
        
        rect3 = Rectangle(width=2.8, height=0.25, color = RED).move_to([1.75,0,0])
        self.play(Create(rect3))
        
        group2 = VGroup(alipayHK,boost,bpi,rect3)
        self.play(group2.animate.scale(1.75).shift(LEFT*0.9))
        
        rect4 = Rectangle(width=1, height=5, color = BLACK).move_to([-3.79,0,0])
        rect4.set_fill(BLACK,1)
        rect5 = Rectangle(width=1, height=5, color = BLACK).move_to([3.79,0,0])
        rect5.set_fill(BLACK,1)
        rect6 = Rectangle(width=8, height=1, color = BLACK).move_to([0,1.54,0])
        rect6.set_fill(BLACK,1)
        rect7 = Rectangle(width=8, height=1, color = BLACK).move_to([0,-1.54,0])
        rect7.set_fill(BLACK,1)
        self.play(FadeIn(rect4),FadeIn(rect5),FadeIn(rect6),FadeIn(rect7))
        
        self.play(FadeOut(rect2,shift=DOWN),FadeOut(rect3,shift=DOWN))
        marginRemove.clear(self)
        self.wait(1)
        
        # 具体实现
        method1Title = Text('具体实现').move_to([0,2.5,0])
        self.add(method1Title)
        
        rect1 = Rectangle(width=7, height=0.5, color = WHITE)
        self.play(Create(rect1))
        
        alipay = SVGMobject("material/alipayplus.svg",width = 1).move_to([-5.5,2,0])
        self.play(Create(alipay),run_time=0.2)
        alipayHK = SVGMobject("material/AlipayHK.svg",width = 1).move_to([-5.5,1,0])
        self.play(Create(alipayHK),run_time=0.2)
        boost = SVGMobject("material/Boost.svg",width = 1).move_to([-5.5,0,0])
        self.play(Create(boost),run_time=0.2)
        bpi = SVGMobject("material/BPI.svg",width = 1).move_to([-5.5,-1,0])
        self.play(Create(bpi),run_time=0.2) 
        
        self.play(alipay.animate.move_to([-3,0,0]),boost.animate.move_to([1,0,0]),bpi.animate.move_to([2,0,0]),alipayHK.animate.move_to([3,0,0])) 
        
        newSVGTitle3 = Text('<svg>').move_to([-3.5,-0.8,0]).scale(0.6)
        newSVGTitle4 = Text('</svg>').move_to([-3.5,-3.2,0]).scale(0.6)
        
        newSVGTitle5 = Text('<g>\n  <svg id = "alipay">\n  </svg>\n  ......\n</g>').move_to([-2,-2,0])
        newSVGTitle5.scale(0.6)
        self.add(newSVGTitle3,newSVGTitle4,newSVGTitle5)
        
        newSVGTitle6 = Text('transform="translate(-3.06, 0)"',color = BLUE).move_to([2,-1.53,-1])
        newSVGTitle6.scale(0.4) 
        self.play(FadeIn(newSVGTitle6))    
        
        self.wait(0.5)
        
        shiftVar = 1.41
        
        self.play(alipay.animate.shift(RIGHT*shiftVar),boost.animate.shift(LEFT*shiftVar),bpi.animate.shift(LEFT*shiftVar),alipayHK.animate.shift(LEFT*shiftVar)) 
        
        newSVGTitle7 = Text('transform="scale(1.78)"',color = BLUE).move_to([-1,-1.17,0])
        
        self.wait(0.5)
        
        newSVGTitle7.scale(0.4) 
        self.play(FadeIn(newSVGTitle7))
        
        self.wait(0.5)
        group01 = VGroup(alipay,alipayHK,boost,bpi)
        self.play(group01.animate.scale(1.78))
        
        rect4 = Rectangle(width=1, height=1, color = BLACK).move_to([-4.04,0,0])
        rect4.set_fill(BLACK,1)
        rect5 = Rectangle(width=1, height=1, color = BLACK).move_to([4.04,0,0])
        rect5.set_fill(BLACK,1)
        rect6 = Rectangle(width=8, height=0.2, color = BLACK).move_to([0,0.39,0])
        rect6.set_fill(BLACK,1)
        rect7 = Rectangle(width=8, height=0.2, color = BLACK).move_to([0,-0.39,0])
        rect7.set_fill(BLACK,1)
        self.play(FadeIn(rect4),FadeIn(rect5),FadeIn(rect6),FadeIn(rect7))
        
        # placeholder   
        self.wait(5)
        
class illustrator(Scene):
    def construct(self):
        # 不兼容展示
        method1Title = SVGMobject("material/chrome.svg",width = 1).move_to([0,2,0])
        self.add(method1Title)
        
        method1Title2 = SVGMobject("material/illus.svg",width = 1.5).move_to([0,2,0])
        
        rect1 = Rectangle(width=7, height=0.5, color = WHITE)
        self.play(Create(rect1))
        
        alipay = SVGMobject("material/alipayplus.svg",width = 1).scale(2).move_to([-5.5,2,0])
        self.play(Create(alipay),run_time=0.2)

        
        self.play(alipay.animate.move_to([-3,0,0])) 
        
        newSVGTitle3 = Text('<svg>').move_to([-3.5,-0.8,0]).scale(0.6)
        newSVGTitle4 = Text('</svg>').move_to([-3.5,-3.2,0]).scale(0.6)
        
        newSVGTitle5 = Text('<g>\n  <svg id = "alipay">\n  </svg>\n  ......\n</g>').move_to([-2,-2,0])
        newSVGTitle5.scale(0.6) 
        self.add(newSVGTitle3,newSVGTitle4,newSVGTitle5)
        
        newSVGTitle6 = Text('transform = "scale(3, 0)"',color = BLUE).move_to([-1,-1.17,0])
        newSVGTitle6.scale(0.4) 
        newSVGTitle7 = Text('style="transform-origin: 0 20;"',color = BLUE).move_to([3,-1.17,-1])
        newSVGTitle7.scale(0.4) 
        self.play(FadeIn(newSVGTitle6),FadeIn(newSVGTitle7))
        
        self.wait(2)
        
        self.play(FadeOut(method1Title),FadeIn(method1Title2))
        
        self.wait(1)
        
        self.play(alipay.animate.shift(DOWN*0.2),newSVGTitle7.animate.set_color(RED))
        
        self.wait(3)
        
        illustrator.clear(self)
        
        
        # 兼容方案
        newSVGTitle6 = Text('transform = "scale(3, 0)" style="transform-origin: 0 20;"',color = BLUE).move_to([0,3,0]).scale(0.6)
        newSVGTitle7 = Text('transform = "???"',color = BLUE).move_to([0,1,0]).scale(0.6)
        self.play(Create(newSVGTitle6))
        
        self.wait(2)
        
        self.play(FadeOut(newSVGTitle6,shift=DOWN),FadeIn(newSVGTitle7,shift=DOWN))
        
        self.wait(3)
        illustrator.clear(self)
        
        # 实现原理
        
        numberplane = NumberPlane()
        self.add(numberplane)
        
        newSVGTitle6 = Text('transform = "scale(s1, 0)" style="transform-origin:x1 y1;"',color = WHITE).move_to([3.5,-2.5,0]).scale(0.4)
        newSVGTitle7 = Text('transform = "???"',color = BLUE).move_to([0,1,0]).scale(0.6)
        self.play(Create(newSVGTitle6))
        
        square = Square(color=BLUE, fill_opacity=1)
        self.add(square)
        dot = Dot([0, -1, 0],color=ORANGE)
        self.add(dot)
        self.wait(2)
        self.play(square.animate.scale(2).shift(UP))
        self.wait(2)
        illustrator.clear(self)
        
        numberplane = NumberPlane()
        self.add(numberplane)
        
        newSVGTitle6 = Text('transform = "translate(-x1,-y1) scale(s1, 0) translate(x1,y1)"',color = WHITE).move_to([3.5,-2.5,0]).scale(0.4)
        self.play(Create(newSVGTitle6))
        
        square = Square(color=BLUE, fill_opacity=1)
        self.add(square)
        
        dot = Dot([-1, 1, 0],color=ORANGE)
        self.add(dot)
        
        self.wait(1)
        
        self.play(square.animate.shift(LEFT*1).shift(UP*2))
        self.wait(1)
        self.play(square.animate.scale(2))
        self.wait(1)    
        self.play(square.animate.shift(RIGHT*1).shift(DOWN*2))
        self.wait(3)
        illustrator.clear(self)
        
        # 线性变换
        
        newSVGTitle6 = Text('transform = "....." style="transform-origin: x1 x2;"',color = BLUE).move_to([0,3,0]).scale(0.6)
        newSVGTitle7 = Text('transform = "matrix(?, ?, ?, ?, ?, ?)"',color = BLUE).move_to([0,1,0]).scale(0.6)
        self.play(Create(newSVGTitle6))
        
        self.wait(2)
        
        self.play(FadeOut(newSVGTitle6,shift=DOWN),FadeIn(newSVGTitle7,shift=DOWN))
        
        # placeholder   
        self.wait(5)
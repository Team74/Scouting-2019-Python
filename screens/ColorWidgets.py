from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.button import Button

Builder.load_string("""
<ColorLabel>:
    text_size: self.size
    halign: "center"
    valign: "middle"
    canvas.before:
        BorderImage:
            source: "background.jpg"
            pos: self.x - 1, self.y - 1
            size: self.width + 2, self.height + 2
        Color:
            rgb: self.rgb
        Rectangle:
            pos: self.pos
            size: self.size
<ColorButton>:
    text_size: self.size
    halign: "center"
    valign: "middle"
    background_normal: ""
    background_color: self.rgb
    canvas.before:
        BorderImage:
            source: "background.jpg"
            pos: self.x - 1, self.y - 1
            size: self.width + 2, self.height + 2
""") # uses BorderImage and Rectangle to outline every widget in white
# BACKGROUND IMAGE IS NEEDED to add borders to the widgets

class Color():
    """
        A way to store rgb values.
        """
    def __init__(self, r, g, b, a=1):
        self.r = r / 255
        self.g = g / 255
        self.b = b / 255
        self.a = a
    
    def mute(self, dimBy=30):
        """
            Dim each of the color values by 30.
            """
        dimBy = (dimBy / 255)
        self.r -= dimBy
        self.g -= dimBy
        self.b -= dimBy
    
    def muteNew(self, dimBy=30):
        """
            Return a new color with the color values dimmed by 30.
            """
        newColor = Color(self.r*255, self.g*255, self.b*255)
        newColor.mute(dimBy)
        return newColor
    
    def asTuple(self):
        """
            Return a tuple with the r, g, b values in that order.
            """
        return (self.r, self.g, self.b)
    
    def asTupleWithAlpha(self):
        """
            Return a tuple with the r, g, b, a values in that order.
            """
        return (self.r, self.g, self.b, self.a)
    
class Colors():
    """
        Enum for different default colors.
        """
    GREEN =         Color(0, 171, 40)
    ORANGE =        Color(225, 120, 45)
    YELLOW =        Color(225, 225, 72)
    BRIGHT_BLUE =   Color(75, 120, 250)
    LIGHT_BLUE =    Color(60, 100, 225)
    FAIR_BLUE =     Color(45, 80, 200)
    BLUE =          Color(30, 60, 175)
    DEEP_BLUE =     Color(15, 40, 150)
    DARK_BLUE =     Color(0, 20, 125)
    RED =           Color(185, 32, 32)
    FAIR_RED =      Color(210, 52, 52)
    LIGHT_RED =     Color(235, 72, 72)
    LIGHT_MAGENTA = Color(208, 107, 147)
    WHITE =         Color(225, 225, 225)

class ColorLabel(Label):
    def __init__(self, text, sizehint, color, **kwargs):
        self.rgb = color.asTuple()
        super(ColorLabel, self).__init__(text=str(text), size_hint=sizehint, **kwargs)

class ColorButton(Button):
    def __init__(self, text, sizehint, color, **kwargs):
        color = color.muteNew()
        self.rgb = color.asTupleWithAlpha()
        super(ColorButton, self).__init__(text=str(text), size_hint=sizehint, **kwargs)

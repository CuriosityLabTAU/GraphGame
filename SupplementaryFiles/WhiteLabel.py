from kivy.uix.label import Label
from kivy.properties import ListProperty

from kivy.factory import Factory
from kivy.lang import Builder

Builder.load_string("""
<WhiteLabel>:
  bcolor: 1, 1, 1, 1
  canvas.before:
    Color:
      rgba: self.bcolor
    Rectangle:

      pos: self.pos
      size: self.size
""")


class WhiteLabel(Label):
    bcolor = ListProperty([1, 1, 1, 1])
    font_size = 45
    color = [0.9, 0.9, 0.9, 1]
    size_hint_y = None
    size_hint_x = None

Factory.register('KivyB', module='WhiteLabel')
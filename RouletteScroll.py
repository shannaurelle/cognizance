from kivy.lang import Builder
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button


from kivymd.app import MDApp
from kivymd.effects.roulettescroll import RouletteScrollEffect
from kivymd.uix.list import OneLineListItem

class Test(MDApp):
    def build(self):
        # Preparing a `GridLayout` inside a `ScrollView`.
        layout = GridLayout(cols=1, padding=10, size_hint=(None, None), width=500)
        layout.bind(minimum_height=layout.setter('height'))

        for i in range(30):
            btn = Button(text=str(i), size=(480, 40), size_hint=(None, None))
            layout.add_widget(btn)

        root = ScrollView(
            size_hint=(None, None),
            size=(500, 320),
            pos_hint={'center_x': .5, 'center_y': .5},
            do_scroll_x=False,
        )
        root.effect_y = RouletteScrollEffect(anchor=20, interval=40)
        root.add_widget(layout)
        return root 

    def on_start(self):
        pass

Test().run()
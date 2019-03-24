import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button

class MyApp(App):
	def build(self):
		return Button(text="Hello!", background_color=(0, 0, 1, 1), font_size=150)

if __name__ == '__main__':
	MyApp().run()

#actieve_doelen = [dagelijkse_doelen, etc]
#dagelijkse_doelen = ...
# etc


from kivy.app import App
from kivy.uix.label import Label

class BasicApp(App):
    def build(self):
        label = Label(text="Hello World")
        return Label(text='Hello World')

app = BasicApp()
app.run()


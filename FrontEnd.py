#actieve_doelen = [dagelijkse_doelen, etc]
#dagelijkse_doelen = ...
# etc


from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class Checklist(App):
    def build(self):
        return BoxLayout()

app = Checklist()
app.run()


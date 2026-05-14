from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock

class RadheOmniAgent(App):
    def build(self):
        self.label = Label(text="Radhe AI: Waiting for your command...")
        Clock.schedule_interval(self.adaptive_role_check, 5)
        return self.label

    def adaptive_role_check(self, dt):
        # This allows me to switch roles autonomously based on your needs
        self.label.text = "Active Role: Multi-Task Assistant\nReady for any Job"

if __name__ == "__main__":
    RadheOmniAgent().run()

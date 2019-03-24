#---------------
#RandomApp
#---------------

#import
from kivy.app import App 

#import kivy.uix
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.anchorlayout import AnchorLayout 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.config import Config

#import python
import random

#window size
Config.set('graphics','resizeble', 0)
Config.set('graphics','width', 600)
Config.set('graphics','height', 400)

#--------------------------------------------------

class RandomApp(App):

#Update label
	def update_label(self):
		self.lbl.text = self.randCount	
#Random function
	def randFunc(self, instance):
		self.formula1 = float(self.txtinp.text)
		self.formula2 = float(self.txtinp2.text) 
		self.randCount = random.randint(self.formula1, self.formula2)
		self.randCount = str(self.randCount)
		self.update_label()
#Build app
	def build(self):	
#widgets and layout		
		bl = BoxLayout(
			orientation = 'vertical',
			size_hint = (1, .4))		
#text input
		self.txtinp = TextInput()		
		self.txtinp2 = TextInput()
#label
		self.lbl = Label(text = '0',
		 font_size = 40,
		 halign = 'center',
		 valign = 'top',
		 size_hint = (1, .5),
		 text_size = (200, 300))
#add widget		
		bl.add_widget(self.lbl)
		bl.add_widget(self.txtinp)
		bl.add_widget(self.txtinp2)
		bl.add_widget(Button(text = 'Get Random', on_press = self.randFunc))

		return bl
				
if __name__ == '__main__':
	RandomApp().run()		
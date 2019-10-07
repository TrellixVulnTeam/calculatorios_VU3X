from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.core.audio import SoundLoader
# core for window & apps this one is for mobile devices
from kivy.core.window import Window
from kivy.uix.button import Button


#Sounds
buttonsound = SoundLoader.load('sounds/button_click_0.wav') #button click
errorsound = SoundLoader.load('sounds/error.wav') #error click
clearsound = SoundLoader.load('sounds/clear_button_0_thanos_snap.wav') #clearing click
equalsound = SoundLoader.load('sounds/equal.wav') #equal click



class MainApp(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # mobile device screen for iphone or andriods
        Window.size = (300, 500)

        # creating a list for the numbers
        numbers = [7, 8, 9, '+', 4, 5, 6, '-', 1, 2, 3, '*', '.', 0, '(', ')', '/']
        self.numbers = self.ids.numbers

        # Number clearing
        numbers_clear = ['C', 'Ca']  # clear, clear all
        self.numbers = self.ids.numbers

        # number display, font, and bck color for them
        for number in numbers:
            button = Button(text=str(number),
                            font_size='30px',
                            background_color=(1, 0, 0, 1)
                            )
            # once user click on the button, it will pass an instance val to the function
            # value will be saved and display on the screen
            button.bind(on_release=self.echo_number)
            #Sound play of clicking a #
            button.bind(on_press=lambda *args: buttonsound.play())
            self.numbers.add_widget(button)

        # clear number on display for user
        for number in numbers_clear:
            clear_button = Button(text=str(number),
                                  font_size='30px',
                                  background_color=(1, 2, 2, .7)
                                  )
            clear_button.bind(on_release=self.echo_number)
            self.numbers.add_widget(clear_button)

        # = symbol now on display for user
        equal_button = Button(text='=',
                              font_size='30px',
                              background_color=(1, 2, 2, .7)
                              )
        button.bind(on_release=self.echo_number)
        equal_button.bind(on_release=self.eval_number)
        self.numbers.add_widget(equal_button)

    # text of your func, will aquire the value of the user input,
    # each new # user has added it will be saved and expand with new numbers that are inputed
    def echo_number(self, instance):
        input = self.ids.input
        input.text += instance.text

        # condition if CA or c has been clicked by the user
        if instance.text == 'Ca':  # deletes everything
            input.text = ''
            # Sound play for clearing data on calculator
            clearsound.play()
        elif instance.text == 'C':  # deletes 1 number
            input.text = input.text[:-2]
            # Sound play for clearing data on calculator
            clearsound.play()


    def eval_number(self, text):
        try:
            input = self.ids.input
            expression = input.text
            eva = eval(expression)  # perform math operations
            input.text = str(eva)
            equalsound.play()
        except:
        # error plays and display error message
           errorsound.play()
           input.text = 'Error! \(x_x\) Tap Ca'


class mainapp(App):
    def build(self):
        return MainApp()


if __name__ == '__main__':
    mainapp().run()


#Made by Jonathan K Almawi

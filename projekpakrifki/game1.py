import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen, ScreenManager

class MathPuzzleScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.add_widget(self.layout)

        self.question_label = Label(text='Pertanyaan: ')
        self.layout.add_widget(self.question_label)

        self.answer_input = TextInput(hint_text='Masukkan jawaban', multiline=False)
        self.layout.add_widget(self.answer_input)

        self.submit_button = Button(text='Kirim Jawaban')
        self.submit_button.bind(on_press=self.check_answer)
        self.layout.add_widget(self.submit_button)

        self.back_button = Button(text='Kembali')
        self.back_button.bind(on_press=self.go_back)
        self.layout.add_widget(self.back_button)

        self.generate_question()

    def generate_question(self):
        self.num1 = random.randint(1, 1000)
        self.num2 = random.randint(1, 1000)
        self.question_label.text = f'Berapa {self.num1} + {self.num2}?'
        self.correct_answer = self.num1 + self.num2

    def check_answer(self, instance):
        try:
            user_answer = int(self.answer_input.text)
            if user_answer == self.correct_answer:
                self.show_popup('Benar!', 'Jawaban Anda benar!')
            else:
                self.show_popup('Salah!', 'Jawaban Anda salah. Coba lagi!')
        except ValueError:
            self.show_popup('Error!', 'Masukkan angka yang valid.')
        
        self.answer_input.text = ''
        self.generate_question()

    def show_popup(self, title, message):
        popup = Popup(title=title, content=Label(text=message), size_hint=(None, None), size=(400, 200))
        popup.open()

    def go_back(self, instance):
        # Kembali ke layar utama
        self.manager.current = 'main'

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.add_widget(layout)

        label = Label(text='Selamat datang di Main Screen')
        layout.add_widget(label)

        start_button = Button(text='Mulai Math Puzzle')
        start_button.bind(on_press=self.start_puzzle)
        layout.add_widget(start_button)

    def start_puzzle(self, instance):
        self.manager.current = 'math_puzzle'

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(MathPuzzleScreen(name='math_puzzle'))
        return sm

if __name__ == '__main__':
    MyApp().run()

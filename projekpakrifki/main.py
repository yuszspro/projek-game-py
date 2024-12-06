from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.image import Image
import subprocess
import sys


class MainScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 15

        # Tambahkan logo atau gambar di atas
        self.add_widget(Image(source='logo.png', size_hint=(1, 0.4)))

        # Judul aplikasi
        title = Label(
            text='Selamat Datang di Aplikasi Game!',
            font_size=32,
            bold=True,
            color=(0.2, 0.6, 0.9, 1),
            halign='center',
        )
        self.add_widget(title)

        # Separator kosong untuk estetika
        self.add_widget(Widget(size_hint_y=None, height=10))

        # Tombol untuk setiap game
        btn_game1 = Button(
            text='Game 1: Hitung-Hitungan',
            size_hint=(1, 0.2),
            background_color=(0.2, 0.6, 0.9, 1),
            font_size=18,
        )
        btn_game1.bind(on_press=self.go_to_game1)
        self.add_widget(btn_game1)

        btn_game2 = Button(
            text='Game 2: Ular Tangga',
            size_hint=(1, 0.2),
            background_color=(0.9, 0.6, 0.2, 1),
            font_size=18,
        )
        btn_game2.bind(on_press=self.go_to_game2)
        self.add_widget(btn_game2)

        btn_game3 = Button(
            text='Game 3: Teka-Teki Menantang',
            size_hint=(1, 0.2),
            background_color=(0.6, 0.9, 0.2, 1),
            font_size=18,
        )
        btn_game3.bind(on_press=self.go_to_game3)
        self.add_widget(btn_game3)

    def go_to_game1(self, instance):
        # Jalankan game1.py
        subprocess.Popen([sys.executable, 'game1.py'])
        App.get_running_app().stop()  # Hentikan aplikasi utama

    def go_to_game2(self, instance):
        # Jalankan game2.py
        subprocess.Popen([sys.executable, 'game2.py'])
        App.get_running_app().stop()  # Hentikan aplikasi utama

    def go_to_game3(self, instance):
        # Jalankan game3.py
        subprocess.Popen([sys.executable, 'game3.py'])
        App.get_running_app().stop()  # Hentikan aplikasi utama


class MyApp(App):
    def build(self):
        self.title = "Aplikasi Game Seru"
        return MainScreen()


if __name__ == '__main__':
    MyApp().run()

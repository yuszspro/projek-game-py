import tkinter as tk
import random
from PIL import Image, ImageTk

class SnakeLadderGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Game Ular Tangga")
        
        self.players_position = [0, 0]  # Posisi kedua pemain
        self.current_player = 0  # Pemain yang sedang bermain (0 atau 1)
        self.dice_value = 0
        
        self.snake_image = None  # Placeholder untuk gambar ular
        self.create_widgets()
        self.load_images()  # Muat gambar
        self.create_board()
        self.create_questions()
        self.draw_board()
        

    def load_images(self):
        """Memuat gambar ular."""
        try:
            image = Image.open("snake.png")  # Ganti dengan path ke gambar Anda
            image = image.resize((100, 100), Image.Resampling.LANCZOS)  # Gunakan Resampling.LANCZOS
            self.snake_image = ImageTk.PhotoImage(image)
        except Exception as e:
            print("Gagal memuat gambar:", e)
            self.snake_image = None

        
    def create_widgets(self):
        self.label = tk.Label(self.master, text="Jawab soal matematika untuk melempar dadu!", font=("Arial", 10))
        self.label.pack(pady=5)
        
        self.question_label = tk.Label(self.master, text="", font=("Arial", 9))
        self.question_label.pack(pady=5)
        
        self.answer_entry = tk.Entry(self.master, width=10)
        self.answer_entry.pack(pady=5)
        
        self.submit_button = tk.Button(self.master, text="Submit Jawaban", command=self.check_answer)
        self.submit_button.pack(pady=5)
        
        self.roll_button = tk.Button(self.master, text="Roll Dadu", command=self.roll_dice, state=tk.DISABLED)
        self.roll_button.pack(pady=5)
        
        self.position_label = tk.Label(self.master, text="Posisi Pemain 1: 0 | Posisi Pemain 2: 0", font=("Arial", 9))
        self.position_label.pack(pady=5)
        
        self.turn_label = tk.Label(self.master, text="Giliran Pemain 1", font=("Arial", 9), fg="blue")
        self.turn_label.pack(pady=5)
        
        self.canvas = tk.Canvas(self.master, width=300, height=300)
        self.canvas.pack(pady=5)
        
        # Tambahkan gambar ular ke canvas
        if self.snake_image:
            self.canvas.create_image(150, 150, image=self.snake_image, anchor=tk.CENTER)
        
    def create_board(self):
        self.board = [0] * 100
        # Ular
        self.board[16] = 6
        self.board[18] = 8
        self.board[24] = 12
        # Tangga
        self.board[2] = 22
        self.board[10] = 28
        self.board[20] = 26
        
    def create_questions(self):
        self.questions = [
            ("5 + 3", 8),
            ("10 - 4", 6),
            ("6 * 2", 12),
            ("8 / 2", 4),
            ("7 + 5", 12),
            ("9 - 3", 6),
            ("3 * 3", 9),
            ("12 / 4", 3)
        ]
        self.current_question = None
        self.ask_question()
        
    def draw_board(self):
        self.canvas.delete("all")
        cell_size = 30  # Ukuran sel lebih kecil
        for i in range(10):  # Baris
            for j in range(10):  # Kolom
                row_number = 10 - i  # Baris dihitung dari bawah (1-10)
                if row_number % 2 == 0:  # Baris genap: angka menurun
                    num = (row_number - 1) * 10 + (10 - j)
                else:  # Baris ganjil: angka menaik
                    num = (row_number - 1) * 10 + (j + 1)
            
                x1 = j * cell_size
                y1 = i * cell_size
                x2 = x1 + cell_size
                y2 = y1 + cell_size
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill="white")
                self.canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text=str(num), font=("Arial", 7))
    
        # Gambar posisi pemain
        self.update_player_positions()
        
    def update_player_positions(self):
        cell_size = 30  # Ukuran sel lebih kecil
        colors = ["blue", "red"]  # Warna untuk masing-masing pemain
        for player, position in enumerate(self.players_position):
            if position < 100:
                row = 9 - (position // 10)  # Baris dihitung dari atas
                col = position % 10
                if (9 - row) % 2 == 1:  # Baris genap (dari bawah): angka menurun
                    col = 9 - col
            
                x = col * cell_size
                y = row * cell_size
                self.canvas.create_oval(x + 5, y + 5, x + cell_size - 5, y + cell_size - 5, fill=colors[player], outline="black")
        
    def ask_question(self):
        self.current_question = random.choice(self.questions)
        self.question_label.config(text=f"Berapa hasil dari {self.current_question[0]}?")
        self.answer_entry.delete(0, tk.END)
        self.roll_button.config(state=tk.DISABLED)
        
    def check_answer(self):
        try:
            answer = int(self.answer_entry.get())
            if answer == self.current_question[1]:
                self.label.config(text="Jawaban benar! Sekarang Anda bisa melempar dadu.")
                self.roll_button.config(state=tk.NORMAL)
            else:
                self.label.config(text="Jawaban salah! Giliran berpindah.")
                self.switch_turn()
        except ValueError:
            self.label.config(text="Masukkan angka yang valid.")
        
    def roll_dice(self):
        self.dice_value = random.randint(1, 6)
        self.label.config(text=f"Pemain {self.current_player + 1} melempar dadu dan mendapatkan: {self.dice_value}")

        # Cek apakah pemain tinggal beberapa kotak lagi tetapi hasil dadu terlalu besar
        remaining_steps = 99 - self.players_position[self.current_player]
        if self.dice_value > remaining_steps:
            self.label.config(text=f"Pemain {self.current_player + 1} mendapatkan {self.dice_value}, tetapi hanya tersisa {remaining_steps} langkah! Giliran berpindah.")
            self.switch_turn()
        else:
            self.move_player()

        
    def move_player(self):
        player = self.current_player
        self.players_position[player] += self.dice_value
        if self.players_position[player] >= 99:
            self.players_position[player] = 99
            self.label.config(text=f"Selamat! Pemain {player + 1} menang!")
            self.roll_button.config(state=tk.DISABLED)
            return
        
        # Cek ular atau tangga
        position = self.players_position[player]
        self.players_position[player] = self.board[position] if self.board[position] != 0 else position
        self.position_label.config(
            text=f"Posisi Pemain 1: {self.players_position[0] + 1} | Posisi Pemain 2: {self.players_position[1] + 1}"
        )
        
        # Gambar ulang papan untuk memperbarui posisi pemain
        self.draw_board()
        
        # Ganti giliran
        self.switch_turn()
        
    def switch_turn(self):
        self.current_player = 1 - self.current_player
        self.turn_label.config(text=f"Giliran Pemain {self.current_player + 1}", fg=["blue", "red"][self.current_player])
        self.ask_question()

if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeLadderGame(root)
    root.mainloop()

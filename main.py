import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


class BeerTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplicación de Bebedores de Cerveza de JThusberg")

        self.user_name_var = tk.StringVar()
        self.weekly_var = tk.DoubleVar()
        self.daily_var = tk.DoubleVar()

        self.create_ui()

    def create_ui(self):
        tk.Label(self.root, text="¡Bienvenido a la Aplicación de Bebedores de Cerveza de JThusberg!",
                 font=("Helvetica", 16)).pack(pady=10)

        tk.Label(self.root, text="Nombre:").pack()
        tk.Entry(self.root, textvariable=self.user_name_var).pack(pady=5)

        tk.Label(self.root, text="Cervezas por semana:").pack()
        tk.Entry(self.root, textvariable=self.weekly_var).pack(pady=5)

        tk.Label(self.root, text="Cervezas por día:").pack()
        tk.Entry(self.root, textvariable=self.daily_var).pack(pady=5)

        ttk.Button(self.root, text="Calcular", command=self.display_message).pack(pady=10)

        # Beer Bottle Image
        beer_image = Image.open("beer_bottle.png")
        beer_image = beer_image.resize((150, 300))
        beer_photo = ImageTk.PhotoImage(beer_image)
        beer_label = tk.Label(self.root, image=beer_photo)
        beer_label.image = beer_photo
        beer_label.pack(pady=10)

    def display_message(self):
        user_name = self.user_name_var.get()
        message = "eres un borracho"  # Display this message regardless of input

        self.show_result_message(user_name, message)

    def show_result_message(self, user_name, message):
        result_text = f"Hola, {user_name}!\n{message}"
        result_label = tk.Label(self.root, text=result_text, font=("Helvetica", 12))
        result_label.pack(pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    app = BeerTrackerApp(root)
    root.mainloop()
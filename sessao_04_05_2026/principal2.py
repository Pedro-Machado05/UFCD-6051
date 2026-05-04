import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk


class PortfolioApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Portefólio Pessoal")
        self.root.geometry("500x600")

        self.photo_path = None

        # FOTO
        self.photo_label = tk.Label(root, text="Sem imagem", width=25, height=10, bg="gray")
        self.photo_label.pack(pady=10)

        self.upload_btn = tk.Button(root, text="Carregar Foto", command=self.load_image)
        self.upload_btn.pack(pady=5)

        # NOME
        tk.Label(root, text="Nome").pack()
        self.name_entry = tk.Entry(root, width=40)
        self.name_entry.pack(pady=5)

        # CONTACTOS
        tk.Label(root, text="Contactos").pack()
        self.contact_entry = tk.Entry(root, width=40)
        self.contact_entry.pack(pady=5)

        # MORADA
        tk.Label(root, text="Morada").pack()
        self.address_entry = tk.Entry(root, width=40)
        self.address_entry.pack(pady=5)

        # INFO PESSOAL
        tk.Label(root, text="Informação Pessoal").pack()
        self.info_text = tk.Text(root, height=5, width=40)
        self.info_text.pack(pady=5)

        # BOTÃO GUARDAR
        self.save_btn = tk.Button(root, text="Guardar Portefólio", command=self.save_data)
        self.save_btn.pack(pady=20)

    def load_image(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Imagens", "*.png *.jpg *.jpeg")]
        )

        if file_path:
            self.photo_path = file_path
            img = Image.open(file_path)
            img = img.resize((150, 150))
            img = ImageTk.PhotoImage(img)

            self.photo_label.config(image=img, text="")
            self.photo_label.image = img

    def save_data(self):
        data = {
            "Nome": self.name_entry.get(),
            "Contactos": self.contact_entry.get(),
            "Morada": self.address_entry.get(),
            "Info": self.info_text.get("1.0", tk.END),
            "Foto": self.photo_path
        }

        print("Dados guardados:")
        print(data)

        messagebox.showinfo("Sucesso", "Portefólio guardado com sucesso!")


if __name__ == "__main__":
    root = tk.Tk()
    app = PortfolioApp(root)
    root.mainloop()
import tkinter as tk

class QuadroEletrico:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulador de Quadro Elétrico")

        self.canvas = tk.Canvas(root, width=400, height=500, bg="white")
        self.canvas.pack()

        # Estados
        self.geral = True
        self.diferencial = True
        self.luzes = True
        self.tomadas = True

        self.desenhar()

    def toggle(self, componente):
        setattr(self, componente, not getattr(self, componente))
        self.canvas.delete("all")
        self.desenhar()

    def desenhar(self):
        c = self.canvas

        # Geral
        cor = "green" if self.geral else "red"
        c.create_rectangle(150, 20, 250, 60, fill=cor)
        c.create_text(200, 40, text="CG")
        c.tag_bind("cg", "<Button-1>", lambda e: self.toggle("geral"))

        # Diferencial
        cor = "green" if self.diferencial and self.geral else "red"
        c.create_rectangle(150, 80, 250, 120, fill=cor)
        c.create_text(200, 100, text="Dif")
        c.tag_bind("dif", "<Button-1>", lambda e: self.toggle("diferencial"))

        # Linha principal
        c.create_line(200, 120, 200, 180)

        # Luzes
        cor = "green" if self.luzes and self.diferencial and self.geral else "red"
        c.create_rectangle(100, 180, 160, 220, fill=cor)
        c.create_text(130, 200, text="Dj Luz")

        c.create_line(130, 220, 130, 300)

        for i in range(3):
            c.create_oval(100 + i*30, 300, 120 + i*30, 320, fill=cor)

        # Tomadas
        cor = "green" if self.tomadas and self.diferencial and self.geral else "red"
        c.create_rectangle(240, 180, 300, 220, fill=cor)
        c.create_text(270, 200, text="Dj Tom")

        c.create_line(270, 220, 270, 300)
        c.create_rectangle(250, 300, 290, 340, fill=cor)

        # Ligações horizontais
        c.create_line(200, 180, 130, 180)
        c.create_line(200, 180, 270, 180)


root = tk.Tk()
app = QuadroEletrico(root)
root.mainloop()
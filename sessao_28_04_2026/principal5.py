import tkinter as tk

VOLTAGE = 230.0

# ---------- MODELO ----------
class Load:
    def __init__(self, power_w, leakage_ma=0.0):
        self.power_w = power_w
        self.leakage_ma = leakage_ma  # fuga para terra (mA)

    @property
    def current(self):
        return self.power_w / VOLTAGE


class Breaker:
    def __init__(self, name, limit_a):
        self.name = name
        self.limit_a = limit_a
        self.enabled = True
        self.tripped = False

    def reset(self):
        self.tripped = False

    def trip_if_needed(self, current_a):
        if self.enabled and current_a > self.limit_a:
            self.tripped = True


class Circuit:
    def __init__(self, breaker, loads):
        self.breaker = breaker
        self.loads = loads

    @property
    def current(self):
        if not self.breaker.enabled or self.breaker.tripped:
            return 0.0
        return sum(l.current for l in self.loads)

    @property
    def leakage_ma(self):
        if not self.breaker.enabled or self.breaker.tripped:
            return 0.0
        return sum(l.leakage_ma for l in self.loads)


class RCD:  # diferencial
    def __init__(self, threshold_ma=30.0):
        self.threshold_ma = threshold_ma
        self.enabled = True
        self.tripped = False

    def reset(self):
        self.tripped = False

    def trip_if_needed(self, leakage_ma):
        if self.enabled and leakage_ma > self.threshold_ma:
            self.tripped = True


class Board:
    def __init__(self):
        self.main = Breaker("CG", 40)
        self.rcd = RCD(30)

        self.c_lights = Circuit(
            Breaker("Dj Luz", 10),
            [Load(60), Load(60), Load(100)]
        )
        self.c_sockets = Circuit(
            Breaker("Dj Tom", 16),
            [Load(1000), Load(500, leakage_ma=10)]  # pequena fuga simulada
        )

        self.circuits = [self.c_lights, self.c_sockets]

    def simulate(self):
        # reset
        self.main.reset()
        self.rcd.reset()
        for c in self.circuits:
            c.breaker.reset()

        # correntes
        total_current = sum(c.current for c in self.circuits)
        total_leak = sum(c.leakage_ma for c in self.circuits)

        # proteções
        self.main.trip_if_needed(total_current)
        for c in self.circuits:
            c.breaker.trip_if_needed(c.current)

        self.rcd.trip_if_needed(total_leak)

        # corte geral se algo disparar
        if self.main.tripped or self.rcd.tripped:
            for c in self.circuits:
                c.breaker.enabled = False


# ---------- UI ----------
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Quadro Elétrico")
        self.root.geometry("500x600")
        self.root.configure(bg="#1e1e1e")

        self.board = Board()

        self.canvas = tk.Canvas(root, bg="#1e1e1e", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        tk.Button(root, text="Simular",
                  bg="#007acc", fg="white",
                  command=self.simular).pack(pady=10)

        self.draw()

    def color(self, ok):
        return "#2ecc71" if ok else "#e74c3c"

    def draw_breaker(self, x, y, text, active, tag):
        color = self.color(active)
        self.canvas.create_rectangle(x, y, x+80, y+40, fill=color, tags=tag)
        self.canvas.create_text(x+40, y+20, text=text, fill="white", tags=tag)
        self.canvas.tag_bind(tag, "<Button-1>", lambda e: self.toggle(tag))

    def toggle(self, tag):
        if tag == "main":
            self.board.main.enabled = not self.board.main.enabled
        elif tag == "rcd":
            self.board.rcd.enabled = not self.board.rcd.enabled
        elif tag == "luzes":
            self.board.c_lights.breaker.enabled = not self.board.c_lights.breaker.enabled
        elif tag == "tomadas":
            self.board.c_sockets.breaker.enabled = not self.board.c_sockets.breaker.enabled

        self.simular()

    def draw(self):
        c = self.canvas
        c.delete("all")

        b = self.board

        # estados
        main_ok = b.main.enabled and not b.main.tripped
        rcd_ok = b.rcd.enabled and not b.rcd.tripped

        # CG
        self.draw_breaker(210, 40, "CG", main_ok, "main")

        # linha
        c.create_line(250, 80, 250, 120, fill="white", width=2)

        # RCD
        self.draw_breaker(210, 120, "Dif", rcd_ok, "rcd")

        c.create_line(250, 160, 150, 200, fill="white", width=2)
        c.create_line(250, 160, 350, 200, fill="white", width=2)

        # Luzes
        luz_ok = main_ok and rcd_ok and b.c_lights.breaker.enabled and not b.c_lights.breaker.tripped
        self.draw_breaker(110, 200, "Luzes", luz_ok, "luzes")
        c.create_text(150, 260, text=f"{b.c_lights.current:.2f} A", fill="white")

        # Tomadas
        tom_ok = main_ok and rcd_ok and b.c_sockets.breaker.enabled and not b.c_sockets.breaker.tripped
        self.draw_breaker(310, 200, "Tomadas", tom_ok, "tomadas")
        c.create_text(350, 260, text=f"{b.c_sockets.current:.2f} A", fill="white")

    def simular(self):
        self.board.simulate()
        self.draw()


root = tk.Tk()
App(root)
root.mainloop()
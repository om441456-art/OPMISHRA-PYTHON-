import tkinter as tk


class PhoneCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Phone Calculator")
        self.root.geometry("280x400")
        self.root.resizable(False, False)
        self.root.configure(bg="#1f1f1f")

        self.first_number = None
        self.operator = None
        self.current_value = "0"
        self.just_pressed_operator = False

        self.display_var = tk.StringVar(value="0")

        display = tk.Entry(
            root,
            textvariable=self.display_var,
            font=("Arial", 24),
            justify="right",
            bd=10,
            relief="flat",
            state="readonly",
            readonlybackground="#2b2b2b",
            fg="white",
        )
        display.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=10)

        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "%", "+"],
        ]

        for r, row in enumerate(buttons, start=1):
            for c, label in enumerate(row):
                btn = tk.Button(
                    root,
                    text=label,
                    font=("Arial", 18),
                    width=4,
                    height=1,
                    command=lambda value=label: self.press(value),
                    bg="#3a3a3a",
                    fg="white",
                    bd=0,
                )
                btn.grid(row=r, column=c, padx=4, pady=4, sticky="nsew")

        clear_btn = tk.Button(
            root,
            text="C",
            font=("Arial", 16),
            width=4,
            height=1,
            command=self.clear,
            bg="#ff9500",
            fg="white",
            bd=0,
        )
        clear_btn.grid(row=5, column=0, padx=4, pady=4, sticky="nsew")

        equal_btn = tk.Button(
            root,
            text="=",
            font=("Arial", 16),
            width=4,
            height=1,
            command=self.calculate,
            bg="#ff9500",
            fg="white",
            bd=0,
        )
        equal_btn.grid(row=5, column=1, columnspan=3, padx=4, pady=4, sticky="nsew")

        for i in range(4):
            root.grid_columnconfigure(i, weight=1)
        for i in range(6):
            root.grid_rowconfigure(i, weight=1)

    def update_display(self):
        self.display_var.set(self.current_value)

    def press(self, value):
        if value.isdigit():
            self.add_number(value)
        elif value == ".":
            self.add_decimal()
        elif value in {"+", "-", "*", "/", "%"}:
            self.set_operator(value)
        elif value == "=":
            self.calculate()

    def add_number(self, number):
        if self.just_pressed_operator:
            self.current_value = number
            self.just_pressed_operator = False
        else:
            if self.current_value == "0":
                self.current_value = number
            else:
                self.current_value += number
        self.update_display()

    def add_decimal(self):
        if "." not in self.current_value:
            if self.just_pressed_operator:
                self.current_value = "0."
                self.just_pressed_operator = False
            else:
                self.current_value += "."
            self.update_display()

    def set_operator(self, op):
        if self.operator is not None and not self.just_pressed_operator:
            self.calculate()
        self.first_number = float(self.current_value)
        self.operator = op
        self.just_pressed_operator = True

    def calculate(self):
        if self.operator is None:
            return

        second_number = float(self.current_value)
        if self.operator == "+":
            result = self.first_number + second_number
        elif self.operator == "-":
            result = self.first_number - second_number
        elif self.operator == "*":
            result = self.first_number * second_number
        elif self.operator == "/":
            if second_number == 0:
                self.current_value = "Error"
                self.update_display()
                self.first_number = None
                self.operator = None
                self.just_pressed_operator = True
                return
            result = self.first_number / second_number
        else:
            if second_number == 0:
                self.current_value = "Error"
                self.update_display()
                self.first_number = None
                self.operator = None
                self.just_pressed_operator = True
                return
            result = self.first_number % second_number

        self.current_value = str(result)
        self.update_display()
        self.first_number = None
        self.operator = None
        self.just_pressed_operator = True

    def clear(self):
        self.first_number = None
        self.operator = None
        self.current_value = "0"
        self.just_pressed_operator = False
        self.update_display()


if __name__ == "__main__":
    root = tk.Tk()
    PhoneCalculator(root)
    root.mainloop()

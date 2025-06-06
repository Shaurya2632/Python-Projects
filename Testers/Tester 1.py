from tkinter import *
import re
from tkinter import messagebox

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")
        self.master.geometry("440x530")
        self.master.iconbitmap(r"D:\coding\python\images\Calc.ico")
        self.master.resizable(False, False)
        self.master.configure(bg="#000000")
        
        # Display
        self.equation = ""
        self.result_var = StringVar()
        self.result_var.set("0")
        self.just_calculated = False
        self.max_display_length = 14  # Maximum characters to display
        
        # Create display container
        self.display_container = Frame(self.master, bg="#000000", bd=0)
        self.display_container.pack(fill="x", padx=20, pady=(20, 10))
        
        # Display background - regular rectangle instead of rounded corners
        self.display_bg = Canvas(self.display_container, bg="#0a0a0a",
                                  highlightthickness=0, height=120)
        self.display_bg.pack(fill="x", expand=True)
        
        # History display
        self.history_var = StringVar()
        self.history_var.set("")
        self.history = Label(self.display_container, textvariable=self.history_var,
                               font=("Arial", 15), bg="#0a0a0a", fg="#888888", 
                               anchor="e", padx=15)
        self.history.place(x=20, y=15, width=380, height=40)
        
        # Main display
        self.result = Label(self.display_container, textvariable=self.result_var,
                              font=("Arial", 28, "bold"), bg="#0a0a0a", fg="#ffffff", 
                              anchor="e", padx=15)
        self.result.place(x=20, y=60, width=380, height=45)
        
        # Buttons container
        self.buttons_container = Frame(self.master, bg="#000000", bd=0)
        self.buttons_container.pack(fill="both", expand=True, padx=20, pady=10)
        
        # Configure grid for buttons
        for i in range(5):
            self.buttons_container.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.buttons_container.grid_columnconfigure(i, weight=1)
            
        # Button colors
        number_bg = "#1a1a1a"
        number_fg = "#ffffff"
        op_bg = "#444444"  # Gray operators
        op_fg = "#ffffff"
        func_bg = "#222222"
        func_fg = "#ffffff"
        equal_bg = "#1E88E5"  # Blue for equals button
        equal_fg = "#ffffff"
        
        # Button dictionary to store references
        self.buttons = {}
            
        # Create buttons
        self.create_button("C", 0, 0, bg=func_bg, fg=func_fg)
        self.create_button("±", 0, 1, bg=func_bg, fg=func_fg)
        self.create_button("%", 0, 2, bg=func_bg, fg=func_fg)
        self.create_button("/", 0, 3, bg=op_bg, fg=op_fg)
        
        self.create_button("7", 1, 0, bg=number_bg, fg=number_fg)
        self.create_button("8", 1, 1, bg=number_bg, fg=number_fg)
        self.create_button("9", 1, 2, bg=number_bg, fg=number_fg)
        self.create_button("*", 1, 3, bg=op_bg, fg=op_fg)
        
        self.create_button("4", 2, 0, bg=number_bg, fg=number_fg)
        self.create_button("5", 2, 1, bg=number_bg, fg=number_fg)
        self.create_button("6", 2, 2, bg=number_bg, fg=number_fg)
        self.create_button("-", 2, 3, bg=op_bg, fg=op_fg)
        
        self.create_button("1", 3, 0, bg=number_bg, fg=number_fg)
        self.create_button("2", 3, 1, bg=number_bg, fg=number_fg)
        self.create_button("3", 3, 2, bg=number_bg, fg=number_fg)
        self.create_button("+", 3, 3, bg=op_bg, fg=op_fg)
        
        self.create_button("0", 4, 0, columnspan=2, bg=number_bg, fg=number_fg)
        self.create_button(".", 4, 2, bg=number_bg, fg=number_fg)
        self.create_button("=", 4, 3, bg=equal_bg, fg=equal_fg)
        
        # Bind keyboard keys
        self.master.bind("<Key>", self.key_press)
    
    def create_button(self, text, row, column, columnspan=1, bg="#222222", fg="#ffffff"):
        # Create regular flat button without rounded corners
        button = Button(
            self.buttons_container,
            text=text, 
            font=("Arial", 18, "bold"),
            bd=0, 
            relief=FLAT,
            command=lambda t=text: self.button_click(t),
            bg=bg, 
            fg=fg,
            activebackground="#555555", 
            activeforeground="#ffffff",
            cursor="hand2"
        )
        
        # Place the button directly in the grid
        button.grid(row=row, column=column, columnspan=columnspan, padx=5, pady=5, sticky="nsew")
        
        # Store button reference
        self.buttons[text] = {"button": button, "default_bg": bg, "default_fg": fg}
        
        # Add hover effects
        button.bind("<Enter>", lambda e, t=text: self.on_button_hover(t, True))
        button.bind("<Leave>", lambda e, t=text: self.on_button_hover(t, False))
        
        # Add click visual
        button.bind("<Button-1>", lambda e, t=text: self.on_button_press(t))
        button.bind("<ButtonRelease-1>", lambda e, t=text: self.on_button_release(t))
        
    def on_button_hover(self, text, is_hover):
        button = self.buttons[text]["button"]
        default_bg = self.buttons[text]["default_bg"]
        
        if is_hover:
            # Brighten button on hover
            r, g, b = button.winfo_rgb(default_bg)
            r, g, b = min(r + 12000, 65535), min(g + 12000, 65535), min(b + 12000, 65535)
            hover_color = f"#{r//256:02x}{g//256:02x}{b//256:02x}"
            button.config(bg=hover_color)
        else:
            # Restore default color
            button.config(bg=default_bg)
    
    def on_button_press(self, text):
        button = self.buttons[text]["button"]
        default_bg = self.buttons[text]["default_bg"]
        
        # Darken button on press
        r, g, b = button.winfo_rgb(default_bg)
        r, g, b = max(r - 15000, 0), max(g - 15000, 0), max(b - 15000, 0)
        press_color = f"#{r//256:02x}{g//256:02x}{b//256:02x}"
        button.config(bg=press_color)
        
    def on_button_release(self, text):
        self.on_button_hover(text, True)
    
    def key_press(self, event):
        """Handle keyboard input"""
        key = event.char
        if key in "0123456789.+-*/":
            self.button_click(key)
        elif key == "\r":  # Enter key
            self.button_click("=")
        elif key == "\x08":  # Backspace
            if self.equation:
                self.equation = self.equation[:-1]
                if not self.equation:
                    self.equation = "0"
                self.result_var.set(self.equation)
                
                # Update display with formatted number if applicable
                try:
                    if all(c in "0123456789.-" for c in self.equation):
                        # If it's just a number, format it
                        value = float(self.equation) if "." in self.equation else int(self.equation)
                        displayed_value = self.format_number(value)
                        self.result_var.set(displayed_value)
                except:
                    pass
    
    def format_number(self, num):
        """Format a number for display with proper formatting"""
        # Convert to string first
        num_str = str(num)
        
        # Handle special case for negative numbers to avoid display issues
        is_negative = num < 0
        abs_num = abs(num)
        abs_num_str = str(abs_num)
        
        # For large integers or large floats, use scientific notation
        if isinstance(num, int) and len(abs_num_str) > self.max_display_length - (1 if is_negative else 0):
            return f"{num:.8e}"
        
        # For floats with many decimal places
        if isinstance(num, float):
            # If the number has more than max_display_length digits total
            if len(abs_num_str) > self.max_display_length - (1 if is_negative else 0):
                # Check if it's a very small number
                if 0.0001 > abs_num > 0:
                    return f"{num:.8e}"
                    
                # For numbers with many decimal places, limit them
                # Count digits before decimal
                int_part = int(abs_num)
                int_digits = len(str(int_part))
                
                # Calculate how many decimal places we can show
                decimal_places = max(0, self.max_display_length - int_digits - 1 - (1 if is_negative else 0))  # -1 for decimal point
                if decimal_places <= 0:
                    return f"{num:.0f}"
                
                # Format with calculated decimal places
                return f"{num:.{decimal_places}f}"
            
            # Check if it's an integer value stored as float
            if num == int(num):
                return str(int(num))
        
        # For smaller integers and well-formatted floats, return as is
        return num_str
    
    def button_click(self, text):
        if text == "C":
            self.equation = ""
            self.result_var.set("0")
            self.history_var.set("")
            self.just_calculated = False
        
        elif text == "=":
            try:
                # Save previous equation for history
                old_equation = self.equation
                
                # Fix potential formatting issues
                temp_equation = self.equation.replace("%", "/100")
                
                # Handle expressions ending with operators
                last_char = temp_equation[-1] if temp_equation else ""
                if last_char in "+-*/":
                    temp_equation = temp_equation[:-1]
                
                # Evaluate and format result
                if temp_equation:
                    result = eval(temp_equation)
                    
                    # Format the result properly
                    formatted_result = self.format_number(result)
                    
                    # Ensure display fits by truncating history if needed
                    if len(old_equation) > 20:
                        display_history = "..." + old_equation[-17:] + " ="
                    else:
                        display_history = old_equation + " ="
                    
                    # Update history and display
                    self.history_var.set(display_history)
                    self.result_var.set(formatted_result)
                    
                    # Store the actual numeric result
                    self.equation = str(result)
                    self.just_calculated = True
            except Exception:
                messagebox.showerror("Error", "Invalid Input")
                self.equation = ""
                self.result_var.set("0")
                self.history_var.set("")
                self.just_calculated = False
        
        elif text == "±":
            if not self.equation:
                self.equation = "0"
            
            try:
                # Convert to float to handle expressions
                value = float(self.equation)
                # Negate the value
                value = -value
                # Convert back to string
                self.equation = str(value) if value != int(value) else str(int(value))
                # Update display with formatted value
                self.result_var.set(self.format_number(value))
            except:
                # If it's not a simple number, just add a negative sign
                if self.equation and self.equation[0] == "-":
                    self.equation = self.equation[1:]
                else:
                    self.equation = "-" + self.equation
                self.result_var.set(self.equation)
        
        else:
            # Handle numeric and operator inputs
            current_display = self.result_var.get()
            
            # Prevent multiple decimal points in a number
            if text == ".":
                # Find the last number in the equation
                parts = re.split(r'[+\-*/]', self.equation)
                last_number = parts[-1] if parts else ""
                
                if "." in last_number:
                    return
            
            # Prevent multiple operators in a row
            if text in "+-*/" and self.equation and self.equation[-1] in "+-*/":
                self.equation = self.equation[:-1] + text
                self.result_var.set(self.equation)
                return
                
            # Start fresh after a calculation result
            if self.just_calculated and text.isdigit():
                self.history_var.set("")
                self.equation = text
                self.just_calculated = False
            elif self.just_calculated:
                # If an operator is pressed after calculation, continue with result
                self.history_var.set("")
                self.just_calculated = False
                self.equation += text
            elif self.equation == "" or current_display == "0":
                if text == ".":
                    self.equation = "0."
                elif text in "+-*/":
                    self.equation = "0" + text
                else:
                    self.equation = text
            else:
                self.equation += text
            
            # Display equation, applying formatting for numbers if needed
            try:
                if all(c in "0123456789.-" for c in self.equation):
                    # If it's just a number, format it
                    value = float(self.equation) if "." in self.equation else int(self.equation)
                    displayed_value = self.format_number(value)
                    
                    # Ensure value fits in display by reducing font size if needed
                    if len(displayed_value) > 12:
                        self.result.config(font=("Arial", 24, "bold"))
                    elif len(displayed_value) > 10:
                        self.result.config(font=("Arial", 26, "bold"))
                    else:
                        self.result.config(font=("Arial", 28, "bold"))
                        
                    self.result_var.set(displayed_value)
                else:
                    # If it's an expression, show as is
                    if len(self.equation) > 12:
                        self.result.config(font=("Arial", 24, "bold"))
                    elif len(self.equation) > 10:
                        self.result.config(font=("Arial", 26, "bold"))
                    else:
                        self.result.config(font=("Arial", 28, "bold"))
                    
                    # Truncate extremely long equations in display
                    if len(self.equation) > 20:
                        display_eq = "..." + self.equation[-17:]
                        self.result_var.set(display_eq)
                    else:
                        self.result_var.set(self.equation)
            except:
                # If there's any error in formatting, show the raw equation
                self.result_var.set(self.equation)

if __name__ == "__main__":
    root = Tk()
    calculator = Calculator(root)
    root.mainloop()

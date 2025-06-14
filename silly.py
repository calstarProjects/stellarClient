import tkinter as tk
from tkinter import messagebox, simpledialog

class MainApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Main Window")
        self.root.geometry("400x300")
        
        # Create buttons for different subwindow types
        tk.Button(self.root, text="Open Modal Dialog", 
                 command=self.open_modal_dialog).pack(pady=10)
        
        tk.Button(self.root, text="Open Non-Modal Window", 
                 command=self.open_non_modal).pack(pady=10)
        
        tk.Button(self.root, text="Open Settings Window", 
                 command=self.open_settings).pack(pady=10)
        
        tk.Button(self.root, text="Simple Input Dialog", 
                 command=self.simple_input).pack(pady=10)
        
        tk.Button(self.root, text="Custom Dialog", 
                 command=self.custom_dialog).pack(pady=10)
        
        self.settings_window = None  # Keep reference to prevent multiple opens
    
    def open_modal_dialog(self):
        """Modal dialog - blocks interaction with main window"""
        dialog = tk.Toplevel(self.root)
        dialog.title("Modal Dialog")
        dialog.geometry("300x200")
        dialog.transient(self.root)  # Make it appear on top of main window
        dialog.grab_set()  # Make it modal (blocks main window)
        
        tk.Label(dialog, text="This is a modal dialog.\nMain window is blocked.").pack(pady=20)
        tk.Button(dialog, text="Close", command=dialog.destroy).pack(pady=10)
        
        # Center the dialog
        dialog.update_idletasks()  # Ensure geometry is calculated
        x = (dialog.winfo_screenwidth() // 2) - (dialog.winfo_width() // 2)
        y = (dialog.winfo_screenheight() // 2) - (dialog.winfo_height() // 2)
        dialog.geometry(f"+{x}+{y}")
    
    def open_non_modal(self):
        """Non-modal window - can interact with both windows"""
        window = tk.Toplevel(self.root)
        window.title("Non-Modal Window")
        window.geometry("250x150")
        
        tk.Label(window, text="This is independent!\nYou can use both windows.").pack(pady=20)
        tk.Button(window, text="Close", command=window.destroy).pack(pady=10)
    
    def open_settings(self):
        """Settings window - prevents multiple instances"""
        if self.settings_window is not None and self.settings_window.winfo_exists():
            self.settings_window.lift()  # Bring to front if already open
            return
            
        self.settings_window = tk.Toplevel(self.root)
        self.settings_window.title("Settings")
        self.settings_window.geometry("300x250")
        self.settings_window.transient(self.root)
        
        # Create settings interface
        tk.Label(self.settings_window, text="Application Settings", 
                font=("Arial", 12, "bold")).pack(pady=10)
        
        # Example settings
        frame = tk.Frame(self.settings_window)
        frame.pack(pady=10)
        
        tk.Label(frame, text="Theme:").grid(row=0, column=0, sticky="w", padx=5)
        theme_var = tk.StringVar(value="Light")
        tk.OptionMenu(frame, theme_var, "Light", "Dark").grid(row=0, column=1, padx=5)
        
        tk.Label(frame, text="Font Size:").grid(row=1, column=0, sticky="w", padx=5)
        font_var = tk.IntVar(value=12)
        tk.Spinbox(frame, from_=8, to=24, textvariable=font_var, width=10).grid(row=1, column=1, padx=5)
        
        # Buttons
        button_frame = tk.Frame(self.settings_window)
        button_frame.pack(pady=20)
        
        tk.Button(button_frame, text="Apply", 
                 command=lambda: self.apply_settings(theme_var.get(), font_var.get())).pack(side="left", padx=5)
        tk.Button(button_frame, text="Cancel", 
                 command=self.settings_window.destroy).pack(side="left", padx=5)
    
    def apply_settings(self, theme, font_size):
        print(f"Applied settings: Theme={theme}, Font Size={font_size}")
        messagebox.showinfo("Settings", f"Settings applied!\nTheme: {theme}\nFont Size: {font_size}")
        self.settings_window.destroy()
    
    def simple_input(self):
        """Using built-in simpledialog"""
        name = simpledialog.askstring("Input", "Enter your name:")
        if name:
            messagebox.showinfo("Result", f"Hello, {name}!")
    
    def custom_dialog(self):
        """Custom dialog with return value"""
        result = CustomDialog(self.root).result
        if result:
            messagebox.showinfo("Result", f"You entered: {result}")
    
    def run(self):
        self.root.mainloop()


class CustomDialog:
    def __init__(self, parent):
        self.result = None
        
        # Create dialog window
        self.dialog = tk.Toplevel(parent)
        self.dialog.title("Custom Dialog")
        self.dialog.geometry("300x150")
        self.dialog.transient(parent)
        self.dialog.grab_set()
        
        # Center the dialog
        self.dialog.update_idletasks()
        x = (self.dialog.winfo_screenwidth() // 2) - (self.dialog.winfo_width() // 2)
        y = (self.dialog.winfo_screenheight() // 2) - (self.dialog.winfo_height() // 2)
        self.dialog.geometry(f"+{x}+{y}")
        
        # Create interface
        tk.Label(self.dialog, text="Enter some text:").pack(pady=10)
        
        self.entry = tk.Entry(self.dialog, width=30)
        self.entry.pack(pady=5)
        self.entry.focus()  # Set focus to entry
        
        # Buttons
        button_frame = tk.Frame(self.dialog)
        button_frame.pack(pady=20)
        
        tk.Button(button_frame, text="OK", command=self.ok_clicked).pack(side="left", padx=5)
        tk.Button(button_frame, text="Cancel", command=self.cancel_clicked).pack(side="left", padx=5)
        
        # Bind Enter key to OK
        self.dialog.bind('<Return>', lambda e: self.ok_clicked())
        self.dialog.bind('<Escape>', lambda e: self.cancel_clicked())
        
        # Wait for dialog to close
        self.dialog.wait_window()
    
    def ok_clicked(self):
        self.result = self.entry.get()
        self.dialog.destroy()
    
    def cancel_clicked(self):
        self.result = None
        self.dialog.destroy()


if __name__ == "__main__":
    app = MainApp()
    app.run()
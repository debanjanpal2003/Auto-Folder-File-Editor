import os
import tkinter as tk
from tkinter import messagebox, ttk
import sys

class FileEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Auto-Folder File Editor")
        self.root.geometry("700x550")

        self.file_map = {}
        
        # AUTOMATIC FOLDER SELECTION:
        # This detects the folder where the script (or .bat) is running from
        self.current_folder = os.path.dirname(os.path.abspath(__file__))

        # --- UI Layout ---
        tk.Label(root, text=f"Working Directory:", font=("Arial", 10, "bold")).pack(pady=(10, 0))
        self.lbl_folder = tk.Label(root, text=self.current_folder, fg="green", wraplength=600)
        self.lbl_folder.pack(pady=5)

        # File Dropdown
        tk.Label(root, text="Select File from Folder or Subfolders:").pack(pady=(10, 0))
        self.file_var = tk.StringVar()
        self.dropdown = ttk.Combobox(self.root, textvariable=self.file_var, state="readonly", width=80)
        self.dropdown.pack(pady=5)
        self.dropdown.bind("<<ComboboxSelected>>", self.load_file_content)

        # Content Area
        tk.Label(root, text="File Content (Paste here):").pack(pady=(10, 0))
        self.text_area = tk.Text(root, height=18, width=85)
        self.text_area.pack(pady=5, padx=10)

        # Save Button
        self.btn_save = tk.Button(root, text="Save Content", bg="#28a745", fg="white", font=("Arial", 10, "bold"), command=self.save_content)
        self.btn_save.pack(pady=10)

        # Initial scan
        self.refresh_file_list()

    def refresh_file_list(self):
        self.file_map = {}
        file_list = []

        for root_dir, dirs, files in os.walk(self.current_folder):
            for file in files:
                # Avoid showing the script itself and the .bat file in the list
                if file == "editor.py" or file.endswith(".bat"):
                    continue
                    
                full_path = os.path.join(root_dir, file)
                rel_path = os.path.relpath(full_path, self.current_folder)
                self.file_map[rel_path] = full_path
                file_list.append(rel_path)

        self.dropdown['values'] = file_list
        if not file_list:
            messagebox.showwarning("Empty Folder", "No editable files found in this directory.")

    def load_file_content(self, event=None):
        selected_rel_path = self.file_var.get()
        full_path = self.file_map.get(selected_rel_path)

        if full_path:
            try:
                with open(full_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, content)
            except Exception as e:
                messagebox.showerror("Error", f"Could not read file: {e}")

    def save_content(self):
        selected_rel_path = self.file_var.get()
        full_path = self.file_map.get(selected_rel_path)

        if not full_path:
            messagebox.showwarning("Warning", "Please select a file first!")
            return

        new_content = self.text_area.get(1.0, tk.END)
        # Remove the extra newline Tkinter adds at the end
        if new_content.endswith('\n'):
            new_content = new_content[:-1]
        
        try:
            with open(full_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            messagebox.showinfo("Success", f"Updated: {selected_rel_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = FileEditorApp(root)
    root.mainloop()
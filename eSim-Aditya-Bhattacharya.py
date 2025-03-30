import tkinter as tk
from tkinter import messagebox, ttk
import subprocess

# Define the list of tools with installation commands
install_commands = {
    "gcc": "sudo apt install gcc -y",
    "g++": "sudo apt install g++ -y",
    "cmake": "sudo apt install cmake -y",
    "python3": "sudo apt install python3 -y",
    "git": "sudo apt install git -y",
    "make": "sudo apt install make -y",
    "vim": "sudo apt install vim -y",
    "ngspice": "sudo apt install ngspice -y",
    "kicad": "sudo apt install kicad -y",
    "verilator": "sudo apt install verilator -y",
    "gtkwave": "sudo apt install gtkwave -y",
}

# Function to list available tools
def list_tools():
    tools_text.delete(1.0, tk.END)  # Clear previous text
    tools_text.insert(tk.END, "Available Development Tools:\n\n")
    for tool, command in install_commands.items():
        tools_text.insert(tk.END, f"{tool} → {command}\n")

# Function to install selected tool
def install_tool():
    tool = tool_var.get()
    if tool in install_commands:
        try:
            tools_text.insert(tk.END, f"\nInstalling {tool}...\n")
            root.update()
            process = subprocess.Popen(install_commands[tool], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            
            for line in process.stdout:
                tools_text.insert(tk.END, line)
                tools_text.see(tk.END)
                root.update_idletasks()
            
            process.wait()
            if process.returncode == 0:
                messagebox.showinfo("Success", f"{tool} installed successfully!")
            else:
                messagebox.showerror("Error", f"Failed to install {tool}")
        except subprocess.CalledProcessError:
            messagebox.showerror("Error", f"Installation failed for {tool}")

# Function to update selected tool
def update_tool():
    tool = tool_var.get()
    if tool:
        try:
            tools_text.insert(tk.END, f"\nUpdating {tool}...\n")
            root.update()
            subprocess.run(f"sudo apt upgrade {tool} -y", shell=True, check=True)
            messagebox.showinfo("Success", f"{tool} updated successfully!")
        except subprocess.CalledProcessError:
            messagebox.showerror("Error", f"Failed to update {tool}")

# Function to check version of selected tool
def check_version():
    tool = tool_var.get()
    if tool:
        try:
            result = subprocess.run(f"{tool} --version", shell=True, capture_output=True, text=True)
            if result.returncode == 0:
                messagebox.showinfo("Version Info", result.stdout.split('\n')[0])
            else:
                messagebox.showerror("Error", f"Version check failed for {tool}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to check version for {tool}")

# GUI Setup
root = tk.Tk()
root.title("Dev Tool Manager")
root.geometry("600x450")
root.configure(bg="#1e1e1e")

# Header Label
header_label = tk.Label(root, text="Development Tool Manager", font=("Arial", 16, "bold"), fg="white", bg="#1e1e1e")
header_label.pack(pady=10)

# Tool Selection Dropdown
tool_var = tk.StringVar()
tool_dropdown = ttk.Combobox(root, textvariable=tool_var, values=list(install_commands.keys()), state="readonly", font=("Arial", 12))
tool_dropdown.pack(pady=5)
tool_dropdown.set("Select a tool")

# Buttons Frame
button_frame = tk.Frame(root, bg="#1e1e1e")
button_frame.pack(pady=10)

btn_style = {"width": 15, "height": 2, "font": ("Arial", 10, "bold"), "bg": "#3498db", "fg": "white", "bd": 0}

tk.Button(button_frame, text="List Tools", command=list_tools, **btn_style).grid(row=0, column=0, padx=5, pady=5)
tk.Button(button_frame, text="Install", command=install_tool, **btn_style).grid(row=0, column=1, padx=5, pady=5)
tk.Button(button_frame, text="Update", command=update_tool, **btn_style).grid(row=0, column=2, padx=5, pady=5)
tk.Button(button_frame, text="Check Version", command=check_version, **btn_style).grid(row=0, column=3, padx=5, pady=5)

# Text Box for Displaying Logs
tools_text = tk.Text(root, height=10, width=60, bg="black", fg="green", font=("Courier", 10))
tools_text.pack(pady=10)
tools_text.insert(tk.END, "Click 'List Tools' to see available tools.\n")

# Start GUI
root.mainloop()

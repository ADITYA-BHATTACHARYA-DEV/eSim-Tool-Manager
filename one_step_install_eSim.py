import tkinter as tk
from tkinter import messagebox, ttk
import subprocess

# Define eSim-related tools and their installation commands
install_commands = {
    "ngspice": "sudo apt install ngspice -y",
    "kicad": "sudo apt install kicad -y",
    "verilator": "sudo apt install verilator -y",
    "gtkwave": "sudo apt install gtkwave -y",
    "scilab": "sudo apt install scilab -y",
    "openmodelica": "sudo apt install openmodelica -y",
    "nghdl": "sudo apt install ghdl -y",
    "freehdl": "sudo apt install freehdl -y",
}

def list_tools():
    tools_text.delete(1.0, tk.END)
    tools_text.insert(tk.END, "Available eSim Tools:\n\n")
    for tool, command in install_commands.items():
        tools_text.insert(tk.END, f"{tool} → {command}\n")

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

def install_all_tools():
    tools_text.insert(tk.END, "\nInstalling all eSim tools...\n")
    root.update()
    command = "sudo apt install " + " ".join(install_commands.keys()) + " -y"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    for line in process.stdout:
        tools_text.insert(tk.END, line)
        tools_text.see(tk.END)
        root.update_idletasks()
    process.wait()
    if process.returncode == 0:
        messagebox.showinfo("Success", "All eSim tools installed successfully!")
    else:
        messagebox.showerror("Error", "Failed to install some tools")

def install_esim():
    try:
        tools_text.insert(tk.END, "\nInstalling eSim...\n")
        root.update()
        command = "git clone --depth=1 https://github.com/FOSSEE/eSim.git && cd eSim && ./install.sh"
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        for line in process.stdout:
            tools_text.insert(tk.END, line)
            tools_text.see(tk.END)
            root.update_idletasks()
        process.wait()
        if process.returncode == 0:
            messagebox.showinfo("Success", "eSim installed successfully!")
        else:
            messagebox.showerror("Error", "Failed to install eSim")
    except Exception as e:
        messagebox.showerror("Error", "eSim installation failed")

# GUI Setup
root = tk.Tk()
root.title("eSim Tool Manager")
root.geometry("600x500")
root.configure(bg="#1e1e1e")

header_label = tk.Label(root, text="eSim Tool Manager", font=("Arial", 16, "bold"), fg="white", bg="#1e1e1e")
header_label.pack(pady=10)

tool_var = tk.StringVar()
tool_dropdown = ttk.Combobox(root, textvariable=tool_var, values=list(install_commands.keys()), state="readonly", font=("Arial", 12))
tool_dropdown.pack(pady=5)
tool_dropdown.set("Select a tool")

button_frame = tk.Frame(root, bg="#1e1e1e")
button_frame.pack(pady=10)

btn_style = {"width": 18, "height": 2, "font": ("Arial", 10, "bold"), "bg": "#3498db", "fg": "white", "bd": 0}

tk.Button(button_frame, text="List Tools", command=list_tools, **btn_style).grid(row=0, column=0, padx=5, pady=5)
tk.Button(button_frame, text="Install Tool", command=install_tool, **btn_style).grid(row=0, column=1, padx=5, pady=5)
tk.Button(button_frame, text="Install All Tools", command=install_all_tools, **btn_style).grid(row=1, column=0, padx=5, pady=5)
tk.Button(button_frame, text="Install eSim", command=install_esim, **btn_style).grid(row=1, column=1, padx=5, pady=5)

# Log Display
tools_text = tk.Text(root, height=12, width=70, bg="black", fg="green", font=("Courier", 10))
tools_text.pack(pady=10)
tools_text.insert(tk.END, "Click 'List Tools' to see available eSim tools.\n")

# Start GUI
root.mainloop()

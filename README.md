


# 🚀 Automated Tool Manager

## 📌 Overview

The **Automated Tool Manager** is a powerful command-line interface (CLI) application designed to automate the **installation, updating, and management** of essential development tools on **Linux-based systems**. 

Developers often require tools like **GCC, CMake, Python, Git, Vim, and Make** for setting up their development environment. Instead of manually installing and updating each tool separately, this CLI automates the process, ensuring that all necessary dependencies are correctly handled and installed efficiently.

By using this tool, users can **quickly install, update, or list development tools** with simple and easy-to-remember commands. The tool leverages **Python's Click module** for a user-friendly command-line experience and **Rich module** for improved text formatting and table display.

---

## **📌 Features**

✅ **Automated Installation** – Install essential development tools with a single command.  
✅ **Easy Updates** – Update installed tools to their latest versions.  
✅ **List Available Tools** – View all supported tools with their installation commands.  
✅ **Interactive Command-Line Interface (CLI)** – Uses `click` and `rich` for better user experience.  
✅ **Logging Support** – Keeps a log of installed and updated tools for reference.  
✅ **Lightweight & Fast** – Minimal system resource usage while executing tasks.  

---

## **📌 Prerequisites**

Before installing the **Automated Tool Manager**, ensure that your system meets the following requirements:

### **🖥 System Requirements**
- **OS**: Linux (Ubuntu 20.04+, Debian-based distributions)
- **Python**: Python 3.8+
- **Permissions**: Root or `sudo` access for package installation

### **🔹 Required Dependencies**
To ensure the smooth functioning of the tool, we need to install some dependencies:

- **Poetry** – A dependency and package manager for Python projects.
- **Click** – A Python library used to create command-line interfaces.
- **Rich** – A Python library that provides enhanced CLI output, including tables and color formatting.

---

## **📌 Installation Guide**

### **1️⃣ Install pipx and Poetry**
`pipx` is a tool for installing Python CLI applications in isolated environments. `Poetry` is used for dependency management.

```bash
sudo apt update && sudo apt install pipx -y
pipx ensurepath
pipx install poetry
```

### **2️⃣ Set Up the Project Directory**
To begin, create a dedicated directory for the tool:

```bash
mkdir dev-tool-manager && cd dev-tool-manager
```

Now, initialize a Poetry project inside this directory:

```bash
poetry init
```

When prompted, enter **dev-tool-manager** as the package name.

Accept the default values or customize them as needed.

### **3️⃣ Install Required Dependencies**
To ensure smooth execution of the tool, install the necessary Python libraries:

```bash
poetry add click rich
```

### **4️⃣ Create the CLI Script**
Inside the **dev-tool-manager** directory, create a Python file named **dev_tool_manager.py**:

```bash
nano dev_tool_manager.py
```

Paste the following Python code:

```python
import os
import subprocess
import click
from rich.console import Console
from rich.table import Table
import logging

console = Console()
logging.basicConfig(filename="dev_tool_manager.log", level=logging.INFO, format="%(asctime)s - %(message)s")

TOOLS = {
    "gcc": {"install": "sudo apt install gcc -y", "update": "sudo apt upgrade gcc -y"},
    "g++": {"install": "sudo apt install g++ -y", "update": "sudo apt upgrade g++ -y"},
    "cmake": {"install": "sudo apt install cmake -y", "update": "sudo apt upgrade cmake -y"},
    "python3": {"install": "sudo apt install python3 -y", "update": "sudo apt upgrade python3 -y"},
    "git": {"install": "sudo apt install git -y", "update": "sudo apt upgrade git -y"},
    "make": {"install": "sudo apt install make -y", "update": "sudo apt upgrade make -y"},
    "vim": {"install": "sudo apt install vim -y", "update": "sudo apt upgrade vim -y"}
}

@click.group()
def cli():
    """Automated Tool Manager for Linux Development"""
    pass

@click.command()
@click.argument("tool_name")
def install(tool_name):
    """Install a specified development tool."""
    if tool_name not in TOOLS:
        console.print(f"[red]Error: {tool_name} is not a supported tool.[/red]")
        return
    console.print("[yellow]Updating package lists before installation...[/yellow]")
    subprocess.run("sudo apt update", shell=True, check=True)
    subprocess.run(TOOLS[tool_name]["install"], shell=True, check=True)
    console.print(f"[green]{tool_name} installed successfully![/green]")
    logging.info(f"Installed {tool_name}")

@click.command()
@click.argument("tool_name")
def update(tool_name):
    """Update a specified development tool."""
    if tool_name not in TOOLS:
        console.print(f"[red]Error: {tool_name} is not a supported tool.[/red]")
        return
    subprocess.run(TOOLS[tool_name]["update"], shell=True, check=True)
    console.print(f"[green]{tool_name} updated successfully![/green]")
    logging.info(f"Updated {tool_name}")

@click.command()
def list_tools():
    """List all available development tools."""
    table = Table(title="Available Development Tools")
    table.add_column("Tool", style="cyan", justify="left")
    table.add_column("Installation Command", style="magenta", justify="left")
    for tool, commands in TOOLS.items():
        table.add_row(tool, commands["install"])
    console.print(table)

cli.add_command(install)
cli.add_command(update)
cli.add_command(list_tools)

if __name__ == "__main__":
    cli()
```

Save and exit (CTRL+X → Y → Enter).

---

## **📌 Usage**

### **✅ Install a Development Tool**
```bash
dev-tool-manager install gcc
dev-tool-manager install cmake
```

### **✅ Update a Development Tool**
```bash
dev-tool-manager update git
dev-tool-manager update python3
```

### **✅ List All Available Tools**
```bash
dev-tool-manager list-tools
```

---
![Screenshot 2025-03-30 085420](https://github.com/user-attachments/assets/fb770ce2-835c-406e-9f31-3cb3c3183021)

![Screenshot 2025-03-30 092224](https://github.com/user-attachments/assets/e8eaa903-7b5a-4d98-9a35-94e888e678c6)
![Screenshot 2025-03-30 092147](https://github.com/user-attachments/assets/a043ec45-1cb9-483d-b8e3-b6b45a1bc35a)
![Screenshot 2025-03-30 092135](https://github.com/user-attachments/assets/23d027ba-28a8-41fe-8c90-2d036ec4c427)
![Screenshot 2025-03-30 090730](https://github.com/user-attachments/assets/aae3343b-0db6-491a-bfc4-a0ed6d582eac)
![Screenshot 2025-03-30 085526](https://github.com/user-attachments/assets/ba256de6-a96f-485f-9b9f-55c2ac99f4b9)
![Screenshot 2025-03-30 085511](https://github.com/user-attachments/assets/3a6241ab-1be7-477c-8136-055f47e4063c)

## **📌 License**

This project is licensed under the **MIT License**. Feel free to use and modify it!

---

## **👥 Contributors**

- **Aditya Bhattacharya** 



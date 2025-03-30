📌 README.md - Automated Tool Manager
markdown
Copy
Edit
# 🚀 Automated Tool Manager

## 📌 Overview
The **Automated Tool Manager** is a command-line interface (CLI) tool designed to simplify the **installation, updating, and management of essential development tools** on **Linux-based systems**. 

Developers often require tools such as **GCC, CMake, Python, Git, Vim, and Make** to set up a development environment. Instead of installing and managing each tool separately, this CLI automates the process and ensures that all dependencies are properly handled.

## ✅ Features
- **Automated Installation** – Quickly install essential development tools.
- **One-Click Updates** – Easily update installed tools.
- **List Available Tools** – View all supported tools with installation commands.
- **User-Friendly CLI** – Uses `click` and `rich` for an interactive experience.
- **Logging Support** – Tracks installation and update history.
- **Lightweight & Fast** – Minimal overhead for system performance.

---

## 📌 Prerequisites
Before installing the **Automated Tool Manager**, ensure your system meets the following requirements:

### 🖥 System Requirements
- **OS**: Linux (Ubuntu 20.04+, Debian-based distributions)
- **Python**: Python 3.8+
- **Permissions**: Root or `sudo` access for package installation

### 🔹 Required Dependencies
- **Poetry** – Dependency and package manager.
- **Click** – Command-line interface framework.
- **Rich** – Provides a better UI with tables and colored text.

---

## 📌 Installation Guide

### **1️⃣ Install pipx and Poetry**
`pipx` installs Python CLI tools in isolated environments. `Poetry` handles dependencies.

```bash
sudo apt update && sudo apt install pipx -y
pipx ensurepath
pipx install poetry
💡 Tip: If you get a pipx: command not found error, restart your terminal.

2️⃣ Set Up the Project Directory
Create a directory for the tool:

bash
Copy
Edit
mkdir dev-tool-manager && cd dev-tool-manager
Now, initialize a Poetry project:

bash
Copy
Edit
poetry init
Enter dev-tool-manager as the package name.

Accept default values or customize as needed.

3️⃣ Install Required Dependencies
Install click and rich for CLI functionality and output formatting:

bash
Copy
Edit
poetry add click rich
4️⃣ Create the CLI Script
Inside the project directory, create a Python file:

bash
Copy
Edit
nano dev_tool_manager.py
Add the following code:

python
Copy
Edit
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
Save and exit (CTRL+X → Y → Enter).

5️⃣ Convert into a Package
bash
Copy
Edit
mkdir -p dev_tool_manager
mv dev_tool_manager.py dev_tool_manager/__main__.py
touch dev_tool_manager/__init__.py
6️⃣ Configure pyproject.toml
Edit the pyproject.toml file:

bash
Copy
Edit
nano pyproject.toml
Modify the contents:

toml
Copy
Edit
[tool.poetry]
name = "dev-tool-manager"
version = "0.1.0"
description = "A CLI tool to manage Linux development tools"
authors = ["Your Name <your.email@example.com>"]
readme = "README.md"
packages = [{include = "dev_tool_manager"}]

[tool.poetry.dependencies]
python = "^3.8"
click = "^8.1.3"
rich = "^13.5.2"

[tool.poetry.scripts]
dev-tool-manager = "dev_tool_manager.__main__:cli"
7️⃣ Build and Install the Package
bash
Copy
Edit
poetry build
pipx install dist/dev-tool-manager-0.1.0-py3-none-any.whl
dev-tool-manager --help
📌 Usage
✅ Install a Development Tool
bash
Copy
Edit
dev-tool-manager install gcc
dev-tool-manager install cmake
✅ Update a Development Tool
bash
Copy
Edit
dev-tool-manager update git
✅ List Available Tools
bash
Copy
Edit
dev-tool-manager list-tools
📌 Troubleshooting
Issue	Solution
Command not found	Run pipx install dev-tool-manager again.
Permission denied	Use sudo before running the command.
Poetry not found	Run pipx install poetry and retry.
ModuleNotFoundError: click	Ensure dependencies are installed: poetry add click rich
📌 Testing
🔍 Test the CLI Functionality
Run:

bash
Copy
Edit
dev-tool-manager --help
It should display the available commands.

🔍 Verify Installation
Try installing a tool:

bash
Copy
Edit
dev-tool-manager install vim
Then check:

bash
Copy
Edit
vim --version
📌 License
This project is licensed under the MIT License.

🎯 Your CLI tool is now fully functional and ready for deployment! 🚀

markdown
Copy
Edit

This README follows **GitHub Markdown format** with **proper headings, bullet points, and code snippets

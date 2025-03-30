📌 Automated Tool Manager
🔹 Overview
The Automated Tool Manager is a command-line interface (CLI) tool designed to simplify the installation, updating, and management of essential development tools on Linux-based systems. This tool eliminates the need for users to manually install or update development packages by automating the process using predefined commands.

Developers often need essential tools such as GCC, CMake, Python, Git, Vim, and Make to set up a development environment. Instead of installing each tool separately, this CLI automates the process and ensures that all dependencies are properly installed.

📌 Features and Benefits
🔧 Key Features
✔️ Automated Installation → Quickly install essential development tools like gcc, git, cmake, and more.
✔️ One-Click Updates → Ensure all tools are up to date without manually running multiple commands.
✔️ List Available Tools → View all supported tools along with their installation commands.
✔️ User-friendly CLI → Simple commands with color-coded output for better readability.
✔️ Logging Support → Saves installation and update history for debugging and tracking.
✔️ Lightweight & Fast → Uses Python’s Click and Rich libraries for quick execution.
✔️ Easy Integration → Ideal for automated development environment setup in CI/CD pipelines.

📌 Prerequisites
Before installing and using the Automated Tool Manager, ensure you meet the following system requirements:

🖥 System Requirements
✅ Operating System: Linux (Ubuntu 20.04+, Debian-based distributions)
✅ Python Version: Python 3.8+ installed
✅ User Permissions: Root or sudo privileges for package installation

🔹 Required Dependencies
The tool requires the following Python libraries for execution:

Poetry → Manages dependencies and project packaging.

Click → Handles command-line interaction.

Rich → Provides better UI output with tables and colored text.

📌 Installation Guide
Follow these detailed step-by-step instructions to install and set up the Automated Tool Manager.

1️⃣ Install pipx and Poetry
pipx allows installing Python CLI tools in isolated environments, preventing dependency conflicts.
Poetry is used for dependency and package management.

Run the following commands to install them:

bash
Copy
Edit
sudo apt update && sudo apt install pipx -y
pipx ensurepath
pipx install poetry
💡 Note: If you encounter a pipx: command not found error, restart your terminal and try again.

2️⃣ Set Up the Project Directory
Create a directory for the tool and navigate into it:

bash
Copy
Edit
mkdir dev-tool-manager && cd dev-tool-manager
Now, initialize a new Poetry project:

bash
Copy
Edit
poetry init
When prompted, enter the package name: dev-tool-manager

Accept default values or customize them as per your needs.

3️⃣ Install Required Dependencies
Install the Click and Rich libraries, which are required for the CLI functionality and output formatting:

bash
Copy
Edit
poetry add click rich
4️⃣ Create the CLI Script
Inside the dev-tool-manager directory, create a Python file:

bash
Copy
Edit
nano dev_tool_manager.py
Now, add the following Python code:

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
bash
Copy
Edit
nano pyproject.toml
Modify the file:

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
✅ Install a Development Tool:

bash
Copy
Edit
dev-tool-manager install gcc
dev-tool-manager install cmake
✅ Update a Development Tool:

bash
Copy
Edit
dev-tool-manager update git
✅ List Available Tools:

bash
Copy
Edit
dev-tool-manager list-tools
📌 Troubleshooting
Issue	Solution
Command not found	Run pipx install dev-tool-manager again.
Permission denied	Use sudo before running the command.
Poetry not found	Run pipx install poetry and retry.
📌 License
📜 This project is licensed under the MIT License.

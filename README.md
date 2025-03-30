
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

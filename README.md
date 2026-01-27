# \# GOPH 547

# 

# \*Semester: \* W2026

# \*Instructor: \*B. Karchewski

# \*Author: Arezou Hadi Najafabadi

# 

# An example repository setup for a simple Python package.
Project Description

The goal of Lab 0 is to practice:
- using a virtual environment to isolate dependencies 
- using NumPy and Matplotlib for basic arrays + visualization
- organizing code in a clean GitHub repo with a Python package structure

## What we need to implement and solve this python programming on Windows:

- **Python 3.8+**
- **git**
- (Recommended) **VS Code** or another editor
 
### Step 1) Download the repository

### Step 2) Create a virtual environment
A *virtual environment* keeps this project’s packages separate from your other Python projects.
-In **PowerShell** (from the repo root):
```powershell
python -m venv .venv
```

Activate it:
```powershell
.\.venv\Scripts\Activate.ps1
```

If Windows blocks activation, run this once (PowerShell):
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```
then try activation again.

You should now see `(.venv)` at the start of your terminal line
### Step 3) Install this package (and its dependencies)

From the repo root (with `(.venv)` active):
```powershell
pip install -e .
```

Why `-e`?
- It installs the package in “developer mode”, meaning if you edit your code, the next run will use your updates automatically.
- This also installs NumPy + Matplotlib (and Pillow if listed as a dependency)
### Step 4) Run the lab script

```powershell
python examples\driver.py
```

### Step 5) What you should see / get as output as TA

`driver.py` prints results for the NumPy array questions (1–9) and then loads/plots the image tasks (10–16). 

At the end, it saves a figure:
- `examples/rock_canyon_RGB_summary.png` 

That figure should contain **two subplots**, each with **four curves** (R, G, B, and mean RGB). 

---

Installation Instructions

git clone https://github.com/Arezou-hadi/goph547-w2026-lab00-stAH.git
cd goph547-w2026-lab00-stAH

# Includes examples using NumPy arrays and Matplotlib for visualization.

## Option B: Run directly on GitHub 
This is useful if we don’t want to install Python or packages on our laptop yet. Also, it is recommended and easier for this assignment and it can be considered as great experience for future to use git and github in future (especially in case we have to share our own code with others!)
### Step 1) Create a Codespace
1. Open the repo on GitHub
2. Click **Code** → **Codespaces** tab → **Create codespace on main**

GitHub opens VS Code in your browser with a terminal.

### Step 2) Install + run
In the Codespaces terminal:
```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
python examples/driver.py
```

### Step 3) Download the output plot
- In the file browser, open `examples/`
- You should see `rock_canyon_RGB_summary.png`
- Right-click → download (or open it in the browser)

---

## Project structure 

After we run the driver script, our repo should have this general structure:

goph547-w2026-lab00-stAH/
|-- .venv/                    # not committed to git
|-- src/
|   |-- goph547lab00/
|       |-- __init__.py
|       |-- arrays.py
|-- examples/
|   |-- driver.py
|   |-- rock_canyon.jpg
|   |-- rock_canyon_RGB_summary.png
|-- .gitignore
|-- LICENSE
|-- pyproject.toml
|-- README.md


# 


# Setting Up Python Virtual Environment (venv)

## Why Use a Virtual Environment?

- **Isolation**: Keep project dependencies separate from system Python
- **No conflicts**: Different projects can use different package versions
- **Clean**: Easy to delete and recreate if something goes wrong
- **Professional**: Industry standard practice

## Step-by-Step Setup

### 1. Open VS Code Terminal
- **View** → **Terminal** (or press `` Ctrl+` `` / `` Cmd+` ``)
- Make sure you're in the project folder: `python-learning-journey`

### 2. Create Virtual Environment

**Windows:**
```bash
python -m venv venv
```

**Mac/Linux:**
```bash
python3 -m venv venv
```

This creates a folder called `venv` with its own Python installation.

### 3. Activate Virtual Environment

**Windows (Command Prompt):**
```bash
venv\Scripts\activate
```

**Windows (PowerShell):**
```bash
venv\Scripts\Activate.ps1
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

You'll see `(venv)` appear at the start of your terminal prompt - this means it's active!

### 4. Install Required Packages

Now install packages in your isolated environment:

```bash
# Upgrade pip first
pip install --upgrade pip

# Install Jupyter and data science basics
pip install jupyter notebook ipykernel

# Install essential libraries
pip install pandas numpy matplotlib

# Install ipython for better interactive experience
pip install ipython
```

### 5. Select Python Interpreter in VS Code

**Method 1: Command Palette**
1. Press `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (Mac)
2. Type: "Python: Select Interpreter"
3. Choose the one that shows `('./venv': venv)`

**Method 2: Bottom Status Bar**
1. Look at the bottom-left of VS Code
2. Click on the Python version shown
3. Select the interpreter from `./venv`

### 6. Register Kernel for Jupyter

This makes your venv available in Jupyter notebooks:

```bash
python -m ipykernel install --user --name=python-learning --display-name "Python (Learning)"
```

### 7. Test It Works

Open your notebook (`notebooks/01_getting_started.ipynb`):
1. Click "Select Kernel" in the top-right
2. Choose "Python (Learning)" or the venv interpreter
3. Run a cell to test!

## VS Code Will Remember!

Once set up, VS Code will automatically:
- Activate your venv when you open the terminal
- Use the venv for running Python files
- Use the venv for Jupyter notebooks

## Daily Workflow

**Opening Project:**
- Just open the folder in VS Code
- VS Code auto-activates venv in terminal
- You're ready to code!

**If venv not activated in terminal:**
```bash
# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

## Deactivating Virtual Environment

When you're done (usually not needed, just close VS Code):
```bash
deactivate
```

## Troubleshooting

### PowerShell Execution Policy Error (Windows)

If you get an error like "cannot be loaded because running scripts is disabled":

**Option 1: Use Command Prompt instead of PowerShell**
- In VS Code terminal, click the dropdown
- Select "Command Prompt"

**Option 2: Change PowerShell policy (one-time)**
Open PowerShell as Administrator and run:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### "Python not found" in venv

Make sure you're using:
- `python` on Windows
- `python3` on Mac/Linux

### Jupyter Kernel Not Showing

```bash
# Make sure venv is activated, then:
python -m ipykernel install --user --name=python-learning
```

## Managing Packages

**Install new package:**
```bash
pip install package-name
```

**See installed packages:**
```bash
pip list
```

**Save your dependencies (for sharing):**
```bash
pip freeze > requirements.txt
```

**Install from requirements file:**
```bash
pip install -r requirements.txt
```

## Git & Virtual Environment

Good news! The `.gitignore` file already excludes the `venv/` folder.

**What this means:**
- Your venv won't be uploaded to GitHub
- Others can create their own venv
- Keeps your repository clean and small

**Sharing your project:**
Others will run:
```bash
# Clone your repo
git clone your-repo-url
cd python-learning-journey

# Create their own venv
python -m venv venv
source venv/bin/activate  # or activate on Windows

# Install dependencies
pip install -r requirements.txt
```

## Quick Command Reference

```bash
# Create venv
python -m venv venv

# Activate
venv\Scripts\activate              # Windows CMD
venv\Scripts\Activate.ps1          # Windows PowerShell  
source venv/bin/activate           # Mac/Linux

# Deactivate
deactivate

# Install packages
pip install package-name

# List packages
pip list

# Save dependencies
pip freeze > requirements.txt

# Install from requirements
pip install -r requirements.txt
```

## VS Code Settings (Optional)

To make VS Code always activate venv in new terminals:

1. Open Settings: `Ctrl+,` or `Cmd+,`
2. Search: "Python: Terminal Activate Environment"
3. Make sure it's checked ✓

---

**You're now following professional Python development practices!** 🎉

Next steps:
1. Create your venv
2. Activate it
3. Install packages
4. Select interpreter in VS Code
5. Start coding!

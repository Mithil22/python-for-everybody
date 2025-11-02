# Complete Setup Guide

## Step 1: Install Required VS Code Extensions

1. Open VS Code
2. Click the Extensions icon (or press `Ctrl+Shift+X` / `Cmd+Shift+X`)
3. Search and install these extensions:
   - **Python** (by Microsoft)
   - **Jupyter** (by Microsoft)
   - **GitLens** (optional but helpful for Git visualization)
   - **Python Indent** (helps with Python indentation)
   - **Pylance** (usually comes with Python extension)

## Step 2: Set Up Python Environment

### Check Python Installation
```bash
# Open VS Code terminal (View -> Terminal or Ctrl+`)
python --version
# or
python3 --version
```

### Install Required Packages
```bash
# Install Jupyter
pip install jupyter notebook ipykernel

# Install data science essentials (you'll need these soon)
pip install pandas numpy matplotlib

# Install ipython for better interactive experience
pip install ipython
```

## Step 3: Open Your Project in VS Code

1. **Open Folder**: File → Open Folder
2. Navigate to where you want to create your project
3. Create a new folder called `python-learning-journey`
4. Select this folder

Or from terminal:
```bash
# Navigate to your preferred location
cd ~/Documents  # or wherever you want

# Create and open project
mkdir python-learning-journey
cd python-learning-journey
code .  # Opens VS Code in this folder
```

## Step 4: Working with Jupyter Notebooks in VS Code

### Open the Notebook
1. In VS Code, navigate to `notebooks/01_getting_started.ipynb`
2. Click to open it
3. VS Code will show a "Select Kernel" button at the top right
4. Click it and select your Python interpreter

### Running Cells
- **Run single cell**: Click the ▶️ icon next to the cell
- **Run all cells**: Click "Run All" at the top
- **Keyboard shortcut**: `Shift+Enter` runs current cell and moves to next

### Tips for Jupyter in VS Code
- Use `Ctrl+Enter` to run cell without moving to next
- Use `Alt+Enter` to run cell and insert new cell below
- Click the `{...}` icon to see variables in Variable Explorer
- Right-click cells for more options

## Step 5: GitHub Setup

### Option A: Using VS Code's Built-in Git

1. **Initialize Git Repository**
   - Open Source Control panel (Ctrl+Shift+G)
   - Click "Initialize Repository"

2. **Make Your First Commit**
   - Stage all files (click the + icon)
   - Add commit message: "Initial commit - Python learning project setup"
   - Click the ✓ checkmark to commit

3. **Connect to GitHub**
   - Click "Publish to GitHub" button
   - Choose public or private repository
   - Follow the prompts to authenticate with GitHub

### Option B: Using Terminal Commands

```bash
# Navigate to your project folder
cd python-learning-journey

# Initialize git
git init

# Configure git (replace with your info)
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Add all files
git add .

# Make first commit
git commit -m "Initial commit - Python learning project setup"

# Create repository on GitHub (do this in your browser first)
# Then connect it:
git remote add origin https://github.com/yourusername/python-learning-journey.git

# Push to GitHub
git branch -M main
git push -u origin main
```

### Regular Git Workflow

```bash
# After making changes:
git add .                              # Stage changes
git commit -m "Completed chapter 2"    # Commit with message
git push                               # Push to GitHub

# Check status anytime
git status

# View commit history
git log --oneline
```

## Step 6: Daily Workflow

### Morning Routine (15-20 mins)
1. Open VS Code
2. Open your project folder
3. Pull latest changes (if working across devices):
   ```bash
   git pull
   ```
4. Review yesterday's notes
5. Read 1-2 pages from the book

### Study Session (30-45 mins)
1. Open corresponding notebook
2. Follow along with the book
3. Type out all code examples (don't copy-paste!)
4. Try exercises
5. Add notes to the notebook

### End of Session (5 mins)
1. Save all files
2. Commit your work:
   ```bash
   git add .
   git commit -m "Day X: Completed [topic]"
   git push
   ```
3. Update your progress checklist in README.md

## Step 7: Useful VS Code Shortcuts

```
Ctrl+` (Cmd+`)         - Toggle terminal
Ctrl+Shift+P           - Command palette
Ctrl+/                 - Comment/uncomment line
Shift+Alt+F            - Format code
F5                     - Start debugging
Ctrl+Space             - Trigger autocomplete
Ctrl+Shift+[           - Fold code
Ctrl+Shift+]           - Unfold code
```

## Troubleshooting

### Jupyter Kernel Not Found
```bash
python -m ipykernel install --user
```

### Import Errors
```bash
# Make sure you're in the right environment
pip list  # Check installed packages
pip install package-name  # Install missing package
```

### Git Authentication Issues
- Use GitHub Desktop as alternative
- Set up SSH keys for easier authentication
- Use Personal Access Token instead of password

## Next Steps

1. ✅ Extensions installed
2. ✅ Python environment ready
3. ✅ Project structure created
4. ✅ First notebook opened
5. ✅ Git configured
6. ✅ Connected to GitHub
7. 🚀 **START LEARNING!**

Open `notebooks/01_getting_started.ipynb` and begin your Python journey!

---

**Remember**: The goal is to build consistency. Even 20 minutes daily is better than irregular 2-hour sessions!

# SmartPigCare Project Setup Guide (VS Code)

---

## Table of Contents

- [Prerequisites](#prerequisites)  
- [Clone and Setup GitHub Repository](#clone-and-setup-github-repository)  
- [Open Project in VS Code](#open-project-in-vs-code)  
- [Step 3: Create and Activate Python Virtual Environment](#step-3-create-and-activate-python-virtual-environment)  
- [Step 4: Install Project Dependencies](#step-4-install-project-dependencies)  
- [Step 5: Configure Python Interpreter in VS Code](#step-5-configure-python-interpreter-in-vs-code)  
- [Step 6: Run the Flask Backend](#step-6-run-the-flask-backend)  
- [Step 7: Deactivate Virtual Environment (Optional)](#step-7-deactivate-virtual-environment-optional)  
- [Basic Git & GitHub Version Control](#basic-git--github-version-control)

---

## Prerequisites

Install this python version for compatability with tensorflow: https://www.python.org/downloads/release/python-3110/
- **Python 3.8 or higher** installed  
  Download from [https://www.python.org/downloads/](https://www.python.org/downloads/)  
  > *Windows users:* Ensure **“Add Python to PATH”** is checked during installation.

- **VS Code** installed  
  Download from [https://code.visualstudio.com/](https://code.visualstudio.com/)

- **Git** installed  
  Download from [https://git-scm.com/downloads](https://git-scm.com/downloads)

---

## Clone and Setup GitHub Repository

### 1. Create a GitHub repository

- Go to [https://github.com/new](https://github.com/new)  
- Name the repo `SmartPigCare`  
- Choose **Public** or **Private**  
- Do **NOT** initialize with README or .gitignore (to simplify syncing)

### 2. Clone the repo locally using VS Code

- Open VS Code  
- Press `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (Mac) to open Command Palette  
- Type `Git: Clone` and select it  
- Paste your GitHub repo URL and press Enter  
- Choose a folder on your computer to clone into  
- VS Code will open the cloned repo automatically

### 3. Add your existing project files

- Copy your project files (backend, frontend, data folders, etc.) into the cloned folder.

### 4. Commit and push files

Open VS Code terminal and run:

```bash
git add .
git commit -m "Initial commit with project files"
git push origin main

## Open Project in VS Code

1. **Launch VS Code**

2. Click on the menu: `File` > `Open Folder...`

3. Navigate to and select the folder where you cloned the repository or placed your project files

---

## Step 3: Create and Activate Python Virtual Environment

1. **Open the integrated terminal in VS Code:**

   - **Windows/Linux:** Press `Ctrl + `` (backtick key, usually above Tab)`  
   - **Mac:** Press `Cmd + `` (backtick key)`  
   - Or click menu: `View` > `Terminal`

2. **Create the virtual environment (only once):**

   - **Mac/Linux:**

     ```bash
     python3 -m venv venv
     ```

   - **Windows:**

     ```bash
     python -m venv venv
     ```

3. **Activate the virtual environment:**

   - **Mac/Linux:**
     source venv/bin/activate

   - **Windows:**

     ```bash
     .\venv\Scripts\activate
     ```

4. **Verify activation:**  
   Your terminal prompt should now start with `(venv)`, indicating the virtual environment is active.

---

## Step 4: Install Project Dependencies

With the virtual environment activated, run:

```bash
pip install -r requirements.txt

## Step 5: Configure Python Interpreter in VS Code

1. Open VS Code.

2. Press `Ctrl + Shift + P` (Windows/Linux) or `Cmd + Shift + P` (Mac) to open the Command Palette.

3. Type **`Python: Select Interpreter`** and press Enter.

4. From the list, select the Python interpreter located inside your project’s virtual environment:

   - On Mac/Linux, it will be something like:  
     `/path/to/your/project/venv/bin/python`

   - On Windows, it will look like:  
     `C:\path\to\your\project\venv\Scripts\python.exe`

This tells VS Code to use your project’s isolated Python environment for running and debugging.

---

## Step 6: Run the Flask Backend

1. Make sure your virtual environment is activated in the terminal.

2. Run your Flask application by executing:

   ```bash
   python app.py

Open your web browser and navigate to:
http://localhost:5000


You should see the SmartPigCare dashboard load, indicating the backend and frontend are running successfully.

## Step 7: Deactivate the Virtual Environment (Optional)

When you finish working, you can deactivate the virtual environment by running:

```bash
deactivate

## Basic Git & GitHub Version Control

### Pull the Latest Changes Before Starting Work:

```bash
git pull origin main

### Stage Your Changes After Editing:

```bash
git add .

### Commit Your Changes with a Descriptive Message:

```bash
git commit -m "Describe your changes here"

### Push Your Changes to GitHub:

```bash
git push origin main

## Additional Tips

- Use the **Source Control** tab in VS Code for an easy graphical interface to manage Git operations.

- Create **feature branches** to isolate new work before merging into `main`.

- Commit frequently with clear, meaningful commit messages.

## Important: Selecting the Python Interpreter in VS Code

To ensure VS Code uses your virtual environment and installs/packages run correctly:

1. Open VS Code.

2. Press `Ctrl + Shift + P` (Windows/Linux) or `Cmd + Shift + P` (Mac) to open the Command Palette.

3. Type and select **`Python: Select Interpreter`**.

4. Choose the Python interpreter located inside your virtual environment folder, for example:

   - On Mac/Linux:  
     `/path/to/your/project/venv/bin/python`

   - On Windows:  
     `C:\path\to\your\project\venv\Scripts\python.exe`

Once selected, VS Code will run your Python files using this interpreter.

smartpigcare/                   # Root project folder
├── app.py                     # Main Flask backend application
├── requirements.txt           # Python dependencies list
├── .gitignore                 # Git ignore rules
├── README.md                  # Project documentation and setup instructions
├── data/                      # Folder for datasets and label files
│   └── combined_data.json     # Sample combined pig data in JSON format
├── notebooks/                 # Jupyter notebooks for experiments and model training
│   └── example_notebook.ipynb # Example notebook (optional)
├── scripts/                   # Python scripts for training and data processing
│   ├── train_feeding.py       # Script to train feeding detection model
│   └── train_bcs.py           # Script to train Body Condition Score model
├── static/                    # Static frontend files (JS, CSS, images)
│   ├── script.js              # Frontend JavaScript (dashboard interactivity)
│   └── style.css              # Stylesheet for dashboard styling (optional)
└── templates/                 # HTML templates for Flask to render
    └── index.html             # Main dashboard HTML page

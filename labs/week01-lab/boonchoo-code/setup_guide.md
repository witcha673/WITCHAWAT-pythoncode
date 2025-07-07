# Python Development Environment Setup Guide

## Overview
This guide will help you set up Python on your computer and prepare your development environment for programming.

## Step 1: Install Python

### For Windows:
1. Visit [python.org](https://www.python.org/downloads/)
2. Download the latest Python 3.x version
3. Run the installer
4. **IMPORTANT**: Check "Add Python to PATH" during installation
5. Click "Install Now"

### For macOS:
1. Visit [python.org](https://www.python.org/downloads/)
2. Download the latest Python 3.x version
3. Run the installer package
4. Follow the installation wizard

### For Linux (Ubuntu/Debian):
```bash
sudo apt update
sudo apt install python3 python3-pip
```

## Step 2: Verify Installation

Open your terminal/command prompt and run:
```bash
python --version
```
or
```bash
python3 --version
```

You should see something like "Python 3.x.x"

## Step 3: Choose a Text Editor or IDE

### Recommended Options:
1. **VS Code** (Recommended for beginners)
   - Download from [code.visualstudio.com](https://code.visualstudio.com/)
   - Install the Python extension

2. **PyCharm Community Edition**
   - Download from [jetbrains.com](https://www.jetbrains.com/pycharm/)
   - Free and feature-rich

3. **IDLE** (Comes with Python)
   - Simple and built-in
   - Good for learning

## Step 4: Test Your Setup

1. Open your chosen editor
2. Create a new file called `test.py`
3. Type: `print("Hello, Python!")`
4. Save the file
5. Run it using:
   ```bash
   python test.py
   ```

If you see "Hello, Python!" printed, you're ready to go!

## Step 5: Create Your Lab Workspace

1. Create a folder called `python-labs` on your desktop
2. Inside that folder, create a subfolder called `week01`
3. This is where you'll save your lab files

## Troubleshooting Common Issues

### Issue: "python is not recognized as a command"
**Solution**: Python is not in your PATH. Reinstall Python and make sure to check "Add Python to PATH"

### Issue: Multiple Python versions
**Solution**: Use `python3` instead of `python` in your commands

### Issue: Permission denied (Linux/Mac)
**Solution**: Use `python3` or add `sudo` before the command

## Next Steps
Once your environment is set up, proceed to the lab exercises to start programming!
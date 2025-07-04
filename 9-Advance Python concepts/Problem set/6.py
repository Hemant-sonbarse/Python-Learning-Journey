#6. Run pip freeze for the system interpreter. Take the contents and create a similar  virtualenv.



'''
 ### **Steps to Create a Virtual Environment from `pip freeze` Output on Windows**  

#### **Step 1: Run `pip freeze` for the System Interpreter**
Open **Command Prompt (cmd)** or **PowerShell** and run:
```cmd
pip freeze > requirements.txt
```
This saves the list of installed packages into a file named `requirements.txt`.

#### **Step 2: Create a Virtual Environment**
Now, create a new virtual environment using `venv`:
```cmd
python -m venv my_virtualenv
```
Replace `my_virtualenv` with your preferred name.

#### **Step 3: Activate the Virtual Environment**
Now, activate the virtual environment:

- **Command Prompt (cmd):**
  ```cmd
  my_virtualenv\Scripts\activate
  ```
- **PowerShell:**
  ```powershell
  my_virtualenv\Scripts\Activate.ps1
  ```
  If you get an execution policy error in PowerShell, run:
  ```powershell
  Set-ExecutionPolicy Unrestricted -Scope Process
  ```

#### **Step 4: Install Packages from `requirements.txt`**
With the virtual environment activated, install the saved dependencies:
```cmd
pip install -r requirements.txt
```

#### **Step 5: Verify Installation**
To ensure the installation was successful, run:
```cmd
pip freeze
```
It should output the same packages as in `requirements.txt`.

---
Now, your virtual environment is set up with the same packages as the system interpreter! Let me know if you need further assistance. 🚀
'''
# run_project.py
import subprocess
import sys
import os

venv_name = "localVenv"
requirements_file = "libReqs.txt"
main_script_name = "stellarClient.py"  # Replace with the actual name of your main script

def create_and_install():
    """Creates venv and installs dependencies if not already done."""
    venv_path = os.path.join(os.getcwd(), venv_name)
    pip_target = os.path.join(venv_path, "Scripts" if sys.platform == "win32" else "bin", "pip")

    if not os.path.exists(venv_path):
        print(f"Creating virtual environment: {venv_name}")
        try:
            subprocess.check_call([sys.executable, "-m", "venv", venv_name])
            print(f"Virtual environment '{venv_name}' created successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error creating virtual environment: {e}")
            return False
    else:
        print(f"Virtual environment '{venv_name}' already exists.")

    # Update pip in the virtual environment
    if os.path.exists(pip_target):
        print("Updating pip...")
        try:
            subprocess.check_call([pip_target, "install", "--upgrade", "pip"])
            print("pip updated successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error updating pip: {e}")
            print("Continuing with dependency installation...")
    else:
        print("Warning: pip executable not found in the virtual environment.")

    if os.path.exists(requirements_file):
        print(f"Installing dependencies from '{requirements_file}'...")
        try:
            subprocess.check_call([pip_target, "install", "-r", requirements_file, "--upgrade"])
            print("Dependencies installed successfully.")
            return True
        except subprocess.CalledProcessError as e:
            print(f"Error installing dependencies: {e}")
            return False
    else:
        print(f"Warning: '{requirements_file}' not found. Skipping dependency installation.")
        return True

if __name__ == "__main__":
    if create_and_install():
        print("\nSetup complete!")
        if os.path.exists(main_script_name):
            print(f"\nTo run the application, first activate the virtual environment:")
            if sys.platform == "win32":
                print(f" .\\{venv_name}\\Scripts\\activate")
            else:
                print(f"  source {venv_name}/bin/activate")
            print(f"Then, run your main script:")
            print(f"  python {main_script_name}")
        else:
            print(f"\nMake sure your main application script is named '{main_script_name}' and is in the same directory.")
    else:
        print("\nSetup failed. Please check the error messages above.")
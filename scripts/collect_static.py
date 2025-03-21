import os
import subprocess
from pathlib import Path

def collect_static():
    # Get the project root directory
    project_root = Path(__file__).resolve().parent.parent
    
    # Run collectstatic
    subprocess.run(['python', 'manage.py', 'collectstatic', '--noinput'], cwd=project_root)
    
    # Run compress
    subprocess.run(['python', 'manage.py', 'compress', '--force'], cwd=project_root)
    
    print("Static files collected and compressed successfully!")

if __name__ == '__main__':
    collect_static() 
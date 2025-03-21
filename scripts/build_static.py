import os
import subprocess
from pathlib import Path

def build_static():
    # Get the project root directory
    project_root = Path(__file__).resolve().parent.parent
    
    # Clean staticfiles directory
    staticfiles_dir = project_root / 'staticfiles'
    if staticfiles_dir.exists():
        for item in staticfiles_dir.glob('*'):
            if item.is_file():
                item.unlink()
            elif item.is_dir():
                for subitem in item.glob('*'):
                    subitem.unlink()
                item.rmdir()
    
    # Build Tailwind CSS
    subprocess.run(['python', 'manage.py', 'tailwind', 'build'], cwd=project_root)
    
    # Collect static files
    subprocess.run(['python', 'manage.py', 'collectstatic', '--noinput', '--clear'], cwd=project_root)
    
    # Compress static files
    subprocess.run(['python', 'manage.py', 'compress', '--force'], cwd=project_root)
    
    print("Static files built and collected successfully!")

if __name__ == '__main__':
    build_static() 
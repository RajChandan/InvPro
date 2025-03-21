import os
import subprocess
from pathlib import Path

def deploy():
    # Get the project root directory
    project_root = Path(__file__).resolve().parent.parent
    
    # Set production environment
    os.environ['DJANGO_SETTINGS_MODULE'] = 'core.settings'
    os.environ['DEBUG'] = 'False'
    
    # Install dependencies
    subprocess.run(['pip', 'install', '-r', 'requirements.txt'], cwd=project_root)
    
    # Build and collect static files
    subprocess.run(['python', 'scripts/build_static.py'], cwd=project_root)
    
    # Run migrations
    subprocess.run(['python', 'manage.py', 'migrate'], cwd=project_root)
    
    # Create superuser if needed
    subprocess.run(['python', 'manage.py', 'createsuperuser'], cwd=project_root)
    
    print("Deployment completed successfully!")

if __name__ == '__main__':
    deploy() 
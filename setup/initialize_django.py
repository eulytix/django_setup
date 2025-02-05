# Without this, you won't be able to import django modules
def initialize_django():

    import sys, os, django
    from django.conf import settings
    
    def find_base_directory(starting_path='.'):
        """
        Find the base directory of the project by searching for a .gitignore file.
        
        Parameters:
        starting_path (str): The directory path to start searching from.
        
        Returns:
        str: The path to the base directory if found, otherwise None.
        """
        current_path = os.path.abspath(starting_path)
        
        while current_path != os.path.dirname(current_path):  # while not at the root directory
            if 'config' in os.listdir(current_path):
                return current_path
            current_path = os.path.dirname(current_path)
        
        return None

    # Find the project base directory
    BASE_DIR= find_base_directory()

    # Add the project base directory to the sys.path
    # This means the script will look in the base directory for any module imports
    # Therefore you'll be able to import analysis.models etc
    sys.path.insert(0, BASE_DIR)

    # The DJANGO_SETTINGS_MODULE has to be set to allow us to access django importsŰ
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

    #  Allow queryset filtering asynchronously when running in a Jupyter notebook
    os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"

    # This is for setting up django
    from django.conf import settings

    if settings.configured:
        pass
    else:
        django.setup()

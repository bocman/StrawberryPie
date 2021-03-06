
#/venv/bin/python
import os
import sys

if __name__ == "__main__":

    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "/var/www/StrawberryPie/")))
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "/var/www/StrawberryPie/project/")))

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

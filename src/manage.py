#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mybook.settings")
    #os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mybook.settings_production")
    #print "pp="+os.environ.get("DJANGO_SETTINGS_MODULE", "fail DJANGO_SETTINGS_MODULE")
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

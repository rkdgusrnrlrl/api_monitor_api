from django.core.management.base import BaseCommand
import os
from pathlib import Path
import glob

class Command(BaseCommand):
    help = 'Clean migrate files and DB file'

    def clear_migrate_db_file(self, base_dir, db_file_name='db.sqlite3'):
        some = glob.glob('**/migrations/*.py')
        filted_file_paths = list(filter(lambda file_name: not ("__init__.py" in file_name), some))

        abs_db_path = os.path.join(base_dir, db_file_name)
        if os.path.exists(abs_db_path):
            os.remove(abs_db_path)
            self.success(f'remove data file({abs_db_path})')

        for file_path in filted_file_paths:
            abs_path = os.path.join(base_dir, file_path)
            os.remove(abs_path)
            self.success(f'remove file({abs_path})')


    def success(self, str):
        self.stdout.write(self.style.SUCCESS(str))

    def handle(self, *args, **options):
        BASE_DIR = Path(os.path.dirname(os.path.abspath(__file__)))\
            .parent.parent.parent
        self.clear_migrate_db_file(base_dir=BASE_DIR)
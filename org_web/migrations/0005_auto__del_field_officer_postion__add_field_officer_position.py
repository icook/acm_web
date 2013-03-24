# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Officer.postion'
        db.rename_column('org_web_officer', 'postion', 'position')


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Officer.postion'
        raise RuntimeError("Cannot reverse this migration. 'Officer.postion' and its values cannot be restored.")
        # Deleting field 'Officer.position'
        db.delete_column('org_web_officer', 'position')

    complete_apps = ['org_web']

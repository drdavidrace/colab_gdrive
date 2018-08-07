import os, sys, re
import pydrive

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from google.colab import auth
from oauth2client.client import GoogleCredentials

class ColabGDrive:
  #
  def __init__(self, current_dir = 'root'):
    print("Entering Initialization")
    auth.authenticate_user()
    gauth = GoogleAuth()
    gauth.credentials = GoogleCredentials.get_application_default()
    self.myGdrive = GoogleDrive(gauth)

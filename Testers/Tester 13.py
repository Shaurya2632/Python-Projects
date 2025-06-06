import ctypes, sys, subprocess

def batchRunner(*files):
  
    for file in files:
      
      try:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin()
        
      except:
        is_admin = False
      
      if not is_admin: 
    
           ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, f'"{__file__}" "{file}"', None, 1)
           sys.exit()
           
      else:
           subprocess.run(f'"{file}"', shell=True)    

batchRunner(r"E:/batch file/fix.bat")
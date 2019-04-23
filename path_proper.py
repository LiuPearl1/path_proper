FILE='/location/to/your/txt/xxx.txt'
OLD_TXT='old_txt'
NEW_TXT='new_txt'
with open (FILE,'r+') as f:
 t=f.read()
 t=t.replace(OLD_TXT,NEW_TXT)
 f.seek(0,0)
 f.write(t)
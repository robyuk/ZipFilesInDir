from pathlib import Path
import zipfile

rootdir=Path('files')
archivepath=rootdir / Path('archive.zip')

# This section archives the files
with zipfile.ZipFile(archivepath, 'w') as zf:
  for path in rootdir.rglob('*.txt'):
    zf.write(path)
    path.unlink()

# This section restores
for path in rootdir.glob("*.zip"):
  with zipfile.ZipFile(path, 'r') as zf:
    zf.extractall()
  

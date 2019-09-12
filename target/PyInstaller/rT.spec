# -*- mode: python -*-

block_cipher = None


a = Analysis(['/home/r4nd0wn/bin/rT/src/main/python/main.py'],
             pathex=['/home/r4nd0wn/bin/rT/target/PyInstaller'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=['/usr/lib/python3.7/site-packages/fbs/freeze/hooks'],
             runtime_hooks=['/tmp/tmpvo5w2t2u/fbs_pyinstaller_hook.py'],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='rT',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=False,
               name='rT')

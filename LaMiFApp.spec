# -*- mode: python -*-

from kivy.deps import sdl2, glew

block_cipher = None


a = Analysis(['LaMiFApp.py'],
             pathex=['C:\\Users\\Sylgi\\Google Drive\\Python\\La Mifa Git\\La-MIFA'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
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
          name='LaMiFApp',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               Tree('C:\\Users\\Sylgi\\Google Drive\\Python\\La Mifa Git\\La-MIFA'),
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
               upx=True,
               name='LaMiFApp')

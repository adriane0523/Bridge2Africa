# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['song_dl.py'],
             pathex=['C:\\Users\\Adriane Inocencio\\Desktop\\git\\Bridge2Africa\\Python_software\\src'],
             binaries=[],
             datas=[],
             hiddenimports=['pyttsx3.drivers'],
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
          name='song_dl',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='song_dl')

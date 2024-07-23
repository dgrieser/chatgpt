# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['ai-cli'],
    pathex=['/usr/local/lib/python3.12/dist-packages'],
    binaries=[('/usr/local/lib/python3.12/dist-packages/_cffi_backend.cpython-312-x86_64-linux-gnu.so', '.')]
    datas=[],
    hiddenimports=['_cffi_backend'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='ai-cli',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

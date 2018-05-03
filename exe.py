from cx_Freeze import setup,Executable


setup(name='Difference',
      version = '0.1',
      description = 'Find difference of text files',
      executables = [Executable('main.py')],
      platform = 'win32')

import cx_Freeze
include_files=None
base=None
if sys.platform == "win64":
    base ='win64GUI'

shortcut_table = [
("DesktopShortcut",
  "DesktopFolder",
  "My Calculator",
  "TRAGETDIR",
  "[TRAGETDIR]\smartcalculator.exe",
  None,
  None,
  None,
  None,
  None,
  None,
  "TARGETDIR"

)
]
msi_data ={"shortcut":shortcut_table}

boist_msi_options ={'data':msi_data}
setup(
  version="0.1",
  description="My Calculator",
  author="Raj Ghadi",
  name="My Calculator",
  options={'build_exe':{'include_files':None},"bdist_msi": bdist_msi_options,},
  executables=[
    Executable(
      script="my_calculator.py",
      base=base,

    )
  ]
  

)



    

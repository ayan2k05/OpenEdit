from cx_Freeze import setup, Executable

app_name = "OpenEdit"
app_version = "v1.1"
app_description = r"OpenEdit - Light Editor"
#in the below line add the path where finalicon.ico is saved
icon_path = r"C:\Users\YRepoPath\OpenEdit\icon.ico"
executables = [Executable("OpenEdit.py", base="Win32GUI", icon = icon_path)]


setup(
    name=app_name,
    version=app_version,
    description=app_description,
    executables=executables,
    options={"build_exe": {"packages": ["tkinter", "os"]}}
)


from cx_Freeze import setup, Executable

app_name = "OpenEdit"
app_version = "1.0"
app_description = r"OpenEdit - Light Editor"
icon_path = r"C:\Users\Anis Pathan\Desktop\OpenEdit\finalicon.ico"
executables = [Executable("OpenEdit.py", base="Win32GUI", icon = icon_path)]


setup(
    name=app_name,
    version=app_version,
    description=app_description,
    executables=executables,
    options={"build_exe": {"packages": ["tkinter", "subprocess"]}}
)


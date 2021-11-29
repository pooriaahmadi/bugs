# Cx_freeze for windows
import cx_Freeze

executables = [cx_Freeze.Executable("main.py")]

build_options = {
    "packages": ["pygame"],
    "include_files": ["fonts/", "artworks/"]
}

cx_Freeze.setup(
    name="Bugs",
    options={"build_exe": build_options},
    executables=executables
)

import subprocess
import sys

windows = False

compiler = "x86_64-w64-mingw32-g++ " if windows else "clang++ "
flags = "-std=c++20 "
name = "-o app.exe " if windows else "-o app "

files = [
    "src/main.cpp "
]

includes = [
    "./deps/raylib/include "
]

libs_macos = [
    "./deps/raylib/lib/macos -lraylib -framework Cocoa -framework OpenGL -framework IOKit -framework CoreVideo "
]

libs_windows = [
    "./deps/raylib/lib/windows -lraylib -lkernel32 -luser32 -lgdi32 -lm -lpthread -lwinmm "
]

cmd = compiler + flags + name

for file in files:
    cmd += f"{file}"

for include in includes:
    cmd += f"-I{include}"

if windows:
    for lib in libs_windows:
        cmd += f"-L{lib}"
else:
    for lib in libs_macos:
        cmd += f"-L{lib}"

subprocess.run(cmd, shell=True)

exe = "./app.exe" if windows else "./app"
subprocess.run(exe, shell=True)
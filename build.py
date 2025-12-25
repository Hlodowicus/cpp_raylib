import subprocess
import sys
import os

windows = False

compiler = "x86_64-w64-mingw32-g++ " if windows else "clang++ "
flags = "-std=c++20 "
name = "-o app.exe " if windows else "-o app "

if not os.path.exists("./deps/sqlite3/windows/sqlite3.o") and windows:
    print("AAAAAAAAAAAAAAA")
    sqlite_compilation = "x86_64-w64-mingw32-gcc -c ./deps/sqlite3/sqlite3.c -o ./deps/sqlite3/windows/sqlite3.o "
elif not os.path.exists("./deps/sqlite3/macos/sqlite3.o") and not windows:
    print("BBBBBBBBBBBBBBB")
    sqlite_compilation = "clang -c ./deps/sqlite3/sqlite3.c -o ./deps/sqlite3/macos/sqlite3.o "
else:
    sqlite_compilation = 'python -C "print("sqlite already compiled.")"'

subprocess.run(sqlite_compilation, shell=True)

files = [
    "src/main.cpp ",
    "./deps/sqlite3/windows/sqlite3.o " if windows else "./deps/sqlite3/macos/sqlite3.o "
]

includes = [
    "./deps/raylib/include ",
    "./deps/fmt "
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
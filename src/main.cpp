#define FMT_HEADER_ONLY
#include "./../deps/fmt/core.h"
#include "./../deps/sqlite3/sqlite3.h"
#include "raylib.h"
#include <string>

#include "./h/player.hpp"

int main(void) {
    InitWindow(0, 0, "oe");
    SetTargetFPS(60);
    ToggleFullscreen();
    DisableCursor();

    while (!WindowShouldClose()) {
        //UPDATE

        //DRAW
        BeginDrawing();
        ClearBackground(BROWN);
        EndDrawing();
    }

    CloseWindow();

    return 0;
}

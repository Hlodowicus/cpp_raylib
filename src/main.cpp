#include "raylib.h"

int main(void) {
    InitWindow(0, 0, "cpp_template_raylib");
    SetTargetFPS(60);
    ToggleFullscreen();

    while (!WindowShouldClose()) {
        //UPDATE

        //DRAW
        BeginDrawing();
        ClearBackground(BLACK);
        EndDrawing();
    }

    CloseWindow();

    return 0;
}
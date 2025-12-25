#pragma once

#include "raylib.h"

class Player {
    private:
    Camera3D cam;
    Vector3 movement, rotation;
    float zoom, speed, sensitivity;

    public:
    Player() {
        cam = {
            .position = Vector3{0.0f, 3.0f, 1.0f},
            .target = Vector3{0.0f, 2.0f, 0.0f},
            .up = Vector3{0.0f, 1.0f, 0.0f},
            .fovy = 60.0f,
            .projection = CAMERA_PERSPECTIVE
        };
        movement = Vector3{0.0f, 0.0f, 0.0f};
        rotation = Vector3{0.0f, 0.0f, 0.0f};
        zoom = 0.0f;

        speed = 10.0f;
        sensitivity = 0.3f;
    }

    void Update() {
        Move();
        UpdateCameraPro(&cam, movement, rotation, zoom);
    }

    void Move() {
        float delta = GetFrameTime();

        if(IsKeyDown(KEY_W)) {
            movement.x = 1 * speed * delta;
        } else if (IsKeyDown(KEY_S)) {
            movement.x = -1 * speed * delta;
        } else {
            movement.x = 0;
        }

        if(IsKeyDown(KEY_D)) {
            movement.y = 1 * speed * delta;
        } else if (IsKeyDown(KEY_A)) {
            movement.y = -1 * speed * delta;
        } else {
            movement.y = 0;
        }

        rotation.x = GetMouseDelta().x * sensitivity;
        rotation.y = GetMouseDelta().y * sensitivity;
    }

    const Camera3D& GetCamera() const { return cam; }
    const Vector3& GetRotation() const { return rotation; }

};
# Project3

# Alien Invasion Game

This Python script utilizes the Turtle module to create a simple game called "Alien Invasion." In this game, the player controls a spaceship represented by a triangle shape and attempts to shoot down alien targets that look like spaceships moving downward on the screen. The game is over when an alien collides with the player's spaceship.

## Setup and Dependencies

- **Python Libraries Used:** `turtle`, `random`, `math`
- **Platform:** This code is designed to run on any system with Python and its standard libraries installed.

## How to Run the Game

1. **Run the Python Script:** Execute the Python script in an environment with Python installed.
2. **Game Controls:**
   - Use the `Left` and `Right` arrow keys to move the player's spaceship horizontally.
   - Press the `Space` key to fire bullets from the spaceship to destroy the aliens.
3. **Objective:** Avoid collisions with the aliens while shooting them down with bullets.

## Code Structure

- **Screen Setup:** Initializes the game window and background with stars in the background.
- **Player Setup:** Sets up the player's spaceship, its movement speed, and the ability to shoot bullets.
- **Alien Setup:** Creates alien targets that move downward on the screen.
- **Functions:**
  - `move_left()` and `move_right()`: Functions to move the player's spaceship left and right.
  - `fire_bullet()`: Fires bullets from the player's spaceship.
  - `is_collision(t1, t2)`: Checks for collisions between game entities.
- **Game Loop:** Manages the game's logic, updates the screen, moves aliens, handles bullet firing, and detects collisions.
- **End Game:** Displays "Game Over" text on the screen if the player collides with an alien.

## How to Exit the Game

- **End Game:** The game ends when the player's spaceship collides with an alien. The script displays "Game Over!" on the screen.
- **Manually Exiting:** To close the game window, simply close the Turtle window or window manager.

Good Luck! 

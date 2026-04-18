<div align="center">

# 🎮 Space Shooter Game 🎮

### Classic Arcade-Style Action Game

**Version:** 1.0 | **Language:** Python | **Framework:** Pygame | **Resolution:** 800×600

<img src="https://img.shields.io/badge/Status-Active%20Development-brightgreen?style=flat-square" alt="Status"/>
<img src="https://img.shields.io/badge/License-MIT-blue?style=flat-square" alt="License"/>
<img src="https://img.shields.io/badge/Python-3.x-yellow?style=flat-square" alt="Python"/>

</div>

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Game Mechanics](#game-mechanics)
- [Controls](#controls)
- [Technical Specifications](#technical-specifications)
- [Game States](#game-states)
- [Installation & Requirements](#installation--requirements)
- [Assets Required](#assets-required)

---

<a id="overview"></a>

## 🎮 Overview

**Space Shooter** is a classic arcade-style action game where players control a player spaceship at the bottom of the screen and must defend against waves of incoming alien enemies. Shoot down enemies to accumulate points while avoiding them reaching the bottom of the screen.

### Game Objective
- **Primary Goal:** Survive as long as possible and achieve the highest score
- **Win Condition:** No single win condition; continuous gameplay focused on survival
- **Lose Condition:** When any enemy reaches the bottom of the screen (y > 480)

---

<a id="features"></a>

## ✨ Features

### Core Gameplay Features
- **Dynamic Enemy Movement:** 6 enemies with horizontal and vertical movement patterns
- **Bullet Mechanics:** Fire bullets upward to destroy enemies
- **Collision Detection:** Precise distance-based collision system using mathematical algorithms
- **Score Tracking:** Real-time score display during gameplay
- **Game Over State:** Graceful game over screen with final score
- **Restart Functionality:** Option to restart or quit after game over

### Visual Features
- **Background Image:** Custom background for immersive gaming experience
- **Sprite-Based Graphics:** Player, enemy, and bullet sprites
- **Game Window Icon:** Custom window icon for branding
- **Score Display:** On-screen score counter in the top-left corner (10, 10)
- **Game Over Screen:** Large centered text with instructions for restart/quit

### Audio/Visual Feedback
- Console score output on each successful hit
- Real-time score updates
- Game over message display

<a id="game-mechanics"></a>

---

## 🎯 Game Mechanics

### Player Mechanics
- **Sprite Size:** 64x64 pixels
- **Starting Position:** X=368 (centered), Y=480 (bottom of screen)
- **Movement Speed:** 5 pixels per frame (left/right)
- **Movement Range:** X axis bounded between 0-736 pixels (prevents off-screen movement)
- **Movement Type:** Horizontal only (left/right)

### Enemy Mechanics
- **Number of Enemies:** 6 simultaneous enemies
- **Sprite Size:** 64x64 pixels
- **Starting Position:** Random X (0-736), Random Y (50-150)
- **Horizontal Speed:** ±4 pixels per frame
- **Vertical Drop:** 40 pixels when reaching left/right boundaries
- **Behavior Pattern:**
  - Move horizontally across screen
  - Upon hitting left (x ≤ 0) or right (x ≥ 736) boundary, reverse direction and drop 40 pixels
  - If y-position exceeds 480, triggers game over
  - Reset to random position upon destruction

### Bullet Mechanics
- **Sprite Size:** Derived from bullet.png asset
- **Initial Position:** Fired from player's current X position + 16 offset
- **Movement Speed:** 10 pixels per frame (upward)
- **Bullet States:** 
  - `"ready"` - Ready to fire, waiting for spacebar press
  - `"fire"` - Currently traveling upward
- **Boundary Behavior:** Reset to Y=480 when reaching top of screen (y ≤ 0)
- **Fire Rate:** One bullet at a time (must wait for previous bullet to clear)

### Collision System
- **Collision Formula:** Distance-based using Euclidean distance
- **Detection Radius:** < 27 pixels distance
- **Calculation:** `distance = √((enemyX - bulletX)² + (enemyY - bulletY)²)`
- **On Collision:**
  - Bullet resets to Y=480 and state set to "ready"
  - Enemy score increases by 1
  - Enemy respawns at random position (0-736, 50-150)

<a id="controls"></a>

---

## 🎮 Controls

| Key | Action |
|-----|--------|
| **LEFT ARROW** | Move player left (-5 px/frame) |
| **RIGHT ARROW** | Move player right (+5 px/frame) |
| **SPACEBAR** | Fire bullet (only when state="ready") |
| **R** | Restart game (on game over screen) |
| **Q** | Quit game (on game over screen) |
| **CLOSE WINDOW** | Exit game immediately |

<a id="technical-specifications"></a>

---

## 📊 Technical Specifications

### Screen & Display
- **Resolution:** 800 x 600 pixels
- **FPS:** Depends on Pygame frame rate (typically 60 FPS)
- **Color Scheme:** Black background (#000000) with white text (#FFFFFF)

### Boundaries
| Boundary | Value | Notes |
|----------|-------|-------|
| Left Edge | x = 0 | Player/Enemy leftmost position |
| Right Edge | x = 736 | Player/Enemy rightmost position (800 - 64) |
| Top Edge | y = 0 | Bullet disappears above |
| Bottom Edge | y = 600 | Game over if enemy reaches y > 480 |
| Player Y-Axis | y = 480 | Fixed at bottom of screen |

### Memory & Variables
- **Score Variable:** Global integer counter starting at 0
- **Game Over Flag:** Boolean state variable
- **Player Position:** playerX (dynamic), playerY=480 (static)
- **Bullet State:** String-based state machine ("ready"/"fire")
- **Enemy Arrays:** Lists containing position and velocity data for 6 enemies

### Fonts
- **Score Font:** Default, Size 36
<a id="game-states"></a>

- **Game Over Font:** Default, Size 72

---

## 🔄 Game States

### 1. **Playing State**
- Active gameplay
- Player can move left/right
- Player can fire bullets
- Enemies move and descend
- Score updates on collision
- Game over triggered if enemy reaches bottom

### 2. **Game Over State**
- Game loop pauses
- Display game over screen with:
  - "GAME OVER" text (red, center-top)
  - Final score display (center-middle)
  - Instructions: "Press R to Restart or Q to Quit" (center-bottom)
- Waiting state for player input (R/Q/Close Window)

### 3. **Restart State**
- Score reset to 0
- Player position reset to X=368, Y=480
- Bullet reset to Y=480 with state="ready"
- All enemies respawn at random positions (0-736, 50-150)
- Return to playing state

---

## 🎯 Scoring System

| Event | Points |
|-------|--------|
| Enemy Destroyed | +1 |
<a id="installation--requirements"></a>

| Game Over | Game ends, final score displayed |

---

## 📦 Installation & Requirements

### Prerequisites
```
Python 3.x
Pygame library
```

### Installation Steps
1. Install Python from python.org
2. Install Pygame:
   ```bash
   pip install pygame
   ```
3. Place all game assets in the game directory
4. Run the game:
<a id="assets-required"></a>

   ```bash
   python SpaceShoter.py
   ```

---

## 🖼️ Assets Required

Place the following image files in the game directory:

| Asset Name | Dimensions | Purpose |
|------------|-----------|---------|
| `icon.png` | Any | Window title bar icon |
| `background.png` | 800x600 | Game background image |
| `player.png` | 64x64 | Player spaceship sprite |
| `alien.png` | 64x64 | Enemy alien sprite (used 6 times) |
| `bullet.png` | Variable | Bullet projectile sprite |

---

## 🔧 Code Structure

### Main Components
1. **Initialization:** Pygame setup, asset loading, variable initialization
2. **Game Objects:** Player, Enemies (6x), Bullet
3. **Functions:** 
   - `player(x, y)` - Render player sprite
   - `enemy(x, y, i)` - Render enemy sprite
   - `fire_bullet(x, y)` - Render and manage bullet
   - `isCollision(enemyX, enemyY, bulletX, bulletY)` - Collision detection
4. **Main Game Loop:** Event handling, update positions, render objects, check states
5. **Game Over Loop:** Display screen, handle restart/quit input

---

## 🎓 Learning Outcomes

This project demonstrates:
- Basic game loop architecture
- Sprite rendering and animation
- Collision detection algorithms
- Event-driven programming
- State management
- Array/list manipulation for multiple game objects
- Boundary checking and constraints

---

**Last Updated:** April 2026  
**Author:** Game Development Team  
**Status:** Active Development

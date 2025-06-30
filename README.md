# Pac-Man & Pepper Game

**Pac-Man & Pepper** is a fast-paced two-player cooperative twist on the classic Pac-Man maze game, built using Python and Pygame. Play together, collect points, avoid hazards, and survive with shared health bars in a colorful, interactive maze.

---

## Gameplay Overview

- **Co-op Challenge**: Two players (Pac-Man and Pepper) navigate the same maze independently.  
- **Shared Lives**: One health bar for both players – if one gets hurt, both lose life.  
- **Goal**: Be the first to reach 1000 points to win. Beat the high score of 1300 for ultimate bragging rights!

---

## Hazards & Powerups

- **Yellow Dots**: +10 points  
- **Red Enemies**: -20 points, -1.5 life (they move dynamically)  
- **Purple Food**: -10 points, -2.5 life  
- **Orange Dots**: +50 points, +2 life  

---

## Strategy Tips

- Prioritize orange dots to restore health.  
- Avoid red and purple tiles — they are hazardous.  
- Work as a team: splitting up covers more ground, but increases danger.  
- Move quickly — red enemies shift positions every frame.

---

## Controls

| Player   | Keys        |
|----------|-------------|
| Pac-Man  | Arrow Keys  |
| Pepper   | W A S D     |

---

## Screenshot

![Screenshot](https://github.com/user-attachments/assets/af3f5603-b71f-473d-afaa-e14ca8bd16c8)

---

## Requirements

- Python 3.x  
- Pygame  
- Tkinter (standard in most Python distributions)  

---

## How to Run

1. Install dependencies:

   ```bash
   pip install pygame
Save the script as pacman_pepper.py.

Run the game:

bash
Copy code
python pacman_pepper.py
Follow the on-screen prompts and start playing!

## Features
Two-player local gameplay

Dynamic enemy tile movement

Scoring system with individual scores and shared life bars

Retro-styled maze design

Introductory instructions and tips via Tkinter popups

Win and Game Over conditions with message alerts

## Notes
The game ends if both players' life bars reach zero.

Game also ends if either player reaches 1000 points and beats the record of 1300.

All movement and interactions are tile-based.

## Author
Built by Kingsley C. Ndukauba
Feel free to fork, modify, and share!

## License
This project is open source and available under the MIT License.

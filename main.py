import pygame
import sys
import tkinter as tk
from tkinter import messagebox
import random

pygame.init()

TILE_SIZE = 20
FPS = 8

WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)
BLACK = (0, 0, 0)
PEACH = (255, 218, 185)

MAZE = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,2,2,2,1,2,4,2,2,3,2,2,2,2,2,1,2,2,5,1,2,3,2,2,4,5,2,2,2,1],
    [1,2,1,2,1,1,1,2,1,1,1,1,2,1,1,1,2,1,2,1,2,1,1,1,1,1,2,1,2,1],
    [1,2,1,2,2,2,1,2,2,2,0,1,2,2,2,1,2,1,2,1,3,1,2,2,2,1,2,1,2,1],
    [1,2,1,1,1,2,1,1,1,1,2,1,1,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1],
    [1,2,2,3,1,2,2,0,0,1,2,1,2,0,2,0,2,2,2,0,2,0,0,1,2,5,2,4,2,1],
    [1,1,1,2,1,1,1,1,0,1,2,1,0,1,1,1,1,0,1,1,1,1,0,1,1,5,1,1,1,1],
    [1,2,4,2,0,2,2,1,2,2,0,2,0,1,2,2,0,0,2,2,2,0,0,1,2,0,3,2,1,1],
    [1,2,1,1,5,1,0,1,1,1,3,1,1,1,2,1,2,1,2,1,1,1,0,1,2,1,1,2,1,1],
    [1,2,1,2,2,1,0,0,2,4,0,4,2,2,2,1,0,1,2,1,5,2,0,1,2,1,0,0,2,1],
    [1,2,1,1,0,1,1,1,1,1,1,1,1,1,1,1,0,1,2,1,1,1,1,1,2,1,1,1,2,1],
    [1,2,2,0,0,2,2,2,5,0,0,0,5,2,2,2,2,2,2,2,0,5,2,2,2,0,0,2,2,1],
    [1,1,1,0,1,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,2,1,1,1,1,0,1,1,1,1],
    [1,2,0,2,1,2,2,1,0,0,2,2,0,1,2,0,0,0,2,1,2,0,2,5,0,0,0,0,2,1],
    [1,2,1,5,1,0,1,1,1,1,1,1,1,1,0,1,0,1,2,1,0,1,1,1,1,1,0,1,2,1],
    [1,2,1,2,0,2,0,2,0,2,2,2,2,0,0,1,0,1,2,1,2,0,2,2,2,5,0,1,2,1],
    [1,2,1,1,1,1,1,1,0,1,2,1,2,1,1,1,0,1,2,1,1,1,1,1,1,1,0,1,2,1],
    [1,2,2,2,2,2,2,1,0,1,2,1,0,1,2,2,0,2,2,2,2,2,2,1,2,2,0,2,2,1],
    [1,2,1,1,1,1,2,1,1,1,2,1,1,1,2,1,1,1,2,1,1,1,2,1,1,1,1,1,2,1],
    [1,2,3,4,5,2,2,2,2,2,2,2,2,2,5,0,2,2,2,0,0,2,2,3,5,2,0,4,2,1],
    [1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1],
    [1,2,2,2,2,2,3,2,2,2,2,2,3,2,2,2,2,2,4,2,2,2,2,2,3,2,2,2,2,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]

ROWS = len(MAZE)
COLS = len(MAZE[0])
WIDTH = COLS * TILE_SIZE
HEIGHT = ROWS * TILE_SIZE

pacman_x, pacman_y = 1, 1
pepper_x, pepper_y = 1, 2
pacman_score, pepper_score = 0, 0
record = 1150

pacman_life = 10
pepper_life = 10

pacman_mouth_open = True
pepper_mouth_open = True

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pac-Man & Pepper")
clock = pygame.time.Clock()

def game():
    messagebox.showinfo("Welcome", "Welcome to Pac-Man & Pepper!\n\n🎮 Controls:\nPac-Man: Arrow Keys\nPepper: W A S D\n\n🎯 Goal: Reach 1000 points to win.\n🏆 Record to beat: 1300 points.")
    messagebox.showinfo("Health & Teamwork", "❤️ Shared Health Bars:\nBoth players lose/gain life together.\n\n🏃 You can both move independently,\nbut teamwork keeps you alive!")
    messagebox.showinfo("Scoring & Hazards", "🔸 Yellow Dots = 10 pts\n🔺 Red Enemies = -20 pts & -1.5 life (move fast)\n🟣 Purple Food = -10 pts & -2.5 life\n🟠 Orange Dots = +50 pts & +2 life")
    messagebox.showinfo("Tips", "💡 Avoid red and purple tiles!\n💡 Prioritize orange dots for health.\n💡 Cooperate and split up smartly.\n💡 If both health bars hit zero... it's game over!")

def draw_maze():
    for y in range(ROWS):
        for x in range(COLS):
            tile = MAZE[y][x]
            rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            if tile == 1:
                pygame.draw.rect(screen, BLUE, rect)
            elif tile == 2:
                pygame.draw.circle(screen, YELLOW, rect.center, 3)
            elif tile == 3:
                pygame.draw.rect(screen, RED, rect)
            elif tile == 4:
                pygame.draw.rect(screen, PURPLE, rect)
            elif tile == 5:
                pygame.draw.circle(screen, ORANGE, rect.center, 6)

def move_player(x, y, dx, dy, score):
    global pacman_life, pepper_life
    new_x, new_y = x + dx, y + dy
    if 0 <= new_x < COLS and 0 <= new_y < ROWS and MAZE[new_y][new_x] != 1:
        tile = MAZE[new_y][new_x]
        if tile == 2:
            score += 10
            MAZE[new_y][new_x] = 0
        elif tile == 3:
            score -= 20
            pacman_life -= 1.5
            pepper_life -= 1.5
        elif tile == 4:
            score -= 10
            pacman_life -= 2.5
            pepper_life -= 2.5
            MAZE[new_y][new_x] = 0
        elif tile == 5:
            score += 50
            pacman_life += 2
            pepper_life += 2
            MAZE[new_y][new_x] = 0
        return new_x, new_y, score
    return x, y, score

def get_red_tiles():
    return [(x, y) for y in range(ROWS) for x in range(COLS) if MAZE[y][x] == 3]

def execute_red_tile_movement():
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for x, y in get_red_tiles():
        random.shuffle(directions)
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < COLS and 0 <= new_y < ROWS and MAZE[new_y][new_x] == 0:
                MAZE[y][x] = 0
                MAZE[new_y][new_x] = 3
                break

def main():
    game()
    global pacman_x, pacman_y, pacman_score
    global pepper_x, pepper_y, pepper_score
    global frame_count, pacman_mouth_open, pepper_mouth_open

    running = True

    while running:
        screen.fill(BLACK)
        draw_maze()
        execute_red_tile_movement()

        pacman_mouth_open = not pacman_mouth_open
        pepper_mouth_open = not pepper_mouth_open

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    pacman_x, pacman_y, pacman_score = move_player(pacman_x, pacman_y, -1, 0, pacman_score)
                elif event.key == pygame.K_RIGHT:
                    pacman_x, pacman_y, pacman_score = move_player(pacman_x, pacman_y, 1, 0, pacman_score)
                elif event.key == pygame.K_UP:
                    pacman_x, pacman_y, pacman_score = move_player(pacman_x, pacman_y, 0, -1, pacman_score)
                elif event.key == pygame.K_DOWN:
                    pacman_x, pacman_y, pacman_score = move_player(pacman_x, pacman_y, 0, 1, pacman_score)
                elif event.key == pygame.K_a:
                    pepper_x, pepper_y, pepper_score = move_player(pepper_x, pepper_y, -1, 0, pepper_score)
                elif event.key == pygame.K_d:
                    pepper_x, pepper_y, pepper_score = move_player(pepper_x, pepper_y, 1, 0, pepper_score)
                elif event.key == pygame.K_w:
                    pepper_x, pepper_y, pepper_score = move_player(pepper_x, pepper_y, 0, -1, pepper_score)
                elif event.key == pygame.K_s:
                    pepper_x, pepper_y, pepper_score = move_player(pepper_x, pepper_y, 0, 1, pepper_score)

        center_x = pacman_x * TILE_SIZE + TILE_SIZE // 2
        center_y = pacman_y * TILE_SIZE + TILE_SIZE // 2
        radius = TILE_SIZE // 2

        if pacman_mouth_open:
            pygame.draw.circle(screen, YELLOW, (center_x, center_y), radius)
        pygame.draw.polygon(screen, BLACK, [(center_x, center_y), (center_x + radius, center_y - radius // 2), (center_x + radius, center_y + radius // 2)])


        center_x2 = pepper_x * TILE_SIZE + TILE_SIZE // 2
        center_y2 = pepper_y * TILE_SIZE + TILE_SIZE // 2

        if pepper_mouth_open:
            pygame.draw.circle(screen, PEACH, (center_x2, center_y2), radius)
        pygame.draw.polygon(screen, BLACK, [(center_x2, center_y2), (center_x2 - radius, center_y2 - radius // 2), (center_x2 - radius, center_y2 + radius // 2)])


        pygame.display.set_caption(f"PAC-MAN SCORE: {pacman_score} LIFE: {pacman_life} | PEPPER SCORE: {pepper_score} LIFE: {pepper_life} | RECORD: {record}")
        pygame.display.flip()
        clock.tick(FPS)

        if pacman_score >= 1000 and pacman_score >= record:
            messagebox.showinfo("Victory", "PAC-MAN WON AND BEAT THE RECORD!")
            running = False
        elif pepper_score >= 1000 and pepper_score >= record:
            messagebox.showinfo("Victory", "PEPPER WON AND BEAT THE RECORD!")
            running = False

        if pacman_life <= 0 and pepper_life <= 0:
            messagebox.showinfo("Game Over", "PAC-MAN AND PEPPER HAVE DIED. GAME OVER")
            running = False

main()

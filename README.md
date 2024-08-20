Here's a README for your Rock Paper Scissors game using OpenCV, cvzone, and Mediapipe:

---

# Rock Paper Scissors Game

This is a Rock Paper Scissors game implemented using OpenCV, cvzone, and Mediapipe. The game uses hand gestures to play against an AI that randomly selects its moves. 

## Features

- Real-time hand gesture detection using a webcam.
- AI opponent that randomly selects Rock, Paper, or Scissors.
- Visual countdown timer to synchronize player and AI moves.
- Score tracking for both the player and the AI.
- Simple and intuitive interface with real-time feedback.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ai-rupak/rock-paper-scissors-game.git
   cd rock-paper-scissors-game
   ```

2. **Install the required dependencies:**
   Make sure you have Python installed. You can install the required libraries using pip:
   ```bash
   pip install opencv-python cvzone mediapipe
   ```

3. **Download the Resources:**
   Ensure you have the `Resources` folder in the project directory containing:
   - `BG.png` (Background image)
   - `1.png`, `2.png`, `3.png` (Images for Rock, Paper, Scissors)

## How to Play

1. **Run the script:**
   ```bash
   python RPS.py
   ```

2. **Start the game:**
   - Press the `s` key to start the game. A countdown timer will begin.
   - Use hand gestures to play:
     - Closed fist for Rock
     - Open hand for Paper
     - Peace sign (two fingers up) for Scissors
   - The AI will make its move after the countdown, and the result will be displayed.

3. **End the game:**
   - Press the `a` key to end the game and close the window.

## Hand Gestures

- **Rock**: Closed fist `[0, 0, 0, 0, 0]`
- **Paper**: Open hand `[1, 1, 1, 1, 1]`
- **Scissors**: Peace sign `[0, 1, 1, 0, 0]`

## Screenshot

![Gameplay Screenshot](./Resources/screenshot.png)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This project uses the [cvzone](https://github.com/cvzone/cvzone) library by **CVZone**.
- Special thanks to the [Mediapipe](https://mediapipe.dev/) team for their hand detection solution.


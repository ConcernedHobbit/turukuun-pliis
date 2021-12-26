# Guide
Download the latest [release](https://github.com/ConcernedHobbit/turukuun-pliis/releases) source code .zip (under *Assets*)

---

*This part assumes you have [poetry](https://python-poetry.org/docs/) installed.*

Open your terminal in the root folder (`turukuun-pliis/`) and run

```bash
poetry install
```

to install the runtime requirements.

After poetry has finished installing the requirements, you can start the game with the command

```bash
poetry run invoke start
```

# Game
The game starts up to a splash screen. Press **SPACE** to start or **Q** to quit.

You can access the splash screen (pause menu) anytime by pressing **ESC**. You can close the menu by pressing **ESC** or **SPACE**, or quit the game by pressing **Q**.

## Objective
Your objective is to evaluate as many persons wanting to cross and to choose whether or not they will be allowed entry.

Make sure their documented details match up with what they're telling you!

Press **Y** to let them through or **N** to deny them entry.

You gain points for letting people in when they're not lying and denying them when they are.

But be careful! You lose points if you wrongfully deny someone entry or let a weasely liar in.

You can check how your points are affected in the pause menu at any time.
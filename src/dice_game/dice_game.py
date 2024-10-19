# dice_game.py

import random
import typer

# Create a Typer app
app = typer.Typer()

@app.command()
def roll_dice(dice: int = 1, sides: int = 6):
    """
    Roll a specified number of dice with a given number of sides.
    
    Args:
    - dice: The number of dice to roll (default is 1).
    - sides: The number of sides on each die (default is 6).
    """
    results = [random.randint(1, sides) for _ in range(dice)]
    total = sum(results)
    typer.echo(f"Rolled {dice} dice with {sides} sides: {results}")
    typer.echo(f"Total: {total}")

if __name__ == "__main__":
    app()

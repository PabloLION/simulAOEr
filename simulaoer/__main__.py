import typer


app = typer.Typer()


@app.command()
def defualt_repl():
    """
    SimulAOEr REPL
    """
    typer.echo("REPL started. try '10 champion vs 10 eagles'")
    user_input = typer.prompt(text=">>> ", prompt_suffix="")
    while user_input != "exit":
        if user_input == "10 champion vs 10 eagles":
            print("10 champion")
        else:
            print(f"you typed: {user_input}")
        user_input = typer.prompt(text=">>> ", prompt_suffix="")


if __name__ == "__main__":
    app()

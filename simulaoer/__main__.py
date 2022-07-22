import typer


app = typer.Typer()


@app.callback(invoke_without_command=True)
def without_command(ctx: typer.Context):
    if ctx.invoked_subcommand is None:
        ctx.invoke(repl)


@app.command("repl")
def repl():
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


@app.command("info")
def info():
    """
    Show info about simulAOEr
    """
    typer.echo("using AOE2DE version 63482")


if __name__ == "__main__":
    app()

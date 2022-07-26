import typer

app = typer.Typer()
state = {"verbose": False}


@app.command()
def create(username: str):
    if state["verbose"]:
        print("About to create a user")
    print(f"Creating user: {username}")
    if state["verbose"]:
        print("Just created a user")


@app.command()
def delete(username: str):
    if state["verbose"]:
        print("About to delete a user")
    print(f"Deleting user: {username}")
    if state["verbose"]:
        print("Just deleted a user")


@app.callback()
def main():
    """
    Manage users in the awesome CLI app.
    """
    print("something")


if __name__ == "__main__":
    print("running __main__")
    app()

import typer

def main():
   test_typer = input("Type '10 champion vs 10 eagles':")
   if test_typer == "10 champion vs 10 eagles":
       print("10 champion")


if __name__ == "__main__":
    typer.run(main)
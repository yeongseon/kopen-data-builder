# src/mycli/cli.py
import typer

app = typer.Typer()


@app.command()
def hello(name: str = "World") -> None:
    """Simple greeting CLI"""
    typer.echo(f"Hello, {name}")


app.command()(hello)

if __name__ == "__main__":
    app()

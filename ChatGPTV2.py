import openai
import config
import typer
from rich import print
from rich.table import Table


def main():
    openai.api_key = config.api_key

    print("[bold blue]Sammael API en Python[/bold blue]")

    table = Table("Comando", "Funcion")
    table.add_row("Salir", "Salir de la aplicacion")
    table.add_row("Nuevo", "Inicia una nueva conversacion")

    print(table)

    # contexto del asistente

    context = {"role": "system", "content": "Eres un programador en Python. "}
    messages = [context]

    while True:
        content = __prompt()

        if content == "Nuevo":
            print("Hola, que gusto que vuelvas!")
            messages = [context]
            content = __prompt()

        messages.append({"role": "user", "content": content})

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )

        response_content = response.choices[0].message.content

        messages.append({"role": "assistant", "content": response_content})

        print(f"[bold blue] > [/bold blue] [purple]{response_content}[/purple]")


def __prompt() -> str:
    prompt = typer.prompt("\nSobre que? Hablaremos hoy!!! ")

    if prompt == "Salir":
        Salir = typer.confirm("Deseas Cerrar?")
        if Salir:
            print("Gracias, Hasta pronto!!!")
            raise typer.Abort()
        return __prompt()

    return prompt


if __name__ == "__main__":
    typer.run(main)

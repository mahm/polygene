import asyncio
import random

import click
import json

from prettytable import PrettyTable
from tqdm.asyncio import tqdm as tqdm_async

from polygene.generator import Generator, condition_generator


async def generate_persona_async(target=None, condition=None, lang='ja', pbar=None):
    persona = await Generator(target=target, condition=condition, lang=lang).generate()
    if pbar:
        pbar.update(1)
    return persona


async def generate_personas_async(num, target=None, condition=None, lang='ja'):
    tasks = []
    with tqdm_async(total=num, desc="Generating personas", unit="persona") as pbar:
        conditions = condition_generator(condition)
        for _ in range(num):
            condition = random.choice(conditions)
            task = asyncio.ensure_future(
                generate_persona_async(target=target, condition=condition, lang=lang, pbar=pbar))
            tasks.append(task)
        personas = await asyncio.gather(*tasks)
    return personas


@click.group()
def cli():
    pass


@cli.command()
@click.argument('num', type=int)
@click.option('--target', type=str, help='The target for generating personas.')
@click.option('--condition', type=str, help='The condition for generating personas.')
@click.option('--lang', type=str, default='ja', help='The language for generating personas (default: ja)')
@click.option('--output', type=str, default='output.json',
              help='The name of the output JSON file (default: output.json)')
def generate(num, output, target, condition, lang):
    """Generate personas and save them to a file."""
    personas = asyncio.run(generate_personas_async(num, target=target, condition=condition, lang=lang))

    with open(output, "w") as outfile:
        json.dump(personas, outfile, indent=2, ensure_ascii=False)

    print(f"Generated {num} personas and saved to {output}")


@click.command(name='list')
@click.argument('filename', type=click.Path(exists=True))
def list_personas(filename):
    """List personas from a JSON file."""

    with open(filename, 'r', encoding='utf-8') as infile:
        personas = json.load(infile)
    # Extract the necessary information from the personas
    data = []
    for persona in personas:
        data.append([
            persona.get('Name', ''),
            persona.get('Age', ''),
            persona.get('Gender', ''),
            persona.get('Residence', ''),
            persona.get('Occupation', '')
        ])

    # Display the data as a table
    table = PrettyTable()
    table.field_names = ['Name', 'Age', 'Gender', 'Residence', 'Occupation']
    table.align = 'l'
    for row in data:
        table.add_row(row)
    print(table)


def main():
    cli.add_command(generate)
    cli.add_command(list_personas)
    cli()


if __name__ == "__main__":
    main()

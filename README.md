# Polygene - Persona Generator

This Python script generates fictional personas based on specified conditions using the Polygene generator library. You
can generate a specified number of personas, and the output will be saved in a JSON file. Additionally, you can list the
personas from an existing JSON file in a tabular format.

## Usage

TODO: pip install support

### Generate Personas

To generate personas, use the following command:

```
poetry run polygene generate [num] --target [target] --condition [condition] --lang [lang] --output [output]
```

- `[num]`: (Required) The number of personas to generate.
- `[target]`: (Required) The target for generating personas.
- `[condition]`: (Required) The condition for generating personas.
- `[lang]`: (Optional) The language for generating personas (default: 'ja').
- `[output]`: (Optional) The name of the output JSON file (default: 'output.json').

Example:

```
poetry run polygene generate 3 --target 仮説検証のため --condition 日本人の男 性・女性を両方含む10代〜60代
```

### List Personas

To list personas from a JSON file, use the following command:

```
poetry run polygene list [filename]
```

- `[filename]`: (Required) The path to the JSON file containing the personas.

Example:

```
poetry run polygene list output.json
```

This command will display the personas in a tabular format, showing their Name, Age, Gender, Residence, and Occupation.

## License

This project is licensed under the MIT License.
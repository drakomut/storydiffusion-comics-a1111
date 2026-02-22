# Story Diffusion Comics A1111

A comprehensive tool for generating comics using diffusion models.

## Installation Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/drakomut/storydiffusion-comics-a1111.git
   cd storydiffusion-comics-a1111
   ```
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage Guide

To generate a comic, run the following command:
```bash
python generate_comic.py --input <input_file> --output <output_file>
```

### Command Line Parameters:
- `--input` : Path to the input file containing the story.
- `--output` : Desired path for the generated comic output.
- `--pages` : Number of pages to generate (default is 5).
- `--style` : Specify the art style of the comic (e.g., 'manga', 'superhero').

## Features
- **Automated Comic Generation**: Easily create comics from text stories using AI-driven models.
- **Customizable Styles**: Select different artistic styles for varied outputs.
- **Multi-page Support**: Generate multiple pages in one go for a complete comic experience.

## Parameters Documentation

| Parameter       | Type        | Description                                   |
|-----------------|-------------|-----------------------------------------------|
| `--input`       | String      | Input file for the story text.               |
| `--output`      | String      | Output file path for the generated comic.    |
| `--pages`       | Integer     | Total number of pages in the comic (default: 5). |
| `--style`       | String      | Specifies artistic style of comic.            |

For further information, consult the repository or the documentation files within it.
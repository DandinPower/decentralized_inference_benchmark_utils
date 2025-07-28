# Activation Visualizer

A Python tool to visualize neural network activation tensors as 3D heatmaps. The tool reads binary tensor files with a specific header format and generates interactive 3D surface plots.

## Features

- Reads binary tensor files with embedded dimension information
- Generates 3D surface plots using matplotlib
- Supports FLOAT32 data type
- Command-line interface with file input and output path specification
- Input file and output directory validation

## Installation

Install the required dependencies:

```bash
pip install numpy matplotlib
```

## Usage

```bash
python main.py -f <input_file> -o <output_image>
```

### Arguments

- `-f, --file`: Path to the binary tensor file (required)
- `-o, --output`: Output image path (required, e.g., `output.png`)

### Example

Run the visualization with the provided example file:

```bash
python main.py -f example.bin -o example_output.png
```

This will:
1. Read the tensor data from `example.bin`
2. Generate a 3D heatmap visualization
3. Save the plot as `example_output.png`

## Binary File Format

The tool expects binary files with the following header structure:

1. **Element Type** (uint8_t): Data type identifier (0 = FLOAT32)
2. **n_embed** (uint64_t): Embedding dimension (width)
3. **n_tokens** (uint64_t): Number of tokens (height)  
4. **Tensor Size** (uint64_t): Total size of tensor data in bytes
5. **Tensor Data** (void*): Raw tensor data

The header uses little-endian byte order with the format: `<BQQQ`

## Output

The tool generates a 3D surface plot with:
- X-axis: Embedding dimensions
- Y-axis: Token positions
- Z-axis: Activation values
- Color mapping using the 'viridis' colormap
- High-resolution output (300 DPI)
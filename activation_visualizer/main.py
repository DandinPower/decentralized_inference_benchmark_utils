import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import struct
import argparse
import sys
import os


def read_tensor_from_file(file_path: str):
    """
    Reads a tensor from a binary file with a specific header format.

    The binary file structure is:
    1. Element Type (uint8_t): 0 for FLOAT32.
    2. n_embed (uint64_t): Embedding dimension (width).
    3. n_tokens (uint64_t): Number of tokens (height).
    4. Tensor Size (uint64_t): Total size of the tensor data in bytes.
    5. Tensor Data (void*): Raw bytes of the tensor.

    Args:
        file_path (str): The path to the binary tensor file.

    Returns:
        A tuple containing:
        - np.ndarray: The tensor data as a 2D NumPy array.
        - int: Width (n_embed).
        - int: Height (n_tokens).
    """
    # Header format: little-endian, 1-byte unsigned char, 3x 8-byte unsigned long long
    header_format = '<BQQQ'
    header_size = struct.calcsize(header_format)

    with open(file_path, 'rb') as f:
        # Read and unpack the header
        header_bytes = f.read(header_size)
        if len(header_bytes) < header_size:
            print(f"❌ Error: Invalid file format. File is smaller than the header size.")
            sys.exit(1)

        element_type, n_embed, n_tokens, tensor_size_bytes = struct.unpack(
            header_format, header_bytes)

        # Currently, only FLOAT32 is supported
        if element_type == 0:  # FLOAT32
            dtype = np.float32
            element_size_bytes = 4
        else:
            print(
                f"❌ Error: Unsupported data type code: {element_type}. Only FLOAT32 (0) is supported.")
            sys.exit(1)

        # Calculate the number of elements
        if tensor_size_bytes % element_size_bytes != 0:
            print(
                f"❌ Error: Tensor size in bytes ({tensor_size_bytes}) is not a multiple of element size ({element_size_bytes}).")
            sys.exit(1)
        num_elements = tensor_size_bytes // element_size_bytes

        # Read the tensor data
        data = np.fromfile(f, dtype=dtype, count=num_elements)

        if data.size != num_elements:
            print(
                f"❌ Error: Could not read the expected number of elements. Expected {num_elements}, got {data.size}.")
            sys.exit(1)

        # Reshape the data to 2D using the embedded dimensions
        try:
            data_2d = data.reshape((n_tokens, n_embed))
        except ValueError as e:
            print(
                f"❌ Error reshaping array with dimensions {n_tokens}x{n_embed}: {e}")
            sys.exit(1)

        return data_2d, n_embed, n_tokens


def plot_3d_heatmap(data_2d: np.ndarray, file_path: str, output_path: str):
    """
    Generates and displays a 3D surface plot for the given 2D data.

    Args:
        data_2d (np.ndarray): The 2D NumPy array to visualize.
        file_path (str): Original file path for the plot title.
        output_path (str): Path where to save the output image.
    """
    y_dim, x_dim = data_2d.shape

    # Create a meshgrid for the x and y coordinates
    x_coords = np.arange(x_dim)
    y_coords = np.arange(y_dim)
    X, Y = np.meshgrid(x_coords, y_coords)

    # The 2D data array serves as the Z values
    Z = data_2d

    # Create the 3D plot
    fig = plt.figure(figsize=(12, 9))
    ax = fig.add_subplot(111, projection='3d')

    # Plot the surface
    surf = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')

    # Add a color bar for reference
    fig.colorbar(surf, ax=ax, shrink=0.6, aspect=10, label='Value')

    # Set labels and title
    ax.set_title(
        f"3D Heatmap for '{os.path.basename(file_path)}'", fontsize=16)
    ax.set_xlabel('embed', fontsize=12)
    ax.set_ylabel('tokens', fontsize=12)
    ax.set_zlabel('Value', fontsize=12)

    print(f"✅ Successfully generated plot. Saving to '{output_path}'...")
    plt.savefig(output_path, dpi=300)


def main():
    """Main function to parse arguments and run the visualization."""
    parser = argparse.ArgumentParser(
        description="Visualize a tensor from a binary file as a 3D heatmap. Dimensions are read from the file header.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        "-f", "--file", type=str, required=True,
        help="Path to the binary tensor file.")
    parser.add_argument(
        "-o", "--output", type=str, required=True,
        help="Output image path (e.g., output.png).")

    args = parser.parse_args()

    # Validate input file path
    if not os.path.exists(args.file):
        print(f"❌ Error: Input file not found at '{args.file}'")
        sys.exit(1)
    
    if not os.path.isfile(args.file):
        print(f"❌ Error: '{args.file}' is not a valid file")
        sys.exit(1)

    # Validate output folder exists
    output_dir = os.path.dirname(os.path.abspath(args.output))
    if not os.path.exists(output_dir):
        print(f"❌ Error: Output directory '{output_dir}' does not exist")
        sys.exit(1)
    
    if not os.path.isdir(output_dir):
        print(f"❌ Error: '{output_dir}' is not a valid directory")
        sys.exit(1)

    # 1. Read the tensor data from the file (now returns 2D array and dimensions)
    print(f"Reading tensor from '{args.file}'...")
    data_2d, width, height = read_tensor_from_file(args.file)
    print(
        f"Read tensor with dimensions {height}x{width} ({height * width} float32 elements).")

    # 2. Generate the plot
    plot_3d_heatmap(data_2d, args.file, args.output)


if __name__ == "__main__":
    main()

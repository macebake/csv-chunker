"""Takes a file with comma separated values, and returns
a new file with a specified number of those values per line.
The name of the new file, and the number of values per line
can be specified - it's set to new.txt and 10 values by default.
"""
import argparse
import os


def create_2d_list_of_ids(original_list, chunk_size):
    """This creates a list of lists with chunk_size values in them."""
    chunks_of_ids = []
    for i in range(0, len(original_list), chunk_size):
        chunks_of_ids.append(original_list[i:i+chunk_size])
    return chunks_of_ids


def write_chunked_file(chunked_list_of_ids, output_file_name):
    with open(output_file_name, 'w') as output_file:
        for chunk in chunked_list_of_ids:
            for i in chunk:
                output_file.write("{}".format(i + ', '))
            output_file.write(os.linesep)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-i',
        '--input_file',
        type=str,
        help='Path to input file',
        required=True
    )
    parser.add_argument(
        '-o',
        '--output_file',
        type=str,
        help='Path to new output file',
        default='new.txt'
    )
    parser.add_argument(
        '-s',
        '--chunk_size',
        type=int,
        help='Number of IDs per line',
        default=10
    )
    args = parser.parse_args()

    with open(args.input_file) as f:
        lines = f.read().strip()
        ids = lines.split(', ')

    write_chunked_file(
        create_2d_list_of_ids(ids, args.chunk_size),
        args.output_file
    )


if __name__ == "__main__":
    main()

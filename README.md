# CSV Chunker

Takes a file with comma separated values, and returns a new file with a specified number of those values per line. The name of the new file, and the number of values per line can be specified - it's set to new.txt and 10 values by default. 

## To run:

Download chunker.py and `cd` into the directory you've stored it in.

Run the program by using the following command:

```python chunker.py --input_file [path to & name of input file]```

If you're in a hurry, you can use `-i` instead of `--input_file`.

This command will chunk the input csv into 10 values per line, in a new file called new.txt. Read on for further options.

## To customize output:

For a custom output file name, and a custom chunk size, use the following command:

```python chunker.py --i [path to & name of input file] --output_file [path to & name of new output file] --chunk_size [number representing chunk size]```

You can use `-o` instead of `--output_file`.
You can also use `-s` instead of `--chunk_size`. 

An example of a full command is below. 

```python chunker.py -i raw_inputs.csv -o assigned_groups.csv -s 5```

This will take an input csv, and print 5 values per line in a new csv called assigned_groups.csv.


### Arguments key
| Argument | Shorthand | Required? | Input type | Description | Example |
| -------- | --------- | --------- | ---------- | ----------- | ------- |
| --input_file  | -i  | Yes | string | Path to & name of the input file you wish to manipulate. | `-i my_file.csv` |
| --output_file  | -o  | No | string | Path to & name you wish to assign to the output file. | `-o new_file.csv` |
| --chunk_size | -s | No | integer | Size of the "chunks" you wish to print to a single line of the output file. | `-s 8` |


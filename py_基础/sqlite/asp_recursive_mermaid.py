import csv


def generate_mermaid_csv(input_csv, output_csv):
    with (
        open(input_csv, "r", encoding="utf-8") as infile,
        open(output_csv, "w", encoding="utf-8", newline="") as outfile,
    ):
        reader = csv.reader(infile)

        print("graph TD", file=outfile)

        for row in reader:
            if len(row) >= 2:
                source = row[0].strip()
                target = row[1].strip()
                print(f"    {source} --> {target}", file=outfile)


if __name__ == "__main__":
    generate_mermaid_csv("asp_recursive_output.csv", "asp_mermaid_output.csv")

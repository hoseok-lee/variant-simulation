from biomart import BiomartServer
import csv


def get_mafs(
    n_variants: int,
    outfile: str
):

    server = BiomartServer("http://useast.ensembl.org/biomart")
    snp = server.datasets['hsapiens_snp']

    response = snp.search(
        {
            # Guarantees a MAF
            'filters': { 'minor_allele_freq_second': 0 },
            'attributes': [ 'refsnp_id', 'minor_allele_freq' ]
        },
    )

    with open(outfile, "w") as csv_file:

        writer = csv.writer(csv_file, delimiter = "\t")
        writer.writerow(['var_id', 'maf'])
        req_iter = response.iter_lines(decode_unicode = True)

        for _ in range(n_variants):
            line = next(req_iter)
            writer.writerow(line.split("\t"))


# Parse arguments
if __name__ == "__main__":

    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("n", help="number for variants to retrieve", type=int)
    parser.add_argument("-o", "--outfile", help="name of output TSV file", type=str, required=True)
    args = parser.parse_args()

    get_mafs(
        n_variants = args.n,
        outfile = args.outfile
    )

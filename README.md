# mer-freq

###### Database
- Merge split compressed files into single text file:
`cd db && cat 4mer_MCM.Bacteria.RefSeq.json.gz.0* | gunzip -c > 4mer_MCM.Bacteria.RefSeq.json`
- Convert json into pkl because it's about 5 sec instead of 12 sec to load:
`json2pickle.py 4mer_MCM.Bacteria.RefSeq.json 4mer_MCM.Bacteria.RefSeq.pkl`

###### Run example
- Query local genomes of interest against RefSeq:
`mer-freq --in-pkl ~/mer-freq/db/4mer_MCM.Bacteria.RefSeq.pkl --r-intra-sets --r-inter-db-sets --asm-acc filenames --min-correlation 0.9 -m fasta */*.fna.gz 1> 4mer-freq.assems_against_RefSeq.tsv 2> 4mer-freq.asm.err`

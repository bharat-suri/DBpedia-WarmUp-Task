# DBpedia-WarmUp-Task
This is for the Warm-up tasks proposed by DBPedia as part of GSoC 2018.
### Here is a list of the Warm-up tasks, that were designed to get familiar with the DBPedia workflow.
- [X] Run the extraction Framework.

### Next up, we have the tasks speciific to the GSoC project. These tasks are :

- [X] Read the paper (SPARQL as a foreign language [here](https://arxiv.org/abs/1708.07624))
- [ ] Train a Neural SPARQL model Machine Model on a DBPedia class of your choice.
- [ ] Run the RVA-based embedding algorithm on a DBpedia subset (read [notebook](https://akshayjagatap.wordpress.com/)).
- [ ] Run the [evaluation of existing KB embedding methods](https://github.com/nausheenfatma/embeddings/tree/master/gsoc2017-nausheen).

### Running the RVA-based embedding Algorithm.
1. I used the wikipedia [dump](https://dumps.wikimedia.org/enwiki/20180220/enwiki-20180220-pages-articles1.xml-p10p30302.bz2) as input to WikiExtractor.py
2. Next, we clean the xml dump and extract plain text using the script WikiExtractor.py using the following :
`python WikiExtractor.py ../enwiki-20180220-pages-articles1.xml -o text
python WikiExtractor.py ../enwiki-20180220-pages-articles1.xml --links -o output`
3. Then we make the global dictionary, AnchorDictionary.csv using the script MakeDictionary.py.
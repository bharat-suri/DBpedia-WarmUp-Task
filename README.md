# DBpedia-WarmUp-Task
This is for the Warm-up tasks proposed by DBPedia as part of GSoC 2018.
### Here is a list of the Warm-up tasks, that were designed to get familiar with the DBPedia workflow.
- [X] Run the extraction Framework.

### Next up, we have the tasks speciific to the GSoC project. These tasks are :

- [X] Read the paper (SPARQL as a foreign language [here](https://arxiv.org/abs/1708.07624))
- [X] Run the RVA-based embedding algorithm on a DBpedia subset (read [notebook](https://akshayjagatap.wordpress.com/)).
- [X] Train a word embedding algorithm (Word2Vec, GloVe)
- [ ] Run the [evaluation of existing KB embedding methods](https://github.com/nausheenfatma/embeddings/tree/master/gsoc2017-nausheen).

### Running the RVA-based embedding Algorithm.
1. I used the wikipedia [dump](https://dumps.wikimedia.org/enwiki/20180220/enwiki-20180220-pages-articles1.xml-p10p30302.bz2) as input to WikiExtractor.py
2. Next, we clean the xml dump and extract plain text using the script WikiExtractor.py using the following :
```python
python WikiExtractor.py ../enwiki-20180220-pages-articles1.xml -o text
python WikiExtractor.py ../enwiki-20180220-pages-articles1.xml -l -o output
```
3. Then we make the global dictionary, AnchorDictionary.csv using the script MakeDictionary.py.
```python
python MakeDictionary.py output/
```
4. Next up, we need the dictionary that maps the gender based pronouns with the help of dbo:Person, in EntityGender.csv .
```python
python CheckPerson.py output/
```
5. Now run the script MakeDictionary.py to change the text files to have the following format :
> Anarchism is a <a href="political%20philosophy">political philosophy</a> that advocates <a href="self-governance">self-governed</a> societies based on voluntary institutions. These are often described as <a href="stateless%20society">stateless societies</a>, although several authors have defined them more specifically as institutions based on non-<a href="Hierarchy">hierarchical</a> <a href="Free%20association%20%28communism%20and%20anarchism%29">free associations</a>. Anarchism holds the <a href="state%20%28polity%29">state</a> to be undesirable, unnecessary, and harmful.

This changes to :
> resource/Anarchism is a resource/Political_philosophy that advocates resource/Self-governance societies based on voluntary institutions. These are often described as resource/Stateless_society, although several authors have defined them more specifically as institutions based on non-resource/Hierarchy resource/Free_association_(communism_and_anarchism). resource/Anarchism holds the resource/State_(polity) to be undesirable, unnecessary, and harmful.

```python
python MakeDictionary.py updatedWiki/
```
6. We have everything we need to train our NN using the WikiTrainer.py module.
```python
python WikiTrainer.py updatedWiki/
```
7. Generate the embeddings using the RVA.py script
```python
python RVA.py updatedWiki/
```
8. Finally, we can plot the results : 
```python
python tsne.py
```
### Here is the final plot obtained after completely running the algorithm :

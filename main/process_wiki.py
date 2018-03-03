import logging
import os.path
import sys

from gensim.corpora import WikiCorpus

if __name__ == '__main__':
	program = os.path.basename(sys.argv[0])
	logger = logging.getLogger(program)

	logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s')
	logging.root.setLevel(level=logging.INFO)
	logger.info("running %s " % ' '.join(sys.argv))

	inp, outp = sys.argv[1:3]
	space = " "
	i = 0
	with open(outp, 'w') as output:
		wiki = WikiCorpus(inp, lemmatize=False, dictionary={})
		for text in wiki.get_texts():
			output.write(space.join(text) + '\n')
			i = i + 1

			if (i % 1000) == 0:
				logger.info("Saved " + str(i) + " articles")

		logger.info("Finished Saved " + str(i) + " articles")
from mrjob.job import MRJob
import logging

class WordFrequencyCounter(MRJob):

    def configure_args(self):
        """Allow user to specify a word to count as an argument."""
        super(WordFrequencyCounter, self).configure_args()
        self.add_passthru_arg('--word', type=str, help="Word to count")

    def mapper(self, _, line):
        """Splits the line into words and emits (word, 1) pairs."""
        target_word = self.options.word.lower()  # Get the target word
        words = line.lower().split()  # Convert line to lowercase and split words
        for word in words:
            if word == target_word:  # Only count the target word
                yield (word, 1)

    def reducer(self, word, counts):
        """Sums up the counts for each word."""
        yield (word, sum(counts))

if __name__ == '__main__':
    # ✅ Disable logging messages
    logging.getLogger().setLevel(logging.ERROR)
    WordFrequencyCounter.run()

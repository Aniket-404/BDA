from mrjob.job import MRJob
import logging

class StudentGradeCalculator(MRJob):

    def mapper(self, _, line):
        """Reads student name and score, then assigns a grade."""
        name, score = line.split()  # Split line into name and score
        score = int(score)  # Convert score to integer

        # Assign grades based on the score
        if 90 <= score <= 100:
            grade = "A"
        elif 80 <= score <= 89:
            grade = "B"
        elif 70 <= score <= 79:
            grade = "C"
        elif 60 <= score <= 69:
            grade = "D"
        else:
            grade = "F"

        yield (name, grade)

    def reducer(self, name, grades):
        """Output the student's name and final grade."""
        yield (name, list(grades)[0])

if __name__ == '__main__':
    # Disable logging messages
    logging.getLogger().setLevel(logging.ERROR)
    StudentGradeCalculator.run()

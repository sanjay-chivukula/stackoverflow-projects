from mrjob.job import MRJob
from mrjob.step import MRStep


class LeagueCount(MRJob):
    def steps(self):
        return [
            MRStep(
                mapper=self.mapper_get_league,
                reducer=self.reducer_count_league
            )
        ]

    def mapper_get_league(self, _, line):
        (Players, Team, League, year) = line.split('|')
        yield League, 1

    def reducer_count_league(self, key, values):
        yield key, sum(values)


if __name__ == '__main__':
    LeagueCount.run()

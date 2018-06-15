LIST_REGIONS = (
    'Caribe',
    'Andina',
    'Pacifica',
    'Oriental',
    'Eje Cafetero',
)


class Person:

    def __init__(self, first_name, last_name, age, gender, region):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.region = region

    @property
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self) -> str:
        return self.get_full_name


class Candidate(Person):

    def __init__(self, *args, **kwargs):
        super(Candidate, self).__init__(*args, **kwargs)


class Vote:
    def __init__(self, candidate, person):
        self.candidate = candidate
        self.__sufragant = person

    def __str__(self) -> str:
        return f'Candidate: {self.candidate.get_full_name}'


class NationalRegistry:
    peoples = []
    candidates = []
    votes = []

    def add_candidate(self, candidate):
        self.candidates.append(*candidate)

    def add_person(self, person):
        self.peoples.append(person)

    def add_vote(self, vote):
        self.votes.append(vote)

    def get_total_votes_by_candidates(self, candidate):
        list_votes_candidate = list(
            filter(lambda x: x.candidate == candidate, self.votes)
        )
        return len(list_votes_candidate)

    def get_total_votes_by_age_range(self, *age_range):
        if age_range is None or len(age_range) < 2:
            age_range = [18, 25]
        start, stop = age_range
        list_votes_candidate = list(
            filter(lambda x: start >= x.age <= stop, self.votes)
        )
        return len(list_votes_candidate)

    def filters(self, **kwargs):
        return list(
            filter(
                lambda obj: all([hasattr(obj, attr) and getattr(obj, attr) == value for attr, value in kwargs.items()]),
                self.votes
            ))

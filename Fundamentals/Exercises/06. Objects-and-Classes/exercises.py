class Exercise:
    def __init__(self, topic, course_name, judge_contest_link, problems):
        self.__topic = self.set_topic(topic)
        self.c_name = course_name
        self.judge_link = judge_contest_link
        self.problems = problems.split(', ')

    def set_topic(self, topic):
        if not isinstance(topic, str):
            raise Exception
        return topic

    def get_topic(self):
        return self.__topic

    def __str__(self):
        problems_str = '\n'.join([f'{index + 1}. {problem}' for index, problem in enumerate(self.problems)])
        result = [
            f'Exercises: {self.get_topic()}',
            f'Problems for exercises and homework for the "{self.c_name}" course @ SoftUni.',
            f'Check your solutions here: {self.judge_link}',
            problems_str
        ]

        return '\n'.join(result)

    
data = input()
exercises = []
while data != 'go go go':
    data_list = data.split(' -> ')
    topic = data_list[0]
    course_name = data_list[1]
    judge_contest_link = data_list[2]
    problems = data_list[3]

    exercise = Exercise(topic, course_name, judge_contest_link, problems)
    exercises.append(exercise)
    data = input()

[print(exercise) for exercise in exercises]
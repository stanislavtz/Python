class Gladiator:
    def __init__(self, name, technique):
        self.__techniques_list = []
        self.name = name
        self.techniques = self.set_technique(technique)

    def set_technique(self, technique):
        if not technique.name in list(map(lambda t: t.name, self.__techniques_list)):
            self.__techniques_list.append(technique)
        else:
            current_technique = list(filter(lambda t: t.name == technique.name, self.techniques))[0]
            if current_technique.skill < technique.skill:
                current_technique.update_skill(technique.skill)

        self.power = self.calculate_power()
        return self.__techniques_list

    def calculate_power(self):
        return sum(list(map(lambda t: t.skill, self.__techniques_list)))

    def __str__(self):
        t_l = sorted(self.techniques, key=lambda t: (-t.skill, t.name))
        techniques_list = list(map(lambda t: f"- {t.name} <!> {t.skill}", t_l))
        return f"{self.name}: {self.power} skill\n" + '\n'.join(techniques_list)


class Technique:
    def __init__(self, name, skill):
        self.name = name
        self. skill = int(skill)

    def update_skill(self, value):
        self.skill = value


arena = []
data = input()
while data != 'Ave Cesar':
    if len(data.split((' -> '))) == 3:
        name, technique, skill = data.split(' -> ')
        technique_obj = Technique(technique, skill)

        if not name in list(map(lambda g: g.name, arena)):
            gladiator = Gladiator(name, technique_obj)
            arena.append(gladiator)
        else:
            gladiator = list(filter(lambda g: g.name == name, arena))[0]
            gladiator.set_technique(technique_obj)
    else:
        first_gladiator_name, second_gladiator_name = data.split(' vs ')
        try:
            first_gladiator = list(filter(lambda g: g.name == first_gladiator_name, arena))[0]
            second_gladiator = list(filter(lambda g: g.name == second_gladiator_name, arena))[0]

            temp = set(list(map(lambda t: t.name, first_gladiator.techniques))).intersection(
                set(list(map(lambda t: t.name, second_gladiator.techniques))))

            if len(temp) == 0:
                data = input()
                continue

            if first_gladiator.power > second_gladiator.power:
                arena.remove(second_gladiator)
            elif first_gladiator.power < second_gladiator.power:
                arena.remove(first_gladiator)
        except:
            pass

    data = input()

for g in sorted(arena, key=lambda g: (-g.power, g.name)):
    print(g)
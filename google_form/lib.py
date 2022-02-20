data = list()


class Simple:
    def __init__(self):
        self.simple_list = list()
        self.url = ""

    def simple_entry(self) -> list:
        for value in data:
            if value is not None and len(value) == 5:
                if isinstance(value[4][0], list) and len(value[4][0]) == 9:
                    entry, ans = value[4][0][0], self.simple_ans(value)
                    no = data.index(value)
                    data.remove(value)
                    data.insert(no, None)
                    yield [entry, ans]

    @staticmethod
    def simple_ans(value: list) -> str:
        # if "" in value[1]:      # find keyword in question
        #     answer = 0          # change this for your answer
        #     choice = value[4][0][1]
        #     return choice[answer][0]
        if value[4][0][2] == 1 and len(value[4][0][1]) == 1:
            return value[4][0][1][0][0]
        return value[4][0][1][0][0]

    def get_list(self):
        for i in self.simple_entry():
            self.simple_list.append(i)

    def get_url(self):
        self.get_list()
        for q in self.simple_list:
            entry = "&entry." + str(q[0]) + "=" + q[1]
            self.url += entry
        return self.url


class Short:
    def __init__(self):
        self.short_list = list()
        self.url = ""

    @staticmethod
    def short_entry() -> list[list]:
        for value in data:
            if value is not None and len(value) == 5:
                entry_list = value[4][0]
                if isinstance(entry_list, list) and len(entry_list) == 3:
                    entry, question = entry_list[0], value[1]
                    no = data.index(value)
                    data.remove(value)
                    data.insert(no, None)
                    yield [entry, question]

    def short_ans(self):
        for q in self.short_list:
            if "姓名" in q[1]:
                q[1] = ""
            elif "身分證字號" in q[1]:
                q[1] = ""
            elif "地址" in q[1]:
                q[1] = ""
            else:
                q[1] = ""

    def get_list(self):
        for i in self.short_entry():
            self.short_list.append(i)
        self.short_ans()

    def get_url(self):
        self.get_list()
        for q in self.short_list:
            if q[1] != "":
                entry = "&entry." + str(q[0]) + "=" + q[1]
                self.url += entry
        return self.url


class Date:
    def __init__(self):
        self.entry = ""
        self.url = ""

    def get_url(self):
        self.date_entry()
        self.date_ans()
        return self.url

    def date_entry(self):
        for value in data:
            if value is not None and len(value) == 5:
                entry = value[4][0]
                if type(entry) == list and len(entry) == 8:
                    no = data.index(value)
                    data.remove(value)
                    data.insert(no, None)
                    self.entry = entry[0]

    def date_ans(self):
        if self.entry == "":
            return ""

        y, m, d = 2022, 2, 20

        result = "&entry." + str(self.entry)
        result += "={:4d}-{:02d}-{:02d}".format(y, m, d)
        self.url = result


class Time:
    def __init__(self):
        self.entry = ""
        self.url = ""

    def get_url(self):
        self.time_entry()
        self.time_ans()
        return self.url

    def time_entry(self):
        for value in data:
            if value is not None and len(value) == 5:
                entry = value[4][0]
                if type(entry) == list and len(entry) == 7:
                    no = data.index(value)
                    data.remove(value)
                    data.insert(no, None)
                    self.entry = entry[0]

    def time_ans(self):
        if self.entry == "":
            return ""

        h, m = 13, 00

        result = "&entry."+str(self.entry)
        result += "={:02d}:{:02d}".format(h, m)
        self.url = result


def combine_url(url):
    url += Simple().get_url()
    url += Short().get_url()
    # url += Date().get_url()
    # url += Time().get_url()
    return url

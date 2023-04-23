import yapsy.IPlugin
import logging


class LocatedFile:
    def __init__(self, path, tags):
        self.path = path
        self.tags = tags


class TaggedData:
    tags = []


class TunnerCommand(yapsy.IPlugin.IPlugin):
    logger_name = "comex.logger"
    cmd_type = ""

    @property
    def logger(self):
        return logging.getLogger(self.logger_name)

    def log(self, level, message):
        return self.logger.log(level, f"[{self.cmd_type}] {message}")

    def filter_by_tags(self, pattern, objects):
        for obj in objects:
            for tag in obj.tags:
                if pattern in tag:
                    yield obj


class ReParser:
    def __init__(self):
        self.text = None

    def parse(self, text, rules):
        self.text = text
        result = []

        for rule in rules:
            result += self.parse_rule(rule)

        return result

    def parse_rule(self, rule):
        result = []
        for regex in rule.include:
            for match in regex.finditer(self.text):
                re_match = ReMatch()
                re_match.match = match
                re_match.rule = rule
                re_match.text = match.group(0)

                re_match.range.line.start = self.text.count("\n", 0, match.start())
                re_match.range.line.end = self.text.count("\n", 0, match.end())

                re_match.range.char.start = match.start()
                re_match.range.char.end = match.end()

                result.append(re_match)

        return result



class ReRangeItem:
    def __init__(self):
        self.start = None
        self.end = None


class ReRange:
    def __init__(self):
        self.line = ReRangeItem()
        self.char = ReRangeItem()


class ReMatch:
    def __init__(self):
        self.range = ReRange()
        self.match = None
        self.rule = None
        self.text = None


class ReRule:
    def __init__(self):
        self.id = None
        self.include = []
        self.exclude = []
        self.tags = []


class Row:
    def __init__(self):
        self.text = None
        self.number = None
        self.matches = []
        self.source = None
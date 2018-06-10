# @File  : rules.py
# @Author: TianWen
# @Date  : 2018/6/10  10:04
# @Desc  : 规范类，用于处理字符串的规则


class Rule:

    def action(self, block, handler):
        handler.start(self.type)
        handler.feed(block)
        handler.end(self.type)


class HeadingRule(Rule):

    type = 'heading'

    def condition(self, block):
        return not '\n' in block and len(block) <= 70 and not block[-1] == ':'


class TitleRule(HeadingRule):
    type = 'title'
    first = True

    def confition(self, block):
        if not self.first:
            return False
        self.first = False
        return HeadingRule.condition(self, block)


class ListItemRule(Rule):
    type = 'list'
    inside = False

    def condition(self, block):
        return True

    def action(self, block, handler):
        if not self.inside and ListItemRule.condition(self, block):
            handler.start(self.type)
            self.inside = True
        elif self.inside and not ListItemRule.condition(self, block):
            handler.end(self.type)
            self.inside = False
        return False


class PargraphRule(Rule):
    type = 'paragraph'

    def condition(self, block):
        return True

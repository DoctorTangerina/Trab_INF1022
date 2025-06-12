from sly import Parser

from lexer import ObsActLexer

class ObsActParser(Parser):
    debugfile = "parser.out"
    tokens = ObsActLexer.tokens

    @_('DEVICES')
    def PROGRAM(self, p):
        return "[\n" + p.DEVICES + "\n]"

    @_('DEVICES CMDS')
    def PROGRAM(self, p):
        return "[\n" + p.DEVICES + p.CMDS + "\n]"

    @_('DEVICE')
    def DEVICES(self, p):
        return p.DEVICE

    @_('DEVICE DEVICES')
    def DEVICES(self, p):
        return p.DEVICE + ",\n" + p.DEVICES

    @_('device ":" "{" namedevice "}"')
    def DEVICE(self, p):
       return f'{{"DEVICE" : "{p.namedevice}"}}'

    @_('device ":" "{" namedevice "," observation "}"')
    def DEVICE(self, p):
        return f'{{"DEVICE" : "{p.namedevice}, {p.observation}"}}'

    @_('CMD "."')
    def CMDS(self, p):
        return p.CMD

    @_('CMD "." CMDS')
    def CMDS(self, p):
        return p.CMD + ",\n" + p.CMDS

    @_('ATTRIB')
    def CMD(self, p):
        return p.ATTRIB

    @_('ACT')
    def CMD(self, p):
        return p.ACT

    @_('set observation "=" VAR')
    def ATTRIB(self, p):
        return f',\n{{"ATTRIB" : "{p.observation}, {p.VAR}"}}'

    @_('ACTION namedevice')
    def ACT(self, p):
        return f',\n{{"{p.ACTION}" : "{p.namedevice}"}}'

    @_('action')
    def ACTION(self, p):
        return f'{p.action}'

    @_('boolean')
    def VAR(self, p):
        return f'{p.boolean}'

    @_('number')
    def VAR(self, p):
        return f'{p.number}'

    def error(self, t):
        return f"Syntax error token={t}"

parser = ObsActParser()
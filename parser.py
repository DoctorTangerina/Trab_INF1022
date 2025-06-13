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
        return f'{{"DEVICE_OBS" : "{p.namedevice}, {p.observation}"}}'

    @_('CMD "."')
    def CMDS(self, p):
        return p.CMD

    @_('CMD "." CMDS')
    def CMDS(self, p):
        return p.CMD + p.CMDS

    @_('OBSACT')
    def CMD(self, p):
        return p.OBSACT

    @_('ATTRIB')
    def CMD(self, p):
        return p.ATTRIB

    @_('ACT')
    def CMD(self, p):
        return p.ACT

    @_('set observation "=" VAR')
    def ATTRIB(self, p):
        return f',\n{{"ATTRIB" : "{p.observation}, {p.VAR}"}}'

    @_('enviar alerta "(" msg ")" para todos ":" NAME')
    def ACT(self, p):
        msg = p.msg.replace('"', '\\"')
        return f',\n{{"ALERT_ALL" : "{msg}, ' + p.NAME + f'"}}'

    @_('enviar alerta "(" msg "," observation ")" namedevice')
    def ACT(self, p):
        msg = p.msg.replace('"', '\\"')
        return f',\n{{"ALERT_OBS" : "{msg}, {p.observation}, {p.namedevice}"}}'

    @_('enviar alerta "(" msg ")" namedevice')
    def ACT(self, p):
        msg = p.msg.replace('"', '\\"')
        return f',\n{{"ALERT" : "{msg}, {p.namedevice}"}}'

    @_('ACTION namedevice')
    def ACT(self, p):
        return f',\n{{"{p.ACTION}" : "{p.namedevice}"}}'

    @_('se OBS entao ACT senao ACT')
    def OBSACT(self, p):
        return f',\n{{"IF" : "' + p.OBS + f'"}}' + p.ACT0 + f',\n{{"ELSE" : ""}}' + p.ACT1 + f',\n{{"END" : ""}}'

    @_('se OBS entao ACT')
    def OBSACT(self, p):
        return f',\n{{"IF" : "' + p.OBS + f'"}}' + p.ACT + f',\n{{"END" : ""}}'

    @_('observation oplogic VAR "&" "&" OBS')
    def OBS(self, p):
        return p.observation + p.oplogic + p.VAR + "&&" + p.OBS

    @_('observation oplogic VAR')
    def OBS(self, p):
        return p.observation + p.oplogic + p.VAR

    @_('action')
    def ACTION(self, p):
        return f'{p.action}'

    @_('namedevice "," NAME')
    def NAME(self, p):
        return f'{p.namedevice}, ' + p.NAME

    @_('namedevice')
    def NAME(self, p):
        return f'{p.namedevice}'

    @_('boolean')
    def VAR(self, p):
        return f'{p.boolean}'

    @_('number')
    def VAR(self, p):
        return f'{p.number}'

    def error(self, t):
        return f"Syntax error token={t}"

parser = ObsActParser()
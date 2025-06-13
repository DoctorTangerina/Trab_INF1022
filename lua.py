def lua_device(args: list[str]):
    s = '%s = "%s"\n' % (args[0], args[0])
    return s

def lua_device_obs(args: list[str]):
    s = '%s = "%s"\n%s = nil\n' % (args[0], args[0], args[1])
    return s

def lua_attrib(args: list[str]):
    s = '%s = %s\n' % (args[0], args[1])
    return s

def lua_if(args: list[str]):
    s = 'if %s then\n\t' % (args[0].replace('&&', ' and '))
    return s

def lua_else(args: list[str]):
    return 'else\n\t'

def lua_end(args: list[str]):
    return 'end\n'

def lua_alert(args: list[str]):
    return 'alert(%s, %s)\n' % (args[1], args[0])

def lua_alert_obs(args: list[str]):
    return 'alert(%s, %s, %s)\n' % (args[2], args[0], args[1])

def lua_alert_all(args: list[str]):
    msg = args[0]
    l = "{"
    for arg in args[1:-1]:
        l += arg + ', '
    l += args[-1] + '}'
    return 'alert_all(%s, %s)\n' % (l, msg)

def lua_off(args: list[str]):
    return 'off(%s)\n' % (args[0])

def lua_on(args: list[str]):
    return 'on(%s)\n' % (args[0])

lua_dict = {
    'DEVICE' : lua_device,
    'DEVICE_OBS' : lua_device_obs,
    'ATTRIB' : lua_attrib,
    'IF' : lua_if,
    'ELSE' : lua_else,
    'END' : lua_end,
    'ALERT' : lua_alert,
    'ALERT_OBS' : lua_alert_obs,
    'ALERT_ALL' : lua_alert_all,
    'desligar' : lua_off,
    'ligar' : lua_on
}
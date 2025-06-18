def lua_precode():
    return '''-- Função ligar
function on(namedevice)
  print(namedevice .. " ligado!")
end

-- Função desligar
function off(namedevice)
  print(namedevice .. " desligado!")
end

-- Função alerta com 2 ou 3 parâmetros (simulando sobrecarga)
function alert(namedevice, msg, var)
  print(namedevice .. " recebeu o alerta :")

  if var == nil then
    print(msg)
  else
    print(msg .. " " .. tostring(var))
  end
end

-- Função alerta todos os devices
function alert_all(msg, ...)
  local dispositivos = {...}

  for i = 1, #dispositivos do
    alert(dispositivos[i], msg)
  end
end

'''

def lua_device(args: list[str]):
    s = '%s = "%s"\n' % (args[0], args[0])
    return s

def lua_device_obs(args: list[str]):
    s = '%s = "%s"\n%s = 0\n' % (args[0], args[0], args[1])
    return s

def lua_attrib(args: list[str]):
    s = '%s = %s\n' % (args[0], args[1])
    return s

def lua_if(args: list[str]):
    s = 'if %s then\n\t' % (args[0].replace('&&', ' and ').replace('!=', '~='))
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
    r = 'alert_all(%s, '
    for arg in args[1:-1]:
        r += arg + ', '
    r += args[-1] + ')\n'
    return r % (msg)

def lua_off(args: list[str]):
    return 'off(%s)\n' % (args[0])

def lua_on(args: list[str]):
    return 'on(%s)\n' % (args[0])

def lua_after_code():
    return ''

lua_dict = {
    'PRECODE' : lua_precode,
    'DEVICE' : lua_device,
    'DEVICE_OBS' : lua_device_obs,
    'ATTRIB' : lua_attrib,
    'IF' : lua_if,
    'ELSE' : lua_else,
    'ENDIF' : lua_end,
    'ALERT' : lua_alert,
    'ALERT_OBS' : lua_alert_obs,
    'ALERT_ALL' : lua_alert_all,
    'desligar' : lua_off,
    'ligar' : lua_on,
    'AFTERCODE' : lua_after_code
}
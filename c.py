obs_table = {}

def c_precode():
    return '''#include <stdio.h>
#include <string.h>

typedef enum { INT, BOOLEAN, NONE } DataType;

typedef struct {
    char name[50];
    char obsName[50];
    int obsInt;
    int obsBool;
    DataType dataType;
} Device;

void on(Device *device) {
    printf("%s ligado!\\n", device->name);
}

void off(Device *device) {
    printf("%s desligado!\\n", device->name);
}

void setObsInt(Device *device, int obs) {
    device->dataType = INT;
    device->obsInt = obs;
}

void setObsBool(Device *device, int obs) {
    device->dataType = BOOLEAN;
    device->obsBool = obs;
}

int getObsInt(Device *device) {
    return device->obsInt;
}

int getObsBool(Device *device) {
    return device->obsBool;
}

void alert(Device *device, const char *msg) {
    printf("%s recebeu o alerta :\\n", device->name);
    printf("%s\\n", msg);
}

void alert_obs(Device *device, const char *msg, const char *extra) {
    printf("%s recebeu o alerta :\\n", device->name);
    printf("%s %s\\n", msg, extra);
}

void alert_all(const char *msg, Device **devices, int count) {
    for (int i = 0; i < count; i++) {
        alert(devices[i], msg);
    }
}

int main() {
'''

def c_device(args: list[str]):
    device = args[0]
    return f'\tDevice {device} = {{"{device}", "", 0, 0, NONE}};\n'

# def c_device_obs(args: list[str]):
#     device = args[0]
#     obs = args[1]
#     obs_table[obs] = device
#     return f'\tDevice {device} = {{"{device}", "{obs}", 0, 0, NONE}};\n'

def c_device_obs(args: list[str]):
    device = args[0]
    obs = args[1]
    obs_table[obs] = device
    return f'\tDevice {device} = {{"{device}", "{obs}", 0, 0, NONE}};\n'

def c_attrib(args: list[str]):
    try:
        device = obs_table[args[0]]
    except KeyError:
        return ''
    value = args[1].lower()
    if value in ['true', 'false']:
        bool_value = '1' if value == 'true' else '0'
        return f'\tsetObsBool(&{device}, {bool_value});\n'
    else:
        return f'\tsetObsInt(&{device}, {value});\n'

def aux_if(conds):
    s = ''
    for cond in conds[:-1]:
        var, op, val = cond.strip().split(' ')
        try:
            device = obs_table[var]
            val = val.lower()
            if val.isdigit():
                s += f'getObsInt(&{device}) {op} {val} && '
            else:
                bool_val = '1' if val == 'true' else '0'
                s += f'getObsBool(&{device}) {op} {bool_val} && '
        except KeyError:
            return ''
    var, op, val = conds[-1].strip().split(' ')
    try:
        device = obs_table[var]
        val = val.lower()
        if val.isdigit():
            s += f'getObsInt(&{device}) {op} {val}'
        else:
            bool_val = '1' if val == 'true' else '0'
            s += f'getObsBool(&{device}) {op} {bool_val}'
    except KeyError:
        return ''
    return s

def c_if(args: list[str]):
    conds = args[0].split('&&')
    s = aux_if(conds)
    return f'\tif ({s}) {{\n'

def c_else(args: list[str]):
    return '\t} else {\n'

def c_endif(args: list[str]):
    return '\t}\n'

def c_alert(args: list[str]):
    msg = args[0]
    device = args[1]
    return f'\talert(&{device}, {msg});\n'

# def c_alert_obs(args: list[str]):
#     msg = args[0]
#     var = args[1]
#     device = args[2]
#     return f'\talert_obs(&{device}, {msg}, {var});\n'

def c_alert_obs(args: list[str]):
    msg = args[0]
    var = args[1]
    device = args[2]
    
    if var in obs_table:
        device_var = obs_table[var]
        return f'\tchar buffer[100];\n\tsprintf(buffer, "%d", getObsInt(&{device_var}));\n\talert_obs(&{device}, {msg}, buffer);\n'
    else:
        return f'\talert_obs(&{device}, {msg}, {var});\n'

def c_alert_all(args: list[str]):
    devices = args[1:]
    count = len(devices)
    devices_list = '{' + ', '.join(f'&{d}' for d in devices) + '}'
    return f'\tDevice *devices[] = {devices_list};\n\talert_all({args[0]}, devices, {count});\n'

def c_off(args: list[str]):
    device = args[0]
    return f'\toff(&{device});\n'

def c_on(args: list[str]):
    device = args[0]
    return f'\ton(&{device});\n'

def c_after_code():
    return '\treturn 0;\n}\n'

c_dict = {
    'PRECODE' : c_precode,
    'DEVICE' : c_device,
    'DEVICE_OBS' : c_device_obs,
    'ATTRIB' : c_attrib,
    'IF' : c_if,
    'ELSE' : c_else,
    'ENDIF' : c_endif,
    'ALERT' : c_alert,
    'ALERT_OBS' : c_alert_obs,
    'ALERT_ALL' : c_alert_all,
    'desligar' : c_off,
    'ligar' : c_on,
    'AFTERCODE' : c_after_code
}

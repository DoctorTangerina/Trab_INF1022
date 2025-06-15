obs_table = {}

def java_precode():
    return '''enum DataType {
    INT,
    BOOLEAN,
    NONE
}

class Device {
    String name;
    String obsName;
    int obsInt;
    boolean obsBool;
    DataType dataType;
    
    public Device(String name) {
        this.name = name;
    }
    
    public Device(String name, String obsName) {
        this(name);
        this.obsName = obsName;
        dataType = DataType.NONE;
    }
    
    public void setObs(int obs) {
        dataType = DataType.INT;
        obsInt = obs;
    }
    
    public void setObs(boolean obs) {
        dataType = DataType.BOOLEAN;
        obsBool = obs;
    }
    
    public Integer getObsInt() {
        return dataType == DataType.INT ? obsInt : null;
    }

    public Boolean getObsBool() {
        return dataType == DataType.BOOLEAN ? obsBool : null;
    }
    
    public void on() {
        System.out.println(this.name + " ligado!");
    }
    
    public void off() {
        System.out.println(this.name + " desligado!");
    }
}

public class Main {
    public static void alert(Device device, String msg) {
        System.out.println(device.name + " recebeu o alerta :");
        System.out.println(msg);
    }

    public static void alert(Device device, String msg, String extra) {
        System.out.println(device.name + " recebeu o alerta :");
        System.out.println(msg + " " + extra);
    }

    public static void alertAll(String msg, Device... devices) {
        for (Device device : devices) {
            alert(device, msg);
        }
    }
    
    public static void main(String[] args) {
'''

def java_device(args: list[str]):
    device = args[0]
    return f'\t\tDevice {device} = new Device("{device}");'

def java_device_obs(args: list[str]):
    device = args[0]
    obs = args[1]
    obs_table[obs] = device
    return f'\t\tDevice {device} = new Device("{device}", "{obs}");\n'

def java_attrib(args: list[str]):
    try:
        device = obs_table[args[0]]
    except KeyError:
        return ''
    value = args[1].lower()
    return f'\t\t{device}.setObs({value});\n'

def aux_if(conds):
    s = ''
    for cond in conds[:-1]:
        var, op, val = cond.split(' ')
        try:
            device = obs_table[var]
            val = val.lower()
            if val.isdigit():
                s += f'{device}.getObsInt() {op} {val} && '
            else:
                s += f'{device}.getObsBool() {op} {val} && '
        except KeyError:
            return ''
    var, op, val = conds[-1].split(' ')
    try:
        device = obs_table[var]
        val = val.lower()
        if val.isdigit():
            s += f'{device}.getObsInt() {op} {val}'
        else:
            s += f'{device}.getObsBool() {op} {val}'
    except KeyError:
        return ''
    return s

def java_if(args: list[str]):
    conds = args[0].split('&&')
    s = aux_if(conds)
    return f'\t\tif ({s}) {{\n\t'

def java_else(args: list[str]):
    return f'\t\t}} else {{\n\t'

def java_endif(args: list[str]):
    return f'\t\t}}\n'

def java_alert(args: list[str]):
    device = args[1]
    msg = args[0]
    return f'\t\talert({device}, {msg});\n'

def java_alert_obs(args: list[str]):
    device = args[1]
    msg = args[0]
    var = args[2]
    return f'\t\talert({device}, {msg}, {var});\n'

def java_alert_all(args: list[str]):
    s = '\t\talertAll(' + args[0] + ', '
    for arg in args[1:-1]:
        s += arg + ', '
    s += args[-1] + ');\n'
    return s

def java_off(args: list[str]):
    device = args[0]
    return f'\t\t{device}.off();\n'

def java_on(args: list[str]):
    device = args[0]
    return f'\t\t{device}.on();\n'

def java_after_code():
    return '\t}\n}'

java_dict = {
    'PRECODE' : java_precode,
    'DEVICE' : java_device,
    'DEVICE_OBS' : java_device_obs,
    'ATTRIB' : java_attrib,
    'IF' : java_if,
    'ELSE' : java_else,
    'ENDIF' : java_endif,
    'ALERT' : java_alert,
    'ALERT_OBS' : java_alert_obs,
    'ALERT_ALL' : java_alert_all,
    'desligar' : java_off,
    'ligar' : java_on,
    'AFTERCODE' : java_after_code
}
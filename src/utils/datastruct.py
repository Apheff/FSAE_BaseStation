class Data:
    def __init__(self, code: str, name: str, value: int):
        self.code = code
        self.name = name
        self.value = value

    def __str__(self):
        return f"Codice: {self.code} | Nome: {self.name} | Valore: {self.value}"


class DataStruct:
    def __init__(self, name, code, value):
        self.datas = []
        self.datas.append(Data("RPM", "RPM", 0))
        self.datas.append(Data("Brake", "BS", 0))
        self.datas.append(Data("Oil_T", "OT", 0))
        self.datas.append(Data("Oil_P", "OP", 0))
        self.datas.append(Data("Water_T", "WT", 0))
        self.datas.append(Data("Intake_P", "IP", 0))
        self.datas.append(Data("Intake_T", "IT", 0))
        self.datas.append(Data("Lambda", "LS", 0))
        self.datas.append(Data("Tire_P_T_PADX", "PADX", 0))
        self.datas.append(Data("Tire_P_T_PASX", "PASX", 0))
        self.datas.append(Data("Tire_P_T_PBDX", "PBDX", 0))
        self.datas.append(Data("Tire_P_T_PBSX", "PBSX", 0))
        self.datas.append(Data("Accelerometer", "TP", 0))
        self.datas.append(Data("Throttle", "TP", 0))
        self.datas.append(Data("Clutch_Sensor", "CS", 0))
        self.datas.append(Data("Shift_Paddles", "M", 0))
        self.datas.append(Data("Pilot_HID", "D", 0))
        self.datas.append(Data("Battery", "BV", 0))
        self.datas.append(Data("Supension_Travel_SADX", "SADX", 0))
        self.datas.append(Data("Supension_Travel_SASX", "SASX", 0))
        self.datas.append(Data("Supension_Travel_SBDX", "SBDX", 0))
        self.datas.append(Data("Supension_Travel_SBSX", "SBSX", 0))
        self.datas.append(Data("Wheel_Rotation_RADX", "RADX", 0))
        self.datas.append(Data("Wheel_Rotation_RASX", "RASX", 0))
        self.datas.append(Data("Wheel_Rotation_RBDX", "RBDX", 0))
        self.datas.append(Data("Wheel_Rotation_RBSX", "RBSX", 0))

    def print_datas(self):
        for d in self.datas:
            print(d)

    def find_by_code(self, code: str):
        for var in self.datas:
            if var.code == code:
                return var
        return None

    def find_by_name(self, nome: str):
        for var in self.datas:
            if var.name == nome:
                return var
        return None

    def set_valore(self, code: str, nuovo_valore: int) -> bool:
        var = self.find_by_code(code)
        if var:
            var.value = nuovo_valore
            return True
        return False

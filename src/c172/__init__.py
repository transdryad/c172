from math import ceil


def press_alt(altitude: int, alt_setting: float) -> float:
    fin_alt = ((29.92 - alt_setting) * 1000) + altitude  # adjust altitude for altimeter setting
    return fin_alt


def dense_alt(oat: int, altitude: int, alt_setting: float) -> int:
    palt = press_alt(altitude, alt_setting)  # get pressure altitude
    print(f"Pressure altitude: {ceil(palt)}")
    isa_temp = 15 - ((1.98 * altitude)/1000)  # get isa temp at true/field altitude
    return ceil(palt + (118.8 * (oat - isa_temp)))  # get density altitude and round up


def main():
    print("Hello from c172 calculator!")
    oat = int(input("Air temp (C): "))
    altitude = int(input("True/Field altitude (feet): "))
    alt_setting = float(input("Altimeter setting (\"Hg): "))
    print(f"Density altitude: {dense_alt(oat, altitude, alt_setting)}")


if __name__ == "__main__":
    main()

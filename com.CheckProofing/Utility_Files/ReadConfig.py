import configparser


def readconfigData(section, key):
    config = configparser.ConfigParser(interpolation=None)
    config.read("../ConfigData/Driver/DataPage.ini")
    return config.get(section, key)


def readabcData(section, key):
    config = configparser.ConfigParser(interpolation=None)
    config.read("../ConfigData/canvas/abc.ini")
    return config.get(section, key)


"""Config Data start below"""


def readCopyTextData(section, key):
    config = configparser.ConfigParser(interpolation=None)
    config.read("../Test_Campaign_2021/ConfigData/Footer.ini")
    return config.get(section, key)


def readfooterData(section, key):
    config = configparser.ConfigParser(interpolation=None)
    config.read("../Test_Campaign_2021/ConfigData/Footer.ini")
    return config.get(section, key)


def readModuleURLData(section, key):
    config = configparser.ConfigParser(interpolation=None)
    config.read("../Test_Campaign_2021/ConfigData/ModuleURL.ini")
    return config.get(section, key)


def readTermsConditionData(section, key):
    config = configparser.ConfigParser(interpolation=None)
    config.read("../Test_Campaign_2021/ConfigData/TermsCondition.ini")
    return config.get(section, key)

def checkSectionExistance(section):
    config = configparser.ConfigParser(interpolation=None)
    config.read("../Test_Campaign_2021/ConfigData/TermsCondition.ini")
    return config.has_section(section)

"""Config Data end Here"""

def Data(section):
    config = configparser.ConfigParser(interpolation=None)
    config.read("../ConfigData/canvas/abc.ini")
    return section


def readImageconfigData(section, key):
    config = configparser.ConfigParser(interpolation=None)
    config.read("../ConfigData/imageTest/data.ini")
    return config.get(section, key)


def read_test_canvas_Page_configData(section, key):
    config = configparser.ConfigParser(interpolation=None)
    config.read("../ConfigData/canvas/test_canvas.ini")
    return config.get(section, key)


def read_w37_fold2_canvas_Page_configData(section, key):
    config = configparser.ConfigParser(interpolation=None)
    config.read("../ConfigData/w37/w_37_fold2_canvas.ini")
    return config.get(section, key)


def read_w38_configData(section, key):
    config = configparser.ConfigParser(interpolation=None)
    config.read("../ConfigData/w38/w_38.ini")
    return config.get(section, key)


def read_w38_S7_Fold2_configData(section, key):
    config = configparser.ConfigParser(interpolation=None)
    config.read("../ConfigData/w38/w_38_S7_&_Fold2.ini")
    return config.get(section, key)


def read_w39_configData(section, key):
    config = configparser.ConfigParser(interpolation=None)
    config.read("../ConfigData/w39/w39_SeroTV.ini")
    return config.get(section, key)


def read_w39_S7_configData(section, key):
    config = configparser.ConfigParser(interpolation=None)
    config.read("../ConfigData/w39/w39_S7.ini")
    return config.get(section, key)


def read_w39_Fold2_configData(section, key):
    config = configparser.ConfigParser(interpolation=None)
    config.read("../ConfigData/w39/w39_Fold2.ini")
    return config.get(section, key)


def read_w40_Wearable_configData(section, key):
    config = configparser.ConfigParser(interpolation=None)
    config.read("../ConfigData/w40/w_40_Wearable.ini")
    return config.get(section, key)


def read_w40_GW3_configData(section, key):
    config = configparser.ConfigParser(interpolation=None)
    config.read("../ConfigData/w40/w_40_GW3.ini")
    return config.get(section, key)


def read_w41_S20FE_configData(section, key):
    config = configparser.ConfigParser(interpolation=None)
    config.read("../ConfigData/w41/w_41_S20FE_T1.ini")
    return config.get(section, key)


def read_w41_Bonanza_configData(section, key):
    config = configparser.ConfigParser(interpolation=None)
    config.read("../ConfigData/w41/w_41_UpgradeBonanza.ini")
    return config.get(section, key)


def read_w41_Fold2_configData(section, key):
    config = configparser.ConfigParser(interpolation=None)
    config.read("../ConfigData/w41/w41_Fold2.ini")
    return config.get(section, key)


def read_w41_S7_S7Plus_configData(section, key):
    config = configparser.ConfigParser(interpolation=None)
    config.read("../ConfigData/w41/w41_S7_S7Plus.ini")
    return config.get(section, key)


def read_w41_ReserveHoliday_configData(section, key):
    config = configparser.ConfigParser(interpolation=None)
    config.read("../ConfigData/w41/w41_ReserveHoliday.ini")
    return config.get(section, key)


def read_w42_HolidayReserve_configData(section, key):
    config = configparser.ConfigParser(interpolation=None)
    config.read("../ConfigData/w42/w42_HolidayReserve.ini")
    return config.get(section, key)


def read_w42_TVDeals_configData(section, key):
    config = configparser.ConfigParser(interpolation=None)
    config.read("../ConfigData/w42/w42_TVDeals.ini")
    return config.get(section, key)


def read_w42_PrimeDay_configData(section, key):
    config = configparser.ConfigParser(interpolation=None)
    config.read("../ConfigData/w42/w42_PrimeDay.ini")
    return config.get(section, key)


def read_w42_SoundBar_configData(section, key):
    config = configparser.ConfigParser(interpolation=None)
    config.read("../ConfigData/w42/w42_SoundBar.ini")
    return config.get(section, key)


def read_w42_S20FE_configData(section, key):
    config = configparser.ConfigParser(interpolation=None)
    config.read("../ConfigData/w42/w_42_S20FE.ini")
    return config.get(section, key)


def read_w42_TVSoundBarAutomation_configData(section, key):
    config = configparser.ConfigParser(interpolation=None)
    config.read("../ConfigData/w42/w42_TVSoundBarAutomation.ini")
    return config.get(section, key)


def read_w43_TVDealsT2_configData(section, key):
    config = configparser.ConfigParser(interpolation=None)
    config.read("../ConfigData/w43/w43_TVDeals_T2.ini")
    return config.get(section, key)


def read_w43_HolidayRsv_BounchBck_Catch2_configData(section, key):
    config = configparser.ConfigParser(interpolation=None)
    config.read("../ConfigData/w43/w43_HolidayReserve_BounchBck_Catch2.ini")
    return config.get(section, key)


def read_w44_HolidayReserveT2_configData(section, key):
    config = configparser.ConfigParser(interpolation=None)
    config.read("../ConfigData/w44/w44_HolidayReserveT2.ini")
    return config.get(section, key)


def read_w44_FlashSale_HA_configData(section, key):
    config = configparser.ConfigParser(interpolation=None)
    config.read("../ConfigData/w44/w44_FlashSale_HA.ini")
    return config.get(section, key)


def read_w44_Holiday_MCME_configData(section, key):
    config = configparser.ConfigParser(interpolation=None)
    config.read("../ConfigData/w44/w44_Holiday_MCME.ini")
    return config.get(section, key)


def read_w44_TVSoundBar_Auto_configData(section, key):
    config = configparser.ConfigParser(interpolation=None)
    config.read("../ConfigData/w44/w44_TVSoundBarAutomation.ini")
    return config.get(section, key)


def read_w45_EarlyAccess_HA_configData(section, key):
    config = configparser.ConfigParser(interpolation=None)
    config.read("../ConfigData/w45/w45_EarlyAccess_HA.ini")
    return config.get(section, key)


def read_w45_HolidayDealsT1_configData(section, key):
    config = configparser.ConfigParser(interpolation=None)
    config.read("../ConfigData/w45/w45_HolidayDeals_T1.ini")
    return config.get(section, key)


def read_w45_VateransDay_configData(section, key):
    config = configparser.ConfigParser(interpolation=None)
    config.read("../ConfigData/w45/w45_VateransDay.ini")
    return config.get(section, key)


def read_w46_HolidayReserve_BF_HHP_configData(section, key):
    config = configparser.ConfigParser(interpolation=None)
    config.read("../ConfigData/w46/w46_HolidayReserve_BF_HHP_FirstChance.ini")
    return config.get(section, key)


def read_w46_HolidayDeals_T2_configData(section, key):
    config = configparser.ConfigParser(interpolation=None)
    config.read("../ConfigData/w46/w46_HolidatDeals_T2.ini")
    return config.get(section, key)
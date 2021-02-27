import configparser
import os


"""Config Data start below"""


def readconfigData(section, key):
    config = configparser.ConfigParser(interpolation=None)
    config.read("../../configData/DataPage.ini")
    return config.get(section, key)


def readCopyTextData(section, key):
    config = configparser.ConfigParser(interpolation=None)
    config.read("../../configData/CopyText.ini")
    return config.get(section, key)


def readfooterData(section, key):
    config = configparser.ConfigParser(interpolation=None)
    config.read("../../configData/Footer.ini")
    return config.get(section, key)


def readFilePathData(section, key):
    config = configparser.ConfigParser(interpolation=None)
    config.read("../../configData/FilePaths.ini")
    return config.get(section, key)


def readModuleURLData(section, key):
    config = configparser.ConfigParser(interpolation=None)
    config.read("../../configData/ModuleURL.ini")
    return config.get(section, key)


def readTermsConditionData(section, key):
    config = configparser.ConfigParser(interpolation=None)
    config.read("../../configData/TermsCondition.ini")
    return config.get(section, key)


def checkSectionTermsExistance(section):
    config = configparser.ConfigParser(interpolation=None)
    config.read("../../configData/TermsCondition.ini")
    return config.has_section(section)


def checkSectionModuleExistance(section):
    config = configparser.ConfigParser(interpolation=None)
    config.read("../../configData/ModuleURL.ini")
    return config.has_section(section)


def checkSectionFooterExistance(section):
    config = configparser.ConfigParser(interpolation=None)
    config.read("../../configData/Footer.ini")
    return config.has_section(section)


def checkSectionCopyExistance(section):
    config = configparser.ConfigParser(interpolation=None)
    config.read("../../configData/CopyText.ini")
    return config.has_section(section)


def checkSectionFilePathExistance(section):
    config = configparser.ConfigParser(interpolation=None)
    config.read("../../configData/FilePaths.ini")
    return config.has_section(section)


"""Config Data end Here"""


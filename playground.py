# # def getAvailableOptions(state):
# #
# #
# # def getCurrentState():
# #
# #
# # def showOptions():
# #     return getAvailableOptions(getCurrentState())
# #
# # def start():
# #     goon = True
# #     while goon:
# #         print("Choose one of the options:")
# #
# #         userInput = str(input(""))
#
# def getCurrentShootingMode():
#     return "M"
#
#
# def getCurrentShutterSpeed():
#     return "1/1000s"
#
#
# def getCurrentAperture():
#     return "f/1.8"
#
#
# def getCurrentISO():
#     return 100
#
#
# def getCurrentFocusingMode():
#     return "AF"
#
#
# def getCurrentAFMode():
#     return "-C"
#
#
# def getCurrentExposure():
#     return 11.7
#
#
# def showCurrentExposure():
#     return "(- 2--1--0--1--2 +)"
#
#
# def getCurrentExposureCompensation():
#     return 0
#
# def getCurrentMeteringMode():
#     return "SPOT"
#
#
# def getCurrentWhiteBalance():
#     return 0
#
#
# def getCurrentFileFormat():
#     return "RAW + JPG"
#
#
# def getCurrentJPGQuality():
#     return "Fine"
#
#
#
#
#
# def currentSettingsDisplay():
#     displayPrint = ""
#     displayPrint += "-----------------\n" \
#                     "CURRENT SETTINGS\n"
#     displayPrint += "Mode " + str(getCurrentShootingMode()) + " "
#     displayPrint += "SS " + str(getCurrentShutterSpeed()) + " "
#     displayPrint += "Aperture " + str(getCurrentAperture()) + " "
#     displayPrint += "ISO " + str(getCurrentISO()) + "\n"
#     displayPrint += "Focusing " + str(getCurrentFocusingMode())
#     if getCurrentFocusingMode() == "AF":
#         displayPrint += str(getCurrentAFMode())
#     displayPrint += "\n"
#     displayPrint += "Exposure " + str(getCurrentExposure()) + \
#                     " " + str(showCurrentExposure()) + " "
#     displayPrint += "+/- " + str(getCurrentExposureCompensation()) + "\n"
#     displayPrint += "Metering mode " + str(getCurrentMeteringMode()) + "\n"
#     displayPrint += "White Balance " + str(getCurrentWhiteBalance()) + "\n"
#     displayPrint += "Image Quality " + str(getCurrentFileFormat())
#     if getCurrentFileFormat() in ["JPG", "RAW + JPG"]:
#         displayPrint += " " + str(getCurrentJPGQuality())
#
#     print(displayPrint)
#
# currentSettingsDisplay()
#
# class State:
#     pass
#
# class Settings:
#     def reset(self):
#         pass
#
# class QuickSettings(Settings):
#     pass
#
# class CaptureSettings(Settings):
#     pass
# class FileSettings(Settings):
#     pass
#
# class State:
#     pass
# class PowerState(State):
#     pass
# class BatteryState(State):
#     pass
# class MemoryCardState(State):
#     pass
#
#
#

# class A:
#     def __init__(self):
#         self.a = 1
#         self._b =2
#         self.__c=3
#
#     def geta(self):
#         return self.a
#     def getb(self):
#         return self.b
#     def getc(self):
#         return self.c
#
#     def getA(self):
#         return self.a
#     def getB(self):
#         return self._b
#     def getC(self):
#         return self.__c
#
#     def seta(self,a):
#         self.a = a
#     def setb(self,b):
#         self.b = b
#     def setc(self,c):
#         self.c = c
#
#     def setA(self,a):
#         self.a = a
#     def setB(self,b):
#         self._b = b
#     def setC(self,c):
#         self.__c = c

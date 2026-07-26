# ============================================
# Building Automation System
# EL 162 / EL 234 OOP Lab - Abstraction
# Author: Clement Arthur
# ============================================

# Import the abstraction module
from abc import ABC, abstractmethod


# Abstract Class
class BuildingSystem(ABC):

    # Abstract method
    @abstractmethod
    def start(self):
        pass

    # Abstract method
    @abstractmethod
    def stop(self):
        pass

    # Abstract method
    @abstractmethod
    def status(self):
        pass


# Child Class: Air Conditioning System
class AirConditioningSystem(BuildingSystem):

    def start(self):
        print("Air Conditioning System started.")

    def stop(self):
        print("Air Conditioning System stopped.")

    def status(self):
        print("Air Conditioning System is operating normally.")


# Child Class: Lighting System
class LightingSystem(BuildingSystem):

    def start(self):
        print("Lighting System switched on.")

    def stop(self):
        print("Lighting System switched off.")

    def status(self):
        print("Lighting System is operating normally.")


# Child Class: Security System
class SecuritySystem(BuildingSystem):

    def start(self):
        print("Security System activated.")

    def stop(self):
        print("Security System deactivated.")

    def status(self):
        print("Security System is monitoring the building.")


# New Child Class
class FireAlarmSystem(BuildingSystem):

    def start(self):
        print("Fire Alarm System activated.")

    def stop(self):
        print("Fire Alarm System deactivated.")

    def status(self):
        print("Fire Alarm System is ready for emergencies.")


# ============================================
# Create Objects
# ============================================

systems = [
    AirConditioningSystem(),
    LightingSystem(),
    SecuritySystem(),
    FireAlarmSystem()
]


# ============================================
# Demonstrate Polymorphism
# ============================================

for system in systems:
    print("\n-----------------------------")
    system.start()
    system.status()
    system.stop()
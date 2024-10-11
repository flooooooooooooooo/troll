import ctypes
from ctypes import wintypes
a = True
while a :
    # Définir les constantes pour le style de la boîte de message
    MB_OK = 0x00000000
    MB_ICONWARNING = 0x00000030
    MB_SYSTEMMODAL = 0x00001000

    # Définir le prototype de la fonction MessageBoxW
    MessageBoxW = ctypes.windll.user32.MessageBoxW
    MessageBoxW.argtypes = [wintypes.HWND, wintypes.LPCWSTR, wintypes.LPCWSTR, wintypes.UINT]
    MessageBoxW.restype = ctypes.c_int

    # Afficher la fenêtre d'avertissement
    def show_warning_box():
        MessageBoxW(None, "Système ne répond pas", "Ubuntu 22.04", MB_OK | MB_ICONWARNING | MB_SYSTEMMODAL)

    # Appeler la fonction pour afficher la fenêtre
    show_warning_box()
    a=False

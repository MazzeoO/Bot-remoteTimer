from ctypes import cast, POINTER
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


devices = AudioUtilities.GetSpeakers();
volume = devices.EndpointVolume


avol = 1

# ------------- Funções -----------


def setVol(a):

    a = a/100

    volume.SetMasterVolumeLevelScalar(a, None)
    print(f"Volume mudado para: {a * 100}%")


def volup():

    aVol = volume.GetMasterVolumeLevelScalar()
    nVol = aVol + 0.01

    verificVol(nVol) # para n repetir a verificação


    volume.SetMasterVolumeLevelScalar(nVol, None)

    print(f"Volume aumentado para: {nVol * 100}%") # vezes 100 para ficar como porcentagem.

    return int(nVol * 100)


def voldown():
    aVol = volume.GetMasterVolumeLevelScalar()
    nVol = aVol - 0.01

    verificVol(nVol)


    volume.SetMasterVolumeLevelScalar(nVol, None)

    print(f"Volume aumentado para: {nVol * 100}%")

    return int(nVol * 100)


def volmute():

    mute = volume.GetMute()

    if mute == 0:
        volume.SetMute(1, None)
        print(f"Volume Mutado")

    else:
        volume.SetMute(0, None)
        print(f"Volume Desmutado")
    
    return int(mute)
    




def verificVol(a):
    if a >= 1: # vol > 100 = 100
        a = 1

    elif a <= 0: # vol < 0 = 0
        a = 0

    return a

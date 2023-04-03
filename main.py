from datetime import datetime

def numberAsBinaryString(num: int) -> str:
    """
    :param num: Integer, A number to convert
    :return: An binary sequence string (read left to right (1,2,4,8,16))
    """

    binNumString = ('{0:05b}'.format(num))
    return binNumString


def binaryStringAsFingerLayout(bNum: str) -> dict:
    """
    :param bNum: String, A 5 digit binary sequence
    :return: A dictionary of each finger and its output configuration. Off == Finger up, On == Finger Down
    """

    pins = {
        "thumb": False,
        "index": False,
        "middle": False,
        "ring": False,
        "pinky": False,
    }

    for index, finger in enumerate(pins.keys()):
        pins[finger] = False if bNum[index] == "1" else True

    return pins


def numToFingerLayout(num: str) -> dict:
    """
    :param num: Integer, Hour up to 23
    :return: A dictionary of each finger and its output configuration. Off == Finger up, On == Finger Down
    """

    processedNum = numberAsBinaryString(num)
    fingerLayout = binaryStringAsFingerLayout(processedNum)
    return fingerLayout


currentTime = datetime.now().time().hour
print(currentTime, numToFingerLayout(currentTime))

def numberAsBinaryString(num: int) -> str:
    """
    :param num: Integer, A number to convert
    :return: An inverted binary sequence string (read left to right (1,2,4,8,16))
    """

    binNumString = ('{0:05b}'.format(num))[::-1]
    return binNumString

def binaryStringAsFingerLayout(bNum: str) -> dict:
    """
    :param bNum: String, A 5 digit inverted binary sequence
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

#Test 0h -> 23h
for num in range(24):
    processedNum = numberAsBinaryString(num)
    fingerLayout = binaryStringAsFingerLayout(processedNum)

    print(num, processedNum, fingerLayout)
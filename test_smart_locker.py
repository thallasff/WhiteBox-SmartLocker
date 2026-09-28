from smart_locker import evaluate_locker


def test_cold_chain_safe():
    assert evaluate_locker(
        "COLD_CHAIN",
        5,
        24,
        2,
        [5, 6, 4]
    ) == "SAFE"


def test_invalid_storage():
    assert evaluate_locker(
        "COLD_CHAIN",
        5,
        -1,
        1,
        []
    ) == "INVALID_INPUT"


def test_unknown_medicine():
    assert evaluate_locker(
        "UNKNOWN",
        5,
        20,
        1,
        []
    ) == "UNKNOWN_MEDICINE_TYPE"

def test_room_temp_safe():
    assert evaluate_locker(
        "ROOM_TEMP",
        20,
        24,
        2,
        [20, 21]
    ) == "SAFE"


def test_temperature_alert():
    assert evaluate_locker(
        "COLD_CHAIN",
        10,
        24,
        2,
        []
    ) == "TEMP_ALERT"


def test_storage_limit():
    assert evaluate_locker(
        "COLD_CHAIN",
        5,
        80,
        2,
        []
    ) == "STORAGE_LIMIT"

def test_one_abnormal_sensor():
    assert evaluate_locker(
        "COLD_CHAIN",
        5,
        24,
        2,
        [10]
    ) == "SAFE"


def test_access_warning():
    assert evaluate_locker(
        "COLD_CHAIN",
        5,
        24,
        7,
        []
    ) == "ACCESS_WARNING"


def test_quarantine():
    assert evaluate_locker(
        "COLD_CHAIN",
        5,
        24,
        2,
        [5, 11, 4, 12]
    ) == "QUARANTINE"

def test_invalid_door_count():
    assert evaluate_locker(
        "COLD_CHAIN",
        5,
        24,
        -1,
        []
    ) == "INVALID_INPUT"


def test_temperature_alert_low():
    assert evaluate_locker(
        "COLD_CHAIN",
        1,
        24,
        2,
        []
    ) == "TEMP_ALERT"


def test_low_abnormal_sensor():
    assert evaluate_locker(
        "COLD_CHAIN",
        5,
        24,
        2,
        [1]
    ) == "SAFE"


def test_temp_alert_not_overwritten():
    assert evaluate_locker(
        "COLD_CHAIN",
        10,
        24,
        7,
        [11, 12]
    ) == "TEMP_ALERT"
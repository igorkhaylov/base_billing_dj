import re
import random
import string
import datetime
import dateutil


def rosetta_access_control(user):
    return user.is_superuser or user.has_perm('auth.can_change_rosetta_messages')


def generate_random_username(length=12):
    characters = string.ascii_lowercase + string.digits
    return ''.join(random.choice(characters) for _ in range(length))


def get_username_type(username):
    regex_email = "[a-zA-Z][a-zA-Z0-9._%+-]*@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(\.[a-zA-Z]{2,})?$"
    regex_phone = "^[\+]998[0-9]{9}$"
    if re.match(regex_phone, str(username)):
        return "phone"
    elif re.match(regex_email, str(username)):
        return "email"
    return None


def get_ip_from_request(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip_address = x_forwarded_for.split(',')[0]
    else:
        ip_address = request.META.get('REMOTE_ADDR')
    return ip_address


def to_cyrillic_translate(s1):
    # Определение соответствия между символами латиницы и кириллицы
    eng_to_cyr = "`qwertyuiop[]asdfghjkl;'zxcvbnm,./"
    cyr_chars = "ёйцукенгшщзхъфывапролджэячсмитьбю."

    # Создание словаря перевода
    translation = {ord(eng): cyr for eng, cyr in zip(eng_to_cyr, cyr_chars)}

    return s1.translate(translation)


def format_size(bytes_size):
    """
    Функция принимает количество байтов и возвращает размер в удобочитаемом формате.
    """
    sizes = ['Bytes', 'KB', 'MB', 'GB', 'TB']

    if bytes_size == 0:
        return '0 Byte'

    i = 0
    while bytes_size >= 1024 and i < len(sizes) - 1:
        bytes_size /= 1024.0
        i += 1

    return "{:.2f} {}".format(bytes_size, sizes[i])


def generate_dates(start_date=None, count=31, step=1, unit="days"):
    """
    Генерирует даты на основе заданного начального дня, количества дат, шага и единицы измерения шага.

    :param start_date: Начальная дата'
    :param count: Количество дат для генерации
    :param step: Шаг между датами
    :param unit: Единица измерения шага ('days', 'weeks', 'months', 'years')
    :return: Список сгенерированных дат
    """
    if start_date is None:
        start_date = datetime.datetime.now().date()
    dates = [start_date]

    for _ in range(1, count):
        if unit == "days":
            next_date = dates[-1] + datetime.timedelta(days=step)
        elif unit == "weeks":
            next_date = dates[-1] + datetime.timedelta(weeks=step)
        elif unit == "months":
            next_date = dates[-1] + dateutil.relativedelta.relativedelta(months=step)
        elif unit == "years":
            next_date = dates[-1] + dateutil.relativedelta.relativedelta(years=step)
        else:
            raise ValueError("Unit must be 'days', 'weeks', 'months', or 'years'")
        dates.append(next_date)
    return dates

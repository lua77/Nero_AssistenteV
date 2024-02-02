from datetime import datetime


def hr():
    #função para horario atual
    hr_ = datetime.now().strftime('%H:%M')
    return hr_
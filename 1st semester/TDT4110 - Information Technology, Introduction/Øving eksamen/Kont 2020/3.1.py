def sec_to_time(s):
    if s < 3600:
        m = s // 60
        s = s % 60
        if s < 10:
            s = "0" + str(s)
        tid = str(m) + ":" + str(s)
        return tid
    else:
        t = s // 3600
        m = s // 60
        while m > 60:
            m -= 60
        s = s % 60
        if (m < 10):
            m = "0" + str(m)
        if s < 10:
            s = "0" + str(s)
        tid = str(t) + ":" + str(m) + ":" + str(s)
        return tid

print(sec_to_time(3729))
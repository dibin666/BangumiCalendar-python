from datetime import datetime, date


def genUUID(projectId, epsId, userid) -> str:
    return str(projectId) + "-" +str(epsId) + "-" + str(userid)


def genSummary(name, name_cn, ep) -> str:
    if name_cn != "":
        return name_cn + " " + str(ep)
    else:
        return name + " " + str(ep)


def genDec(summary, epname) -> str:
    str(epname).replace("/n","\n")
    return "「"+epname+"」" + "\n" + "\n"+ "\n"+ summary


def genDate(time) -> date:
    formats = ["%Y-%m-%d", "%Y年%m月%d日"]
    date = datetime.strptime(time, format)
    return date.date()

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

def genDate(time: str) -> date:
    formats = ["%Y-%m-%d", "%Y年%m月%d日"]
    for fmt in formats:
        try:
            parsed_date = datetime.strptime(time, fmt)
            return parsed_date.date()
        except ValueError:
            continue
    raise ValueError(f"time data '{time}' does not match any supported format")


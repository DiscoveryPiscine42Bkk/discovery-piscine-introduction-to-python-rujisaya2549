def find_the_redheads(family_dict):
    # ใช้ filter เพื่อกรองชื่อที่ผมสีแดง
    redheads = list(filter(lambda name: family_dict[name] == "red", family_dict.keys()))
    return redheads

dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
}

print(find_the_redheads(dupont_family
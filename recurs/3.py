def reverse(metin):
    if len(metin) == 0:
        return ""
    return metin[-1] + reverse(metin[:-1])

print(reverse("merhaba"))

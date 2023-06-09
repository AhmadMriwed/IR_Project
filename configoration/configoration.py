language_code='en'
language_code_ar='ar'
language_code_en='en'
cluster_exc = False
def change_language(language_code1):
    global language_code
    language_code=language_code1
def get_by_language(data_en,data_ar):
    if  language_code==language_code_ar:

        return data_ar
    else:
        return  data_en
def get_by_language_at_ln(data_en,data_ar,ln):
    if   ln==language_code_ar:
        return data_ar
    else:
        return  data_en
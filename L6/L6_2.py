def string_replace(s):
    if "'" in s:       
        return(s.replace("'", '"'))
    else:
        return(s.replace('"', "'"))

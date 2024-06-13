# ***********************
# SEPARANDO RECURSO SAMBA
# ***********************


def run(smb_path: str) -> tuple:
    doble_barra = smb_path.strip('//')
    index_bar = doble_barra.find('/')
    host = doble_barra[:index_bar]
    path = doble_barra[index_bar:]

    return host, path


if __name__ == '__main__':
    run('//1.1.1.1/aprende/python')

from subprocess import Popen, PIPE
import os
import platform

avs_pbi_path = "/usr/pbi/avs-" + platform.machine()
avs_etc_path = os.path.join(avs_pbi_path, "etc")
avs_mnt_path = os.path.join(avs_pbi_path, "mnt")
avs_fcgi_pidfile = "/var/run/avs.pid"
avs_fcgi_wwwdir = os.path.join(avs_pbi_path, "www")
avs_control = "/usr/local/etc/rc.d/avs"
avs_config = os.path.join(avs_etc_path, "mt-daapd.conf")
avs_icon = os.path.join(avs_pbi_path, "default.png")
avs_oauth_file = os.path.join(avs_pbi_path, ".oauth")


def get_rpc_url(request):
    return 'http%s://%s:%s/plugins/json-rpc/v1/' % (
        's' if request.is_secure() else '',
        request.META.get("SERVER_ADDR"),
        request.META.get("SERVER_PORT"),
        )


def get_avs_oauth_creds():
    f = open(avs_oauth_file)
    lines = f.readlines()
    f.close()

    key = secret = None
    for l in lines:
        l = l.strip()

        if l.startswith("key"):
            pair = l.split("=")
            if len(pair) > 1:
                key = pair[1].strip()

        elif l.startswith("secret"):
            pair = l.split("=")
            if len(pair) > 1:
                secret = pair[1].strip()

    return key, secret


avs_advanced_vars = {
    "set_cwd": {
        "type": "checkbox",
        "on": "-a",
        },
    "debuglevel": {
        "type": "textbox",
        "opt": "-d",
        },
    "debug_modules": {
        "type": "textbox",
        "opt": "-D",
        },
    "disable_mdns": {
        "type": "checkbox",
        "on": "-m",
        },
    "non_root_user": {
        "type": "checkbox",
        "on": "-y",
        },
    "ffid": {
        "type": "textbox",
        "opt": "-b",
        },
}

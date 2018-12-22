#!/usr/bin/python
# -*- coding:utf-8 -*-

import ipaddress

from collections import OrderedDict

from flask import Flask
from flask import render_template
from flask import jsonify
from flask import request

app = Flask(__name__)

# jinja_option = app.jinja_options.copy()
# jinja_option.update(dict(
#     variable_start_string = ""
# ))

app.jinja_env.variable_start_string = "(%"
app.jinja_env.variable_end_string = "%)"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/ip-detail", methods=["GET"])
def calc_ip():
    ip = request.values.get("ip", "")
    mask = request.values.get("mask", "")
    try:
        net = ipaddress.ip_network("{}/{}".format(ip, mask), strict=False)
        calc_rst = OrderedDict({
            "Net": net.with_prefixlen,
            "Mask": str(net.netmask),
            "TotalAvailableNum": net.num_addresses - 2,
            "First IP": str(net[1]),
            "Last IP": str(net[-2]),
            "NetworkAddress": str(net.network_address),
            "Bcast": str(net.broadcast_address)
        })
    except ValueError as err:
        print(err)
        calc_rst = {"ValueError": str(err)}

    return jsonify(calc_rst)


def main():
    app.run(host="0.0.0.0")


if __name__ == '__main__':
    main()

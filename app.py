from flask import Flask, render_template, request
from scanner import scan_target
import socket
import whois

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    results = None
    dns_result = None
    whois_result = None

    if request.method == "POST":

        target = request.form.get("target")
        start_port = int(request.form.get("start_port"))
        end_port = int(request.form.get("end_port"))

        results = scan_target(target, start_port, end_port)

        try:
            dns_result = socket.gethostbyname(target)
        except:
            dns_result = "DNS Lookup Failed"

        try:
            whois_result = whois.whois(target)
        except:
            whois_result = "WHOIS Lookup Failed"

    return render_template(
        "index.html",
        results=results,
        dns_result=dns_result,
        whois_result=whois_result
    )

if __name__ == "__main__":
    app.run(debug=True)
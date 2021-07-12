from flask import Flask, render_template, request

aplikasi = Flask(__name__)

@aplikasi.route("/")
def app():
    return render_template("lingkaran.html")

@aplikasi.route("/send", methods=["POST"])
def send(sum=sum):
    if request.method == "POST":
        lingkaran = request.form["lingkaran"]
        sum = float(lingkaran)
        result = (22 / 7 * sum * sum)
        sum2 = float(lingkaran)
        result2 = (2 * (22 / 7 * sum2))
        return render_template("lingkaran.html", sum=result, sum2=result2)
    else:
        return render_template("lingkaran.html")

if __name__ == '__main__':
    aplikasi.run(debug=True)

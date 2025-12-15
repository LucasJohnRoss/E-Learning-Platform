from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "dev-secret-key-change-later"  # needed for sessions

# Simple user login
VALID_USERNAME = "Employee"
VALID_PASSWORD = "password123"


# routing and authentication 

@app.route("/", methods=["GET"])
def root():
    # always send the user to the login page first
    return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    # if already logged in, skip login page
    if "user" in session:
        return redirect(url_for("home"))

    error = None

    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")

        if username == VALID_USERNAME and password == VALID_PASSWORD:
            session["user"] = username
            return redirect(url_for("home"))
        else:
            error = "Invalid username or password."

    return render_template("login.html", error=error)


@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))


# MAIN PAGES

@app.route("/home")
def home():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("index.html")


@app.route("/module1-info")
def module1_info():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("module1_info.html")


@app.route("/module2-info")
def module2_info():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("module2_info.html")


@app.route("/module3-info")
def module3_info():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("module3_info.html")


@app.route("/module4-info")
def module4_info():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("module4_info.html")


# module 1 quiz 

@app.route("/module1-phishing", methods=["GET", "POST"])
def module1_phishing():
    if "user" not in session:
        return redirect(url_for("login"))

    total = 4          # 4 matches, each worth 1 point
    score = 0
    error = None

    
    match_answers = {
        "email": "",
        "smish": "",
        "spear": "",
        "vish": "",
    }

    if request.method == "POST":
        email = request.form.get("q1_email", "")
        smish = request.form.get("q1_smish", "")
        spear = request.form.get("q1_spear", "")
        vish = request.form.get("q1_vish", "")

        match_answers = {
            "email": email,
            "smish": smish,
            "spear": spear,
            "vish": vish,
        }

        # make sure all four have been answered
        if not all([email, smish, spear, vish]):
            error = "Please complete all parts of the question before submitting."
            return render_template(
                "module1_phishing.html",
                finished=False,
                score=score,
                total=total,
                error=error,
                match_answers=match_answers,
            )

        if email == "4":   # Email phishing - 4
            score += 1
        if smish == "2":   # Smishing - 2
            score += 1
        if spear == "1":   # Spear phishing - 1
            score += 1
        if vish == "3":    # Vishing - 3
            score += 1

        return render_template(
            "module1_phishing.html",
            finished=True,
            score=score,
            total=total,
            error=None,
            match_answers=match_answers,
        )

    # GET requests
    return render_template(
        "module1_phishing.html",
        finished=False,
        score=score,
        total=total,
        error=error,
        match_answers=match_answers,
    )

@app.route("/module2-malware", methods=["GET", "POST"])
def module2_malware():
    if "user" not in session:
        return redirect(url_for("login"))

    total = 4
    score = 0
    error = None

    match_answers = {
        "virus": "",
        "trojan": "",
        "ransomware": "",
        "adware": "",
    }

    if request.method == "POST":
        virus = request.form.get("q1_virus", "")
        trojan = request.form.get("q1_trojan", "")
        ransomware = request.form.get("q1_ransomware", "")
        adware = request.form.get("q1_adware", "")

        match_answers = {
            "virus": virus,
            "trojan": trojan,
            "ransomware": ransomware,
            "adware": adware,
        }

        if not all(match_answers.values()):
            error = "Please complete all parts of the question before submitting."
            return render_template(
                "module2_malware.html",
                finished=False,
                score=score,
                total=total,
                error=error,
                match_answers=match_answers,
            )

        if virus == "1":
            score += 1
        if trojan == "2":
            score += 1
        if ransomware == "3":
            score += 1
        if adware == "4":
            score += 1

        return render_template(
            "module2_malware.html",
            finished=True,
            score=score,
            total=total,
            error=None,
            match_answers=match_answers,
        )

    return render_template(
        "module2_malware.html",
        finished=False,
        score=score,
        total=total,
        error=error,
        match_answers=match_answers,
    )


@app.route("/module3-passwords", methods=["GET", "POST"])
def module3_passwords():
    if "user" not in session:
        return redirect(url_for("login"))

    total = 4
    score = 0
    error = None

    match_answers = {
        "strong": "",
        "reuse": "",
        "mfa": "",
        "share": "",
    }

    if request.method == "POST":
        strong = request.form.get("q1_strong", "")
        reuse = request.form.get("q1_reuse", "")
        mfa = request.form.get("q1_mfa", "")
        share = request.form.get("q1_share", "")

        match_answers = {
            "strong": strong,
            "reuse": reuse,
            "mfa": mfa,
            "share": share,
        }

        if not all(match_answers.values()):
            error = "Please complete all parts of the question before submitting."
            return render_template(
                "module3_passwords.html",
                finished=False,
                score=score,
                total=total,
                error=error,
                match_answers=match_answers,
            )

        # Correct mapping (1–4)
        if strong == "1":
            score += 1
        if reuse == "2":
            score += 1
        if mfa == "3":
            score += 1
        if share == "4":
            score += 1

        return render_template(
            "module3_passwords.html",
            finished=True,
            score=score,
            total=total,
            error=None,
            match_answers=match_answers,
        )

    return render_template(
        "module3_passwords.html",
        finished=False,
        score=score,
        total=total,
        error=error,
        match_answers=match_answers,
    )


@app.route("/module4-payments", methods=["GET", "POST"])
def module4_payments():
    if "user" not in session:
        return redirect(url_for("login"))

    total = 4
    score = 0
    error = None

    match_answers = {
        "verify": "",
        "trusted": "",
        "invoice": "",
        "card": "",
    }

    if request.method == "POST":
        verify = request.form.get("q1_verify", "")
        trusted = request.form.get("q1_trusted", "")
        invoice = request.form.get("q1_invoice", "")
        card = request.form.get("q1_card", "")

        match_answers = {
            "verify": verify,
            "trusted": trusted,
            "invoice": invoice,
            "card": card,
        }

        if not all(match_answers.values()):
            error = "Please complete all parts of the question before submitting."
            return render_template(
                "module4_payments.html",
                finished=False,
                score=score,
                total=total,
                error=error,
                match_answers=match_answers,
            )

        # Correct mapping (1–4)
        if verify == "1":
            score += 1
        if trusted == "2":
            score += 1
        if invoice == "3":
            score += 1
        if card == "4":
            score += 1

        return render_template(
            "module4_payments.html",
            finished=True,
            score=score,
            total=total,
            error=None,
            match_answers=match_answers,
        )

    return render_template(
        "module4_payments.html",
        finished=False,
        score=score,
        total=total,
        error=error,
        match_answers=match_answers,
    )


if __name__ == "__main__":
    app.run(debug=True)




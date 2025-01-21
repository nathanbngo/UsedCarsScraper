from flask import Flask, render_template, request, redirect, url_for, send_file, flash
from scripts.utils import setup_driver, scrape_car_data, save_to_excel, visualize_data
import os

app = Flask(__name__)
app.secret_key = "secret"
UPLOAD_FOLDER = "data"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/scrape", methods=["POST"])
def scrape():
    url = request.form["url"]
    if not url:
        flash("Please enter a valid URL!")
        return redirect(url_for("index"))

    try:
        driver = setup_driver()
        car_data = scrape_car_data(driver, url)
        driver.quit()

        file_path = os.path.join(UPLOAD_FOLDER, "used_cars.xlsx")
        save_to_excel(car_data, file_path)
        flash("Data scraped and saved successfully!")
        return redirect(url_for("index"))
    except Exception as e:
        flash(f"Error occurred: {e}")
        return redirect(url_for("index"))

@app.route("/download")
def download():
    file_path = os.path.join(UPLOAD_FOLDER, "used_cars.xlsx")
    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True)
    flash("No data file available to download!")
    return redirect(url_for("index"))

@app.route("/visualize")
def visualize():
    file_path = os.path.join(UPLOAD_FOLDER, "used_cars.xlsx")
    try:
        visualize_data(file_path)
        flash("Visualization generated successfully!")
        return redirect(url_for("index"))
    except Exception as e:
        flash(f"Failed to visualize data: {e}")
        return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)

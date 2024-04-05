from flask import Flask,render_template, request
import CustomCalender
import datetime

app = Flask(__name__, template_folder="html")



@app.route("/", methods=["GET"])
def home():
    current_date = datetime.date.today()
    current_year = current_date.year
    months_data = {}
    for month_num in range(1, 13):
        month_name = datetime.date(current_year, month_num, 1).strftime("%B")
        month_data = CustomCalender.get_calendar(current_year, month_num)
        months_data[month_name.lower()] = month_data

    for month, days in months_data.items():
        for index, day_string in enumerate(days):
            day_components = day_string.split()
            for i, component in enumerate(day_components):
                if component.isdigit():
                    day_components[i] = f'<label for="{component.zfill(2)}{month[:3]}" class="custom-radio">{component.zfill(2)} </label>'
                    day_components.append(f'<input id="{component.zfill(2)}{month[:3]}" type="radio" name="option" value="{component.zfill(2)}{month[:3]}">')
            months_data[month][index] = '\n    '.join(day_components)

    return render_template("index.html", months_data=months_data)

@app.route("/submit", methods=["GET"])
def submit():
    return request.args
    
app.run("127.0.0.1",port=4001)

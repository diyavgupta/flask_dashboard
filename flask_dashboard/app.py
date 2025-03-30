from flask import Flask, render_template, request
import plotly.express as px
import pandas as pd
import json
import plotly

app = Flask(__name__)

# Function to load coffee export data
def load_data():
    df = pd.read_csv("coffee_exports.csv")  # Make sure to add your CSV file later
    return df

@app.route("/", methods=["GET", "POST"])
def index():
    df = load_data()
    chart_type = request.form.get("chart_type", "box")

    # Generate the selected chart type
    if chart_type == "bar":
        fig = px.bar(df, x="Country", y="Total_Exports", title="Coffee Exports by Country")
    elif chart_type == "scatter":
        fig = px.scatter(df, x="Country", y="Total_Exports", title="Coffee Export Scatter Plot")
    else:
        fig = px.box(df, x="Country", y="Total_Exports", title="Coffee Export Box Plot")

    # Update plot layout
    fig.update_layout(plot_bgcolor='#1a1c23', paper_bgcolor='#1a1c23', font_color='#ffffff')

    # Convert plot to JSON
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template("index.html", graphJSON=graphJSON, chart_type=chart_type)

if __name__ == "__main__":
    app.run(debug=True)

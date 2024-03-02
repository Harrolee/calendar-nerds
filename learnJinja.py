from jinja2 import Environment, FileSystemLoader

results_filename = "final_calendar.html"
environment = Environment(loader=FileSystemLoader("templates/"))
template = environment.get_template("calendar.html")
context = {
    "img_path" : "/Users/lee/calendarNerds/ascend.png",
    "cal_desc" : "descriotuon here"
}
with open(results_filename, mode="w", encoding="utf-8") as results:
    results.write(template.render(context))
    print("wrote to " + results_filename)
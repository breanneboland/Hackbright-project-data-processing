import csv

survey_results = open("survey_responses.csv")

survey_responses_dict = {
    "infrequent": {}


}

def count_answers():
    readable_survey = csv.reader(survey_results)
    for row in readable_survey:
        if row[1] == "Once a week"
            count
        elif row[1] == "Once a month"
        elif row[1] == "Once every six months"
        elif row[1] == "Once a year"
        else:
            #I haven't eaten at a food truck tally 


count_answers()

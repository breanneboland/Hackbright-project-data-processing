survey_results = open("survey_responses.csv")

class Survey_result(object):
    """
    Magically turns survey result rows into objects in a listings
    """

    def __init__(self, row):
        frequency = row[0]
        ways_of_finding = row[1]
        needed_info = row[2]
        desired_features = row[3]
        fave_truck = row[4]
        fave_truck_resource = row[5]
        fave_food_resource = row[6]
        most_important_info = row[7]
        pun = row[8]

        self.frequency = frequency
        self.ways_of_finding = ways_of_finding
        self.needed_info = needed_info
        self.desired_features = desired_features
        self.fave_truck = fave_truck
        self.fave_truck_resource = fave_truck_resource
        self.fave_food_resource = fave_food_resource        
        self.most_important_info = most_important_info
        self.pun = pun

object_list = []

def make_survey_objects():
    for row in survey_results:
        temp_object = Survey_result(row)
        object_list.append(temp_object)

    return object_list


def tally_survey_objects():
    pass 




# ['Once a year', 'At a gathering or festival', 'Type of food', 'An interactive map, Text listings with search, Search by food type', '', '', '', '', 'Location that day', '']
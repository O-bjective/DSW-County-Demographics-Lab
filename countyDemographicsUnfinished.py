import json

def main():
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    print(alphabetically_first_county(counties))
    print(county_most_under_18(counties))
    print(percent_most_under_18(counties))
    print(most_under_18(counties))
    print(state_with_most_counties(counties))

def alphabetically_first_county(counties):
    """Return the county with the name that comes first alphabetically."""
    first = counties[0]["County"]
    for county in counties :
        if county["County"] < first:
            first = county["County"]
    return first

def county_most_under_18(counties):
    """Return the name and state of a county ("<county name>, <state>") with the highest percent of under 18 year olds."""
    state = counties[0]["State"]
    for county in counties :
        if county["State"] < state:
            state = county["State"]
    return state


def percent_most_under_18(counties):
    """Return the highest percent of under 18 year olds."""
    pmu18 = counties[0]["Age"]["Percent Under 18 Years"]
    for county in counties:
        if county["Age"]["Percent Under 18 Years"] < 18:
            pmu18 = county["Age"]["Percent Under 18 Years"]
    return pmu18

def most_under_18(counties):
    """Return a list with the name and state of a county ("<county name>, <state>") and the percent of under 18 year olds for a county with the highest percent of under 18 year olds."""
    state = counties[0]["Age"]["Percent Under 18 Years"]
    for county in counties:
        if county["Age"]["Percent Under 18 Years"] < 18:
            state = county["Age"]["Percent Under 18 Years"]
    return state

def state_with_most_counties(counties):
    """Return a state that has the most counties."""
    #Make a dictionary that has a key for each state and the values keep track of the number of counties in each state
    dict = {}
    most = 0
    st = ""
    for state in counties:
        if state["State"] in dict:
            dict[state["State"]] += 1
        else:
            dict[state["State"]] = 1
    for county in counties:
        if 
    #Find the state in the dictionary with the most counties

    #Return the state with the most counties


def your_interesting_demographic_function(counties):
    """Compute and return an interesting fact using the demographic data about the counties in the US."""

if __name__ == '__main__':
    main()

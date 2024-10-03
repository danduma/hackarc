from data_loading import load_cohort_data, load_death_data, load_grip_strength_data
import os
from db_functions import create_database

create_database()

# Load the grip strength data
# load_grip_strength_data( "/Users/masterman/Downloads/LEVF/Behavioral Testing/Grip strength")

# load_cohort_data("/Users/masterman/Downloads/LEVF/Mouse MasterIndex__ NOT CURRENT - Weights.csv")

load_death_data("/Users/masterman/Downloads/LEVF/Mouse Death Sheet _ CL 2024-10-02 STILL UPDATING FROM JUNE.xlsx")
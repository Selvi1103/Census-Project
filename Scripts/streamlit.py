#Task 7: Run Query on the database and show output on streamlit

import streamlit as st1
import pandas as pd
import mysql.connector
from mysql.connector import Error


#connecting Mysql 
def get_connection():
       
    connect=st1.connection('mysql',type='sql')
    return connect

def execute_query(query):
    connect=get_connection()
    df=connect.query(query,ttl='10m')
    return pd.DataFrame(df)
#Queries
Queries={'Total population of each district':'select District,Population as Total_Population from census;',
'Total Literate males and females in each district':'select District,Literate_Male, Literate_Female from census;',
'Percentage of workers (both male and female) in each district':'select District,(Male_Workers/Population)*100 as Percentage_Male_Population,(Female_Workers/Population)*100 as Percentage_Female_Population from census;',
'Total Households have access to LPG or PNG as a cooking fuel in each district':'select District,LPG_or_PNG_Households from census;',
'Religious composition (Hindus, Muslims, Christians, etc.) of each district':'select District,Hindus,Muslims,Christians,Sikhs,Buddhists,Jains,Others_Religions from census;',
'Total Households have internet access in each district?':'select District,Housewith_Internet from census;',
'Educational attainment distribution (below primary, primary, middle, secondary, etc.) in each district':'select District,Below_Primary_Education,Primary_Education,Middle_Education,Secondary_Education,Higher_Education,Graduate_Education,Other_Education from census;',
'Total Households have access to various modes of transportation (bicycle, car, radio, television, etc.) in each district':'select District,Housewith_Bicycle,Housewith_Car_Jeep_Van,Housewith_Radio_Transistor,Housewith_Scooter_Motorcycle_Moped,Housewith_Telephone_Mobile_Phone_Landline_only,Housewith_Telephone_Mobile_Phone_Mobile_only,Housewith_TV_PC_Ltop_Telph_mphone_Scooter_Car,Housewith_Television,Housewith_Telephone_Mobile_Phone,Housewith_Telephone_Mobile_Phone_Both from census;',
'Condition of occupied census houses (dilapidated, with separate kitchen, with bathing facility, with latrine facility, etc.) in each district':'select District,Condition_of_occupied_census_houses_Dilapidated_Houses,Housewith_separate_kitchen_Cooking_inside_house,Having_bathing_facility_Total_Households,Having_latrine_facility_within_the_premises_Total_Houses,Type_of_bathing_facility_Enclosure_without_roof_Houses,Type_of_latrine_facility_Pit_latrine_Houses,Type_of_latrine_facility_Other_latrine_Houses,Not_having_bathing_facility_within_the_premises_Houses,Not_hav_latfacility_within_the_premises_Altern_src_Open_Houses from census;',
'Household size distributed (1 person, 2 persons, 3-5 persons, etc.) in each district':'select District,Household_size_1_person_Households,Household_size_2_persons_Households,Household_size_1_to_2_persons,Household_size_3_persons_Households,Household_size_3_to_5_persons_Households,Household_size_4_persons_Households,Household_size_5_persons_Households,Household_size_6_8_persons_Households,Household_size_9_persons_and_above_Households from census;',
'Total number of households in each state':'select State_UT,sum(Households) from census group by State_UT;',
'Total Households have a latrine facility within the premises in each state':'select State_UT,sum(Having_latrine_facility_within_the_premises_Total_Houses) as Latrine_facility_within_the_premises from census group by State_UT;',
'Average household size in each state':'select State_UT, avg(Household_size_1_person_Households) as 1_person_Households,avg(Household_size_2_persons_Households) as 2_persons_Households ,avg(Household_size_1_to_2_persons) as 1_to_2_persons_Households,avg(Household_size_3_persons_Households) as 3_persons_Households,avg(Household_size_3_to_5_persons_Households) as 3_to_5_persons_Households,avg(Household_size_4_persons_Households) as 4_persons_Households,avg(Household_size_5_persons_Households) as 5_persons_Households,avg(Household_size_6_8_persons_Households) as 6to8_persons_Households,avg(Household_size_9_persons_and_above_Households) as 9_above_persons_Households from census group by State_UT;',
'Number of Households are owned versus rented in each state':'Select State_UT, sum(Ownership_Owned_Households) as Owned,sum(Ownership_Rented_Households) as Rented from census group by State_UT;',
'Different types of latrine facilities (pit latrine, flush latrine, etc.) in each state':'Select State_UT,sum(Type_of_latrine_facility_Pit_latrine_Houses) as Pit_latrine,sum(Type_of_latrine_facility_Other_latrine_Houses) as Other_latrine,sum(Type_of_latfacility_Nightsoil_disposed_in_open_drain_Houses) as Nightsoil_disposed_in_open_drain_Houses,sum(Type_of_latfacility_Flush_pour_latrine_connec_toother_Houses) as Flush_latrine from census group by State_UT;',
'Households have access to drinking water sources near the premises in each state':'Select State_UT,sum(Location_of_drinking_water_source_Near_the_premises_Houses) as Drinking_water_source_Near_the_premises from census group by State_UT;',
'Average household income distribution in each state based on the power parity categories':'select State_UT,avg(Power_Parity_Less_than_Rs_45000),avg(Power_Parity_Rs_45000_90000),avg(Power_Parity_Rs_90000_150000),avg(Power_Parity_Rs_45000_150000) ,avg(Power_Parity_Rs_150000_240000) ,avg(Power_Parity_Rs_240000_330000) ,avg(Power_Parity_Rs_150000_330000),avg(Power_Parity_Rs_330000_425000),avg(Power_Parity_Rs_425000_545000),avg(Power_Parity_Rs_330000_545000),avg(Power_Parity_Above_Rs_545000) from census group by State_UT;',
'Percentage of married couples with different household sizes in each state':'select State_UT,(sum(Married_couples_1_Households)*100)/sum(Households) as Percent_Married_couples_1,(sum(Married_couples_2_Households)*100)/sum(Households) as Percent_Married_couples_2,(sum(Married_couples_3_Households)*100)/sum(Households) as Percent_Married_couples_3,(sum(Married_couples_3_or_more_Households)*100)/sum(Households) as Percent_Married_couples_3_or_more,(sum(Married_couples_4_Households)*100)/sum(Households) as Percent_Married_couples_4,(sum(Married_couples_5__Households)*100)/sum(Households) as Percent_Married_couples_5,(sum(Married_couples_None_Households)*100)/sum(Households) as Percent_No_Married_couples from census group by State_UT;',
'Households fall below the poverty line in each state based on the power parity categories':'select State_UT,sum(Power_Parity_Less_than_Rs_45000) as Households_fall_below_the_povertyline from census group by State_UT;',
'Overall literacy rate (percentage of literate population) in each state':'select state_UT,(sum(Literate_Education)*100)/sum(Total_Education) as Percentage_of_literate_population from census group by state_UT;',
} 
#Executing Quries and diplaying the output in interactive straemlit Dashboard
st1.title("Census Data Analysis")
selected_query = st1.sidebar.selectbox('Select a Query',list(Queries.keys()))
if selected_query:
    st1.subheader(selected_query)
    query=Queries[selected_query]

    try:
        result = execute_query(query)
        st1.dataframe(result, height=700,width=700,hide_index=True)
    except Exception as e:
        st1.error(f"An error occured while executing the query:{e}")
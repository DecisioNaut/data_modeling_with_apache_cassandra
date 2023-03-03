# Data Modeling With Apache Cassandra
***A Project in Course of Udacity's Nano-Degree for Data Engineering With AWS***

## Introduction

For learning more about data engineering, I've decided to do Udacity's nano-degree program for Data Engineering With AWS. Having done such programs in the past, I'm looking foreward to learning about data engineering through practical exercises.

The first project in course of this program is "Data Modeling With Apache Cassandra. Apache Cassandra is an open-source No-SQL database, or, to be more specific, a key-value store. So this exercise is all about learning to model data the "No-SQL way" meaning creating a datamodel whose design focusses on performance rather than on flexibility of arbitrary querying.

Udacity describes the task as follows:

> **Project: Data Modeling with Cassandra**  
> A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analysis team is particularly interested in understanding what songs users are listening to. Currently, there is no easy way to query the data to generate the results, since the data reside in a directory of CSV files on user activity on the app.
> 
> They'd like a data engineer to create an Apache Cassandra database which can create queries on song play data to answer the questions, and wish to bring you on the project. Your role is to create a database for this analysis. You'll be able to test your database by running queries given to you by the analytics team from Sparkify to create the results.
>
> **Project Overview**  
> In this project, you'll apply what you've learned on data modeling with Apache Cassandra and complete an ETL pipeline using Python. To complete the project, you will need to model your data by creating tables in Apache Cassandra to run queries. You are provided with part of the ETL pipeline that transfers data from a set of CSV files within a directory to create a streamlined CSV file to model and insert data into Apache Cassandra tables.
>
> We have provided you with a project template that takes care of all the imports and provides a structure for ETL pipeline you'd need to process this data.

Although it may be convenient to make use of the provided project template, I've decided to do this exercise from scratch. This way I can learn more about the process of installing cassandra on a/my machine and of creating a data model for Apache Cassandra using python. Furthermore, I can build some helper functions to generate a cleaner notebook.  
I hope the reviewer of this project will forgive me for this ;-)

## Project Structure

Udacity provides a project template `Project_1B_Project_Template.ipynb` on the root level of the project. Included in this template is a picture contained in the folder `images`. This template serves me as a starting point for this project, but **my actual work is contained in the notebook `Project_1B_Project.ipynb`**. I moved them **both to the folder `notebooks`** to keep the root level cleaner. 

Furthermore, it provides a folder `event_data` which contains the data to be processed. The folder files `2018-11-01-events.csv` to `2018-11-30-events.csv`, which contain the actual data to be used in this project. I **moved this folder into the folder `data`**, again, to keep the root level cleaner. **Preprocessed data can be found in the folder `data/preprocessed`**. 

Lastly, **I've created a package contained in `src` which contains the code for some functionality** to make the notebook a bit cleaner.

## Project Requirements

**Requirements for this specific project** are:
- Python 3.11.2
- Pandas 1.5.3
- Numpy 1.24.2
- Cassandra-driver 3.25.0
I chose these as they were also used in the project template (although Pandas and Numpy are actually not needed in this project). I've installed them using poetry. For pip users, please find the requirements in the file `requirements.txt`.

**Installing Apache Cassandra on macOS** (my machine) is easy using homebrew. I've installed it using the following command:

    brew install cassandra

**Starting and stopping Apache Cassandra** was also easy. I've started it using the following command:

    brew services start cassandra
    brew services stop cassandra


